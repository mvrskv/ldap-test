#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import urllib
import urllib2
import json
#from copy import deepcopy

from config import * 

headers = {'Content-Type': 'application/json',
           'Accept': 'application/json'}


def postreq(url, body, headers):
    '''POST request'''
    Body = json.dumps(body)
    request = urllib2.Request(url, Body, headers)
    response = urllib2.urlopen(request)
    return json.loads(response.read())    

def getreq(url, header):
    '''GET request'''
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    return json.loads(response.read())    

def gettoken(username, password, tenant_name = None):
    '''POST / tokens. Authentificate by exchanging credentials for an access token'''
    url = service_url + 'tokens'
    body =  {"auth": {"passwordCredentials": 
                      {"username": username, "password": password}}}
    if tenant_name:
        body['auth']['tenantId'] = tenant_name 
    #try:
    token = postreq(url, body, headers)
    return token
    #except:
    #    return None

def gettenants(token):
    '''# GET / tenants. List all of the tenants accessible for the token'''
    token_id = token['access']['token']['id']
    headers = {'X-Auth-Token': token_id,
               'user-agent': 'python-keystoneclient'}
    url = service_url + 'tenants'
    tenants = getreq(url, headers)['tenants']
    return tenants

def getroles(token, tenant_id):
    '''POST / tokens. Get list all of the roles for the token in the tenant'''
    token_id = token['access']['token']['id']
    headers = {'X-Auth-Token': token_id,
               'user-agent': 'python-keystoneclient',
               'content-type': 'application/json'}
    url = service_url + 'tokens'
    body =  {"auth": {"token": 
                      {"id": token_id},
                      "tenantId": tenant_id }}
    try:
        roles = postreq(url, body, headers)
        return roles
    except:
        return None

def main():
    '''Manual tests. Deprecated'''
    exit()
    print "===== Authorization with specifying a tenant ======"
    tokens = {}
    tenant_tokens = {}
    for u in users:
        print u,
        for t in tenants:
            tokens[u] = gettoken(u, users[u]['password'], t)
            if tokens[u]:
                user_id = tokens[u]['access']['user']['id']
                tenant_id = tokens[u]['access']['token']['tenant']['id']
                token_id = tokens[u]['access']['token']['id']
                #tokens[u]['token_tenants'] = gettenants(tokens[u])
                print '\t(' + tenant_id + ')', "OK",
            else:
                print '\t(' + t + ')', "None",
        print
    #print tokens
    
    print "===== Authorization without specifying a tenant ======"
    tokens = {}
    tenant_tokens = {}
    for u in users:
        tokens[u] = gettoken(u, users[u]['password'])
        if tokens[u]:
            user_id = tokens[u]['access']['user']['id']
            print user_id, '\tOK'
        else:
            print u, "\tNone"
    
    print "===== Accessible tenants for each user ======"
    tokens = {}
    tenant_tokens = {}
    for u in users:
        tokens[u] = gettoken(u, users[u]['password'])
        if tokens[u]:
            user_id = tokens[u]['access']['user']['id']
            tokens[u]['tenants'] = gettenants(tokens[u])
            print user_id, '(', 
            for t in tokens[u]['tenants']:
                print t['id'],
            print ')'
        else:
            print u, "\tNone\t"
    
    print "===== Roles in tenants for each user ======"
    tokens = {}
    tenant_tokens = {}
    for u in users:
        tokens[u] = gettoken(u, users[u]['password'])
        if tokens[u]:
            user_id = tokens[u]['access']['user']['id']
            tokens[u]['tenants'] = gettenants(tokens[u])
            print user_id, 
            for t in tokens[u]['tenants']:
                t['roles'] = getroles(tokens[u], t) 
                print '(' + t['id'], 
                for r in t['roles']['access']['user']['roles']:
                    print '[' + r['id'] + ']',
                print ')', 
            print
        else:
            print u, "\tNone"
    
if __name__ == "__main__":
    main()