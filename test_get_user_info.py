'''
Created on 19.07.2012

@author: mrasskazov
'''
import unittest

from config import *
from get_user_info import *


class TestGetUserInfo(unittest.TestCase):
    

    def setUp(self):
        pass


    def tearDown(self):
        pass


for u in users:
    def auth_wo_spec_tenant(self, username = u, password = users[u]['password']):
        token = gettoken(username, password)
        self.assert_(token['access']['token']['id'])
    auth_wo_spec_tenant.__doc__ = "Authorization without specifying tenant for " + u
    auth_wo_spec_tenant.__name__ = "test_" + auth_wo_spec_tenant.__name__ + '_' + u
    #TestGetUserInfo.__dict__[auth_wo_spec_tenant.__name__] = auth_wo_spec_tenant
    setattr(TestGetUserInfo, auth_wo_spec_tenant.__name__, auth_wo_spec_tenant)
    #auth_wo_spec_tenant.__name__ = "dumb_" + auth_wo_spec_tenant.__name__ + '_' + u
    #delattr(self, auth_wo_spec_tenant.__name__)
print __name__



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()