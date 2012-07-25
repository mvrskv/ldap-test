#!/usr/bin/env python
# -*- coding: utf-8 -*-


service_url = 'http://172.18.67.60:5000/v2.0/'
#admin_token = 'JOPxsy8WmrFEiTxR_b_w'


#===============================================================================
# tenant_ids = 
# {
#    'tenant_1_name': 'tenant_1_id', 
#    'tenant_2_name': 'tenant_2_id', 
#    'tenant_3_name': 'tenant_3_id',
# } 
#===============================================================================

tenant_ids = {
            't1': '2534d910499a4eb0adfb150ed4b77e15', 
            't2': 'e254970338f34201bab9394f0fce3f24'
              } 


#===============================================================================
# users=
# {
#    'UserName': 
#    {
#        'password':'Password_phrase',
#        'expected_result':
#        {
#            '<TestName>': <Expected_result>,
#            '<TestName>': <Expected_result>,
#        }
#    },
# }
# <TestName> must coincide with 'testname' variable value, that defined in 
# each test_ function, for example:
#    testname = 'test_auth_w_spec_tenant'
# <Expected_result> may be defined for each test individually, test function
# use this. Examples:
# 'expected_result':
# {
#    'test_auth_w_spec_tenant':                  {'t1':True, 't2':False},
#    'test_auth_wo_spec_tenant':                 True,
#    'test_get_available_tenants':               set(['t1']),
#    'test_get_roles_in_tenant':                 {'t1':set(['admin']), 't2':False},
# }
# In test 'test_get_roles_in_tenant' set([]) != False
#    'test_get_roles_in_tenant':                 {'t1':False, 't2':set([])},

#===============================================================================

users={
        # Admin in t1 tenant
       't1a': 
       {
            'password':'Mirantis123',
            'expected_result':
            {
                'test_auth_w_spec_tenant':                  {'t1':True, 't2':False},
                'test_auth_wo_spec_tenant':                 True,
                'test_get_available_tenants':               set(['t1']),
                'test_get_roles_in_tenant':                 {'t1':set(['admin']), 't2':False},
            }
        },
        # Member in t1 tenant
       't1m': 
       {
            'password':'Mirantis123',
            'expected_result':
            {
                'test_auth_w_spec_tenant':                  {'t1':True, 't2':False},
                'test_auth_wo_spec_tenant':                 True,
                'test_get_available_tenants':               set(['t1']),
                'test_get_roles_in_tenant':                 {'t1':set(['Member']), 't2':False},
            }
        },
        # Admin in t2 tenant (and has membership but has no roles in t1) 
       't2a': 
       {
            'password':'Mirantis123',
            'expected_result':
            {
                'test_auth_w_spec_tenant':                  {'t1':False, 't2':True},
                'test_auth_wo_spec_tenant':                 True,
                'test_get_available_tenants':               set(['t2']),
                'test_get_roles_in_tenant':                 {'t1':False, 't2':set(['admin'])},
            }
        },
        # Member in t2 tenant (and has membership but has no roles in t1) 
       't2m': 
       {
            'password':'Mirantis123',
            'expected_result':
            {
                'test_auth_w_spec_tenant':                 {'t1':False, 't2':True},
                'test_auth_wo_spec_tenant':                True,
                'test_get_available_tenants':              set(['t2']),
                'test_get_roles_in_tenant':                {'t1':False, 't2':set(['Member'])},
            }
        },
        # Admin in t1 tenant and member in t2 tenant
       't1at2m': 
       {
            'password':'Mirantis123',
            'expected_result':
            {
                'test_auth_w_spec_tenant':                 {'t1':True, 't2':True},
                'test_auth_wo_spec_tenant':                True,
                'test_get_available_tenants':              set(['t1','t2']),
                'test_get_roles_in_tenant':                {'t1':set(['admin']), 't2':set(['Member'])},
            }
        },
        # Member in t1 tenant and admin in t2 tenant
       't1mt2a': 
       {
            'password':'Mirantis123',
            'expected_result':
            {
                'test_auth_w_spec_tenant':                  {'t1':True, 't2':True},
                'test_auth_wo_spec_tenant':                 True,
                'test_get_available_tenants':               set(['t1','t2']),
                'test_get_roles_in_tenant':                 {'t1':set(['Member']), 't2':set(['admin'])},
            }
        },
        # fake user
       'fake': 
       {
            'password':'Superuser',
            'expected_result':
            {
                'test_auth_w_spec_tenant':                  {'t1':False, 't2':False},
                'test_auth_wo_spec_tenant':                 False,
                'test_get_available_tenants':               False,
                'test_get_roles_in_tenant':                 {'t1':False, 't2':False},
            }
        },
        # user in tenant 1 without specified roles
       't1wor': 
       {
            'password':'Mirantis123',
            'expected_result':
            {
                'test_auth_w_spec_tenant':                  {'t1':True, 't2':False},
                'test_auth_wo_spec_tenant':                 True,
                'test_get_available_tenants':               set(['t1']),
                'test_get_roles_in_tenant':                 {'t1':set([]), 't2':False},
            }
        },
        # user in tenant 1 without specified roles
       't2wor': 
       {
            'password':'Mirantis123',
            'expected_result':
            {
                'test_auth_w_spec_tenant':                  {'t1':False, 't2':True},
                'test_auth_wo_spec_tenant':                 True,
                'test_get_available_tenants':               set(['t2']),
                'test_get_roles_in_tenant':                 {'t1':False, 't2':set([])},
            }
        },
       }



