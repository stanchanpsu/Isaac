from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpResponse
from personal.models import EngineeringAmbassador
from .models import Group
from django.core import serializers
import json, requests, operator, string, random, time


groupme_url = "https://api.groupme.com/v3"
push_url = "https://push.groupme.com/faye"

@ensure_csrf_cookie
@login_required(login_url='/login/')
def groupme(request):
    
	# if groupme callbacks with the access token of the user
	if request.GET and 'access_token' in request.GET:
		request.session['access_token'] = request.GET['access_token']
		access_token = request.session['access_token']
		
		parameters = {"token":access_token}
		me = requests.get(groupme_url + "/users/me", params = parameters)
		
		ambassador = get_object_or_404(EngineeringAmbassador,user = request.user)
		
		groupme_id = me.json()['response']["id"]
		
		ambassador.groupme_id = groupme_id		
		ambassador.save()
		
		return redirect('/groupme/')
	
	# if regular page request by user	
	else:
		# if user logged into groupme
		if 'access_token' in request.session:
			stylesheet = 'groupme/chat.css'
			script = 'groupme/chat.js'
			
			# store all the isaac groups in groups
			user = request.user
			ambassador = get_object_or_404(EngineeringAmbassador, user = user)
			groups = ambassador.group_set.all()
			
			
			#create a list of isaac groups and a dictionary for matching relevant groupme groups
			isaac_groups = []
			relevant_groups = {}
			
			# iterating through groups append their group_id to isaac_groups
			for group in groups:
				isaac_groups.append(group.group_id)
			
			# get request to groupme for all a user's groupme groups (up to 20)
			params = {"token":request.session['access_token'], "per_page":20}
			groupme_groups = requests.get(groupme_url + "/groups", params = params)
			
			#reinstantiate the variable to store only the response object portion
			groupme_groups = groupme_groups.json()['response']
			
			# iterate through these groupme groups and compare them to Isaac_groups, if they match store their id and name in relevant groups
			for group in groupme_groups:
				if group['group_id'] in isaac_groups:
					relevant_groups[group['group_id']] = group['name']
					
			relevant_groups = sorted(relevant_groups.items(), key=operator.itemgetter(1))
			#pass on only relevant groups to template
			return render(request, 'groupme/groupme.html',{'stylesheet':stylesheet, 'script':script, 'relevant_groups':relevant_groups,})
			
		#if user is logged out of groupme
		else:
			auth_url = 'https://oauth.groupme.com/oauth/authorize?client_id=bnveOko8sTysD27ugGxOL5HhPeBmrxhzmXdewuXarxi50FOk'
			return render(request, 'groupme/groupme.html',{'auth_url':auth_url,})
			
@ensure_csrf_cookie
@login_required(login_url='/login/')
def token(request):			
	if request.is_ajax():
		if 'access_token' in request.session:
			token = request.session['access_token']
			
			headers = {"Content-Type":"application/json"}
			
			data = json.dumps([{"channel":"/meta/handshake","version":"1.0", "supportedConnectionTypes":["long-polling"], "id":1}])
			
			handshake = requests.post(push_url,data=data, headers=headers)
			
			signature = handshake.json()[0]["clientId"]
			params = {"token":token}
			me = requests.get(groupme_url + "/users/me", params = params)
			
			user_id = me.json()["response"]["id"]
			
			data = json.dumps([{"channel":"/meta/subscribe","clientId":signature,"subscription":"/user/" + user_id, "id":2,"ext":{"access_token":token,"timestamp":time.time()}}])
			
			sub_user_channel = requests.post(push_url, data=data, headers=headers)	
			
			response = json.dumps({"token":token, "handshake":handshake.json()[0], "sub_user_channel":sub_user_channel.json()[0]})
			response = JsonResponse(response,safe=False)
			return response
		else:
			return redirect('/groupme/')
	else:
		return redirect('/groupme/')

@login_required(login_url='/login/')		
def group(request):
	if request.is_ajax():
		if 'access_token' in request.session:
			token = request.session['access_token']
			if 'json_data' in request.POST:
				message_data = json.loads(request.POST.get('json_data'))
				group_id = str(message_data["group_id"])
				clientId = message_data["clientId"]
				id = message_data["id"]
				data = json.dumps([{
					"channel":"/meta/subscribe","clientId":clientId,"subscription":"/group/"+group_id,"id":id,"ext":{"access_token":token,"timestamp":time.time()}
				}])
				
				headers = {"Content-Type":"application/json"}
				
				sub_group_channel = requests.post(push_url, data=data, headers=headers)
				
				response = sub_group_channel.json()
				response = JsonResponse(response, safe=False)
				return response
				

# @ensure_csrf_cookie	
# @login_required(login_url='/login/')
# def getGroups(request):
# 	if request.is_ajax():
		
# 		user = request.user
# 		ambassador = get_object_or_404(EngineeringAmbassador, user = user)
# 		groups = ambassador.group_set.all()
# 		groups = serializers.serialize("json", groups)
# 		response = JsonResponse(groups, safe=False)
# 		return response
		
# 	else:
# 		return redirect('/groupme/')

@login_required(login_url='/login/')
def message(request):
	if request.is_ajax():
		if 'access_token' in request.session:
			token = request.session['access_token']
			if 'json_data' in request.POST:
				#contains text and group_id
				message_data = json.loads(request.POST.get('json_data'))
				
				text = message_data["text"]
				guid = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
				group_id = str(message_data["group_id"])
				data = json.dumps({"message":{"source_guid":guid, "text":text}})
				headers = {"X-Access-Token": token, "Content-Type":"application/json"}
				send_message = requests.post(groupme_url+'/groups/'+group_id+'/messages', headers = headers, data = data )
	
				response = send_message.json()
	return JsonResponse(response, safe=False)
	
@login_required(login_url='/login/')
def longpoll(request):
	# return JsonResponse(json.dumps("hello"),safe=False)
	if request.is_ajax():
		if 'access_token' in request.session:
			token = request.session['access_token']
			if 'json_data' in request.POST:
				message_data = json.loads(request.POST.get('json_data'))
				clientId = message_data["clientId"]
				id = message_data["id"]
				headers = {"Content-Type":"application/json"}
			
				data = json.dumps([{"channel":"/meta/connect","clientId":clientId,"connectionType":"long-polling","id":id}])
				
				pollMessages = requests.post(push_url, data=data,headers=headers)
				
				response = pollMessages.json()
	# response = json.dumps("hello")
				
	return JsonResponse(response,safe=False)