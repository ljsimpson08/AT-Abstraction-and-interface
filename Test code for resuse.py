
import json
import requests
from requests.api import get

def getToken():
    ## Creates a token and supplies token via return value. 
    ## User name and Password will need to be re-configured within bank using app2app service account
    username = 'admin'
    password = 'Hobbit1937!'
    tokenUrl = 'https://164.90.209.85/api/v2/tokens/'
    data = {
        "description":"My Access Token",
        "application":2,
        "scope":"write"
    }
    target = requests.post(tokenUrl, auth=(username, password), verify=False)
    rawData = target.text
    parseData = json.loads(rawData)
    return parseData["token"]

def getUser(token):
    tokenUrl = 'https://164.90.209.85/api/v2/users/'   
    header = {'Authorization':'Bearer ' + token,}
    data = {}
    target = requests.request('GET', tokenUrl, verify=False, headers=header, data=data, allow_redirects=False)
    rawData = target.text
    parseData = json.loads(rawData)
    return parseData

def buildUser(token):
    tokenUrl = 'https://164.90.209.85/api/v2/users/'   
    header = {'Authorization':'Bearer ' + token, 'Content-Type': 'application/json',}
    data = {
    "username":'mrtest',
    "first_name":'loyd',
    "last_name":'simpson',
    "email":'ljsimpson08@gmail.com',
    "is_superuser":True,
    "is_system_auditor":True,
    "password":'password'
    }
    target = requests.request('POST', tokenUrl, verify=False, headers=header, json=data, allow_redirects=False)
    rawData = target.text
    parseData = json.loads(rawData)
    return parseData

def getProject(token):
    tokenUrl = 'https://164.90.209.85/api/v2/proojects/'   
    header = {'Authorization':'Bearer ' + token,}
    data = {}
    target = requests.request('GET', tokenUrl, verify=False, headers=header, data=data, allow_redirects=False)
    rawData = target.text
    parseData = json.loads(rawData)
    return parseData

def getTeam(token):
    tokenUrl = 'https://164.90.209.85/api/v2/teams/'   
    header = {'Authorization':'Bearer ' + token, 'Content-Type': 'application/json',}
    data = {}
    target = requests.request('GET', tokenUrl, verify=False, headers=header, data=data, allow_redirects=False)
    rawData = target.text
    parseData = json.loads(rawData)
    return parseData

def getOrg(token):
    tokenUrl = 'https://164.90.209.85/api/v2/organizations/'   
    header = {'Authorization':'Bearer ' + token, 'Content-Type':'application/json',}
    data = {
    }
    target = requests.request('GET', tokenUrl, verify=False, headers=header, json=data, allow_redirects=False)
    rawData = target.text
    parseData = json.loads(rawData)
    return parseData

def adminOrg(token):
    tokenUrl = 'https://164.90.209.85/api/v2/Organizations/'   
    header = {'Authorization':'Bearer ' + token,}
    data = {}
    target = requests.request('POST', tokenUrl, verify=False, headers=header, json=data, allow_redirects=False)
    rawData = target.text
    parseData = json.loads(rawData)
    return parseData

def buildOrg(token):
    tokenUrl = 'https://164.90.209.85/api/v2/organizations/'   
    header = {'Authorization':'Bearer ' + token, 'Content-Type':'application/json',}
    data = {
        'name':'Test Org',
        'description':'Testing organization creation using API interface'
    }
    target = requests.request('POST', tokenUrl, verify=False, headers=header, json=data, allow_redirects=False)
    rawData = target.text
    parseData = json.loads(rawData)
    return parseData

def orgKill(token, tName):
    tempList = getOrg(token)
    tempDict = parseOrgList(tempList)
    for key, value in tempDict:
        if value == tName:
            tKey = key 
    tokenUrl = 'https://164.90.209.85/api/v2/organizations/',tKey,'/'   
    header = {'Authorization':'Bearer ' + token, 'Content-Type':'application/json',}
    data = {
        'name':'Test Org',
        'description':'Testing organization creation using API interface'
    }
    target = requests.request('POST', tokenUrl, verify=False, headers=header, json=data, allow_redirects=False)
    rawData = target.text
    parseData = json.loads(rawData)
    return parseData    

def getHost(token):
    tokenUrl = 'https://164.90.209.85/api/v2/hosts/'   
    header = {'Authorization':'Bearer ' + token,}
    data = {}
    target = requests.request('GET', tokenUrl, verify=False, headers=header, data=data, allow_redirects=False)
    rawData = target.text
    parseData = json.loads(rawData)
    return parseData

def getJob(token):
    tokenUrl = 'https://164.90.209.85/api/v2/jobs/'   
    header = {'Authorization':'Bearer ' + token,}
    data = {}
    target = requests.request('GET', tokenUrl, verify=False, headers=header, data=data, allow_redirects=False)
    rawData = target.text
    parseData = json.loads(rawData)
    return parseData

def parseOrgList(list):
    list = (list.get("results"))
    tempDict = {}
    for i in list:
        for key, value in i.items():
            if key == 'id':
                cId = i.get(key)
            if key == 'name':
                cName = i.get(key)
                tempDict.update({cId:cName})
    return tempDict

#Get token tested successfully
cToken = getToken()

#Get user has been tested successfully
#userList = getUser(cToken)

#Build user tested successfully
#bUser = buildUser(cToken)

#jobList = getJob(cToken)

#teamList = getTeam(cToken)

#Get org tested successfully
orgList = getOrg(cToken)

#target = 'Test Org'

#result = orgKill(cToken, target)

#Build org tested successfully
#bOrg = buildOrg(cToken)

#result = parseOrgList(orgList);


#hostList = getHost(cToken)

#projectList = getProject(cToken)

dictList = (orgList.get("results"))
#for i in dictList:
#   for key, value in i.items():
#       print(key, value, "\n")

tempDict = {}

#Code for searching object looksups in Ansible Tower API
for i in dictList:
    for key, value in i.items():
        if key == 'id':
           cId = i.get(key)
        if key == 'name':
           cName = i.get(key)
           tempDict.update({cId:cName})

for key, value in tempDict.items():
    print(key, value)

#for key, value in tempDict:
#    print("This is org 1: ",key, value, '\n')

#for key, value in orgList.items():
#    print(key, value)


