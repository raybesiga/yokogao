from django.shortcuts import render
import requests
import json
from dateutil.parser import parse
from datetime import timedelta
from gitit.settings import GITHUB_USER


def index(request):
    yoko = requests.get('https://api.github.com/users/%s' % GITHUB_USER)
    context = yoko.json()

    context['created_at'] = parse(context['created_at'], dayfirst=False, yearfirst=True)
    context['updated_at'] = parse(context['updated_at'], dayfirst=False, yearfirst=True)

    return render(request, 'yokogao/index.html', context)

def repo_list(request):
    yoko = requests.get('https://api.github.com/users/%s/repos' % GITHUB_USER)
    context = {}
    context['repos'] = yoko.json()

    return render(request, 'yokogao/repo_list.html', context)

def repo_detail(request, repo_name):
    url = "https://api.github.com/repos/{0}/{1}".format(GITHUB_USER, repo_name)
    repo = requests.get(url)
    context = dict()
    context['repo'] = repo.json()
    context['repo']['pushed_at'] = parse(context['repo']['pushed_at'],
                                         dayfirst=False, yearfirst=True)

    langs = requests.get(context['repo']['languages_url']).json()
    context['languages'] = langs

    issues = requests.get(context['repo']['url'] + '/issues')
    if issues.json():
        context['issues'] = issues.json()

    return render(request, 'yokogao/repo_detail.html', context)

def follower_list(request):
    url = "https://api.github.com/users/{0}/followers".format(GITHUB_USER)
    followers = requests.get(url)
    context = {}
    context['followers'] = followers.json()
    return render(request, 'yokogao/follower_list.html', context)

def following_list(request):
    url = "https://api.github.com/users/{0}/following".format(GITHUB_USER)
    following = requests.get(url)
    context = {}
    context['following'] = following.json()
    return render(request, 'yokogao/following_list.html', context)
