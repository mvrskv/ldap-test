#!/usr/bin/env python
# -*- coding: utf-8 -*-


service_url = 'http://172.18.67.57:5000/v2.0/'
#admin_token = 'JOPxsy8WmrFEiTxR_b_w'


#===============================================================================
# tenants = 
# (
#    'tenant_1_name', 
#    'tenant_2_name', 
#    'tenant_3_name',
# ) 
#===============================================================================

tenants = ('t1', 't2') 


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
        # Global admin
        #-------------------------------------- 'ga': {'password':'Mirantis123',
        #----------------------------- 'roles':{'g':'admin','t1':None,'t2':None}
        #-------------------------------------------------------------------- },
        #------------------------------------------------------- # Global member
        #-------------------------------------- 'gm': {'password':'Mirantis123',
        #---------------------------- 'roles':{'g':'member','t1':None,'t2':None}
        #-------------------------------------------------------------------- },
        # Admin in t1 tenant
       't1a': {'password':'Mirantis123',
        'roles':{'g':None,'t1':'admin','t2':None}
        },
       # Member in t1 tenant
       't1m': {'password':'Mirantis123',
        'roles':{'g':None,'t1':'member','t2':None}
        },
       # Admin in t2 tenant (and has membership but has no roles in t1) 
       't2a': {'password':'Mirantis123',
        'roles':{'g':None,'t1':None,'t2':'admin'}
        },
       # Member in t2 tenant (and has membership but has no roles in t1) 
       't2m': {'password':'Mirantis123',
        'roles':{'g':None,'t1':None,'t2':'member'}
        },
        #-------------------------------- # Global admin and member in t1 tenant
        #----------------------------------- 'gat1m': {'password':'Mirantis123',
        #------------------------- 'roles':{'g':'admin','t1':'member','t2':None}
        #-------------------------------------------------------------------- },
        #-------------------------------- # Global member and admin in t1 tenant
        #----------------------------------- 'gmt1a': {'password':'Mirantis123',
        #------------------------- 'roles':{'g':'member','t1':'admin','t2':None}
        #-------------------------------------------------------------------- },
        # Admin in t1 tenant and member in t2 tenant
       't1at2m': {'password':'Mirantis123',
        'roles':{'g':None,'t1':'admin','t2':'member'}
        },
       # Member in t1 tenant and admin in t2 tenant
       't1mt2a': {'password':'Mirantis123',
        'roles':{'g':None,'t1':'member','t2':'admin'}
        },
       # fake
       'fake': {'password':'superuser',
        'roles':{'g':'admin','t1':'admin','t2':'member'}
        },
       }



