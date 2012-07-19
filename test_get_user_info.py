#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import unittest

import config
from get_user_info import *


class TestGetUserInfo(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass


# GLOBAL !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition tests for each user ...
for u in config.users:
    # ... in each tenant
    for t in config.tenants:
        # define test function for authorization with specifying a tenant for each user in each tenant
        def auth_w_spec_tenant(self, username = u, password = users[u]['password'], tenant_name = t):
            "Authorization in tenant "
            token = gettoken(username, password, tenant_name)
            #------------------- print token['access']['token']['id'] + ' ... '
            self.assert_(token['access']['token']['id'])
            # сравнить имя пользователя с полученным в токене - в конфиг написать expected-result
            # expected result может быть exception
        # Setting up docstring for this test
        auth_w_spec_tenant.__doc__ += t + " for user " + u
        # Setting up test name
        auth_w_spec_tenant.__name__ = "test_" + auth_w_spec_tenant.__name__ + '_' + u + '_'+ t
        # setting up test as unittest-based class
        setattr(TestGetUserInfo, auth_w_spec_tenant.__name__, auth_w_spec_tenant)
        # delete pointer for test from current namespace
        del auth_w_spec_tenant


    # define test function for authorization without specifying a tenant for each user
    def test_auth_wo_spec_tenant(self, username = u, password = users[u]['password']):
        "Authorization without specifying tenant for user "
        token = gettoken(username, password)
        #------------------------ print token['access']['token']['id'] + ' ... '
        self.assert_(token['access']['token']['id'])
        # сравнить имя пользователя с полученным в токене - в конфиг написать expected-result
        # expected result может быть exception
    # Setting up docstring for this test
    test_auth_wo_spec_tenant.__doc__ += u
    # Setting up test name
    test_auth_wo_spec_tenant.__name__ += '_' + u
    # setting up test as unittest-based class
    setattr(TestGetUserInfo, test_auth_wo_spec_tenant.__name__, test_auth_wo_spec_tenant)
    # delete pointer for test from current namespace
    del test_auth_wo_spec_tenant


    # define test function for getting avalable tenants for user
    def test_get_avalable_tenants_for_token(self, username = u, password = users[u]['password']):
        "Avalable tenants for user "
        token = gettoken(username, password)
        tenants = gettenants(token)
        #------------------------------------------------------- print username,
        #---------------------------------------------------- for tt in tenants:
            #------------------------------------------ print tt['name'] + ', ',
        #----------------------------------------------------------------- print
        self.assert_(tenants)
        # сравнить список токенов в конфиге с полученным  - в конфиг написать expected-result
        # expected result может быть exception
    # Setting up docstring for this test
    test_get_avalable_tenants_for_token.__doc__ += u
    # Setting up test name
    test_get_avalable_tenants_for_token.__name__ += '_' + u
    # setting up test as unittest-based class
    setattr(TestGetUserInfo, test_get_avalable_tenants_for_token.__name__, test_get_avalable_tenants_for_token)
    # delete pointer for test from current namespace
    del test_get_avalable_tenants_for_token


    # define test function for getting roles in avalable tenants for user
    def test_get_avalable_tenants_for_token(self, username = u, password = users[u]['password']):
        "Roles in avalable tenants for user "
        token = gettoken(username, password)
        tenants = gettenants(token)
        for tt in tenants:
            roles = getroles (token, tt)
        self.assert_(roles)
        # сравнить список токенов в конфиге с полученным  - в конфиг написать expected-result
        # expected result может быть exception
    # Setting up docstring for this test
    test_get_avalable_tenants_for_token.__doc__ += u
    # Setting up test name
    test_get_avalable_tenants_for_token.__name__ += '_' + u
    # setting up test as unittest-based class
    setattr(TestGetUserInfo, test_get_avalable_tenants_for_token.__name__, test_get_avalable_tenants_for_token)
    # delete pointer for test from current namespace
    del test_get_avalable_tenants_for_token



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
