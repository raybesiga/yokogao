from django.shortcuts import render, HttpResponse
import requests
# import json

def index(request):
    yoko = requests.get('https://api.github.com/users/raybesiga')
    lisht = []
    lisht.append(yoko.json())
    cleanedData = []
    yokogaoData = {}
    for data in lisht:
        yokogaoData['name'] = data['name']
        yokogaoData['blog'] = data['blog']
        yokogaoData['email'] = data['email']
        yokogaoData['public_gists'] = data['public_gists']
        yokogaoData['public_repos'] = data['public_repos']
        yokogaoData['avatar_url'] = data['avatar_url']
        yokogaoData['followers'] = data['followers']
        yokogaoData['following'] = data['following']
        yokogaoData['location'] = data['location']
        yokogaoData['created_at'] = data['created_at']
        yokogaoData['updated_at'] = data['updated_at']
    cleanedData.append(yokogaoData)
    return render(request, 'yokogao/index.html', {'data': yokogaoData})

# def index(request):
#     jsonList = []
#     req = requests.get('https://api.github.com/users/raybesiga')
#     jsonList.append(json.loads(req.content))
#     parsedData = []
#     userData = {}
#     for data in jsonList:
#         userData['name'] = data['name']
#         userData['blog'] = data['blog']
#         userData['email'] = data['email']
#         userData['public_gists'] = data['public_gists']
#         userData['public_repos'] = data['public_repos']
#         userData['avatar_url'] = data['avatar_url']
#         userData['followers'] = data['followers']
#         userData['following'] = data['following']
#     parsedData.append(userData)
#     return render(request, 'yokogao/index.html', {'data': userData})
#     # return HttpResponse(parsedData)
