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
    for t in config.tenant_ids:
        # define test function for authorization with specifying a tenant for each user in each tenant
        def test_auth_w_spec_tenant(self, username = u, password = users[u]['password'], tenant_id = t):
            "Authorization in tenant_id "
            # attribute for extracting expected result
            testname = 'test_auth_w_spec_tenant'
            try:
                token = gettoken(username, password, tenant_id)
                if token['access']['user']['name'] == username:
                    result = True
            except:
                result = False
            # get expected_result in config
            expected_result = config.users[username]['expected_result'][testname][tenant_id]
            self.assertEqual(expected_result, result)
        # Setting up docstring for this test
        test_auth_w_spec_tenant.__doc__ += '"' + t + '" for user "' + u + '" must be "' + str(config.users[u]['expected_result'][test_auth_w_spec_tenant.__name__][t]) + '"'
        # Setting up test name
        test_auth_w_spec_tenant.__name__ += '_' + u + '_in_' + t
        # setting up test as unittest-based class
        setattr(TestGetUserInfo, test_auth_w_spec_tenant.__name__, test_auth_w_spec_tenant)
        # delete pointer for test from current namespace
        del test_auth_w_spec_tenant


# GLOBAL !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition tests for each user ...
for u in config.users:
    # define test function for authorization without specifying a tenant for each user
    def test_auth_wo_spec_tenant(self, username = u, password = users[u]['password']):
        "Authorization without specifying tenant for user "
        # attribute for extracting expected result
        testname = 'test_auth_wo_spec_tenant'
        try:
            token = gettoken(username, password)
            if token['access']['user']['name'] == username:
                result = True
        except:
            result = False
        # get expected_result inconfig
        expected_result = config.users[username]['expected_result'][testname]
        self.assertEqual(expected_result, result)
    # Setting up docstring for this test
    test_auth_wo_spec_tenant.__doc__ += '"' + u + '" must be "' + str(config.users[u]['expected_result'][test_auth_wo_spec_tenant.__name__]) + '"' 
    # Setting up test name
    test_auth_wo_spec_tenant.__name__ += '_' + u
    # setting up test as unittest-based class
    setattr(TestGetUserInfo, test_auth_wo_spec_tenant.__name__, test_auth_wo_spec_tenant)
    # delete pointer for test from current namespace
    del test_auth_wo_spec_tenant


# GLOBAL !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition tests for each user ...
for u in config.users:
    # define test function for getting avalable tenants for user
    def test_get_available_tenants(self, username = u, password = users[u]['password']):
        "Avalable tenants for user "
        # attribute for extracting expected result
        testname = 'test_get_available_tenants'
        try:
            token = gettoken(username, password)
            if token['access']['user']['name'] == username:
                try:
                    tenants = gettenants(token)
                    result = set()
                    for tt in tenants:
                        result.add(tt['name'])
                except:
                    result = False
        except:
            result = False
        # get expected_result inconfig
        expected_result = config.users[username]['expected_result'][testname]
        self.assertEqual(expected_result, result)
    # Setting up docstring for this test
    test_get_available_tenants.__doc__ += '"' + u + '" must be "' + str(config.users[u]['expected_result'][test_get_available_tenants.__name__]) + '"'
    # Setting up test name
    test_get_available_tenants.__name__ += '_' + u
    # setting up test as unittest-based class
    setattr(TestGetUserInfo, test_get_available_tenants.__name__, test_get_available_tenants)
    # delete pointer for test from current namespace
    del test_get_available_tenants


# GLOBAL !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition tests for each user ...
for u in config.users:
    for t in config.tenant_ids:
        # define test function for getting available tenants for user
        def test_get_roles_in_tenant(self, username = u, password = users[u]['password'], tenant_id = t):
            "Roles in tenant "
            # attribute for extracting expected result
            testname = 'test_get_roles_in_tenant'
            result = set()
            try:
                token = gettoken(username, password)
                if token['access']['user']['name'] == username:
                    try:
                        roles = getroles (token, tenant_id)
                        if roles:
                            for r in roles['access']['user']['roles']:
                                result.add(r['name'])
                        else:
                            result = False
                    except:
                        result = False
            except:
                result = False
            # get expected_result inconfig
            expected_result = config.users[username]['expected_result'][testname][tenant_id]
            self.assertEqual(expected_result, result)
        # Setting up docstring for this test
        test_get_roles_in_tenant.__doc__ += "'" + t + '" for user "' + u + '" must be "' + str(config.users[u]['expected_result'][test_get_roles_in_tenant.__name__][t]) + '"'
        # Setting up test name
        test_get_roles_in_tenant.__name__ += '_' + u + '_in_' + t
        # setting up test as unittest-based class
        setattr(TestGetUserInfo, test_get_roles_in_tenant.__name__, test_get_roles_in_tenant)
        # delete pointer for test from current namespace
        del test_get_roles_in_tenant


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
