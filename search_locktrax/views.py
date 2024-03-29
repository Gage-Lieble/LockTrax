from turtle import right
from django.shortcuts import render
import urllib.request
from urllib.request import Request, urlopen
import json
from .forms import *
# Create your views here.

def index(request):

    form = NameSearchForm()

    context = {
        'form': form
    }
    return render (request, 'search_temp/index.html', context)

def results(request):
   
    state_form = request.POST['state'] # Users state
    source_url = 'https://www.jailbase.com/api/1/sources/'
    request_sources = Request(source_url, headers={'User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(request_sources) as url:
        sources = json.loads(url.read().decode())
    

    # Finds all counties in selected state
    counties = []
    index = 0
    for items in sources['records']:
        if str(sources['records'][index]['state_full']) == str(state_form): # If result matches user intput
            county = sources['records'][index]['source_id']
            counties.append(county)
        index += 1
    first_name = request.POST['first']
    last_name = request.POST['last']
    
    # Finds all results in each county
    result = []
    
    for places in counties:
        county = places
        search_link = f'http://www.jailbase.com/api/1/search/?source_id={county}&last_name={last_name}&first_name={first_name}'
        request_site = Request(search_link, headers={'User-Agent':'Mozilla/5.0'}) # 403 ERROR fixed by adding USER-AGENT
        with urllib.request.urlopen(request_site) as url:
            data = json.loads(url.read().decode())
        if data['records'] != []:
            
            result.append(data['records'])
    
    
    index = 0 
    full_details = {}
    while index < len(result[0]):
        name = result[0][index]['name'] #0

        age = result[0][index]['details'][2][1] #1
        try:
            race = result[0][index]['details'][1][1] #2 
            if race == 'HISPANIC':
                race = 'h'
            elif race == 'asian':
                race = 'a'
            elif race.rstrip() == 'other':
                race = 'N/A'
            
        except IndexError:
            race = 'N/A'
        try:
            gender = result[0][index]['details'][0][1] #3 
        except IndexError:
            gender = 'N/A'
        try:
            height = result[0][index]['details'][3][1] #4 
        except IndexError:
            height = 'N/A'
        try:
            weight = result[0][index]['details'][4][1] #5
        except IndexError:
            weight = 'N/A'
        try:
            mugshot = result[0][index]['mugshot'] #6 
        except IndexError:
            mugshot = 'N/A'
        try:
            county_in = result[0][index]['county_state'] #7
        except IndexError:
            county_in = 'N/A'
        
        try:
            pre_split_charges = result[0][index]['charges'] #8
            charges = []
            for items in pre_split_charges: # Exctracts charge from other info
                remove = '/'
                stripped = items.split(remove)
                charges.append(stripped[1])
        except IndexError:
            pre_split_charges = ['N/A']
            charges = ['N/A']
        try:
            date_booked = result[0][index]['book_date'] #9
        except IndexError:
            date_booked = 'N/A'
        full_details[index] = [name, age, race, gender, height, weight, mugshot, county_in, charges, date_booked]
        index += 1

        
    context = {
        'result': full_details,
        'sources': counties,
    }
    return render(request, 'search_temp/result.html', context)

