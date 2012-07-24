#!/usr/bin/env python
# -*- coding: utf-8 -*-


service_url = 'http://172.18.67.57:5000/v2.0/'
#admin_token = 'JOPxsy8WmrFEiTxR_b_w'


#===============================================================================
# tenants_ID = 
# {
#    'tenant_1_name': 'tenant_1_id', 
#    'tenant_2_name': 'tenant_2_id', 
#    'tenant_3_name': 'tenant_3_id',
# } 
#===============================================================================

tenant_ids = {
              't1':'t1',
              't2':'t2'
              #=================================================================
              # 't1': 'd547dc29ffbf478eaec6a8bc59484756', 
              # 't2': '74f1a3e00f1c42ef8f191aab49f5f3bf'
              #=================================================================
              } 


#===============================================================================
# users=
# {
#    'UserName': 
#    {
#        'password':'Password_phrase',
#        'roles':
#        {
#            'g':'Global_role_name',
#            't1':'Tenant_1_role',
#            't2':None
#        }
#    },
# }
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
                'test_get_roles_in_tenant':                 {'t1':set(['member']), 't2':False},
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
                'test_get_roles_in_tenant':                {'t1':False, 't2':set(['member'])},
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
                'test_get_roles_in_tenant':                {'t1':set(['admin']), 't2':set(['member'])},
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
                'test_get_roles_in_tenant':                 {'t1':set(['member']), 't2':set(['admin'])},
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
       }



