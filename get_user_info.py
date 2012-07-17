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

def getroles(token, tenant):
    '''POST / tokens. Get list all of the roles for the token in the tenant'''
    token_id = token['access']['token']['id']
    tenant_id = tenant['id']
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

class tests():
    pass

def generate_auth_wo_spec_tenant_tests(cls):
    for u in users:
        def test_auth_wo_spec_tenant_user(self, username = u, password = users[u]['password']):
            print '(' + username, password + ')'
            #return gettoken(username, password)
        test_auth_wo_spec_tenant_user.__doc__ = "Authorization without specifying tenant for " + u
        test_auth_wo_spec_tenant_user.__name__ = "test_auth_wo_spec_tenant_" + u
        setattr(cls, test_auth_wo_spec_tenant_user.__name__, test_auth_wo_spec_tenant_user)
        #test_auth_wo_spec_tenant_user()
        
    
def main():
    generate_auth_wo_spec_tenant_tests(tests)
    ts = tests()
    #print tests.__dict__
    for t in tests.__dict__:
        if not t.startswith("__"):
            print getattr(tests, t), '(' + getattr(tests, t).__doc__ + ')',
            getattr(tests, t) (ts)

if __name__ == '__main__':
    main()

