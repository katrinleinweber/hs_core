__author__ = 'shaunjl'
"""
Tastypie REST API tests for GetCapabilities.as_view() modeled after: https://github.com/hydroshare/hs_core/blob/master/tests/api/http/test_resource.py

note- only GET is currently implemented
test_othertypes must be added to in release 3

"""
from django.contrib.auth.models import User
from hs_core import hydroshare
from tastypie.test import ResourceTestCase, TestApiClient
from hs_core.models import GenericResource
from hs_core.hydroshare.resource import create_resource, get_capabilities


class GetCapabilities(ResourceTestCase):
    def setUp(self):
        self.api_client=TestApiClient()
        self.user = hydroshare.create_account(
            'shaun@gmail.com',
            username='user',
            first_name='User_FirstName',
            last_name='User_LastName',
            )
        self.url = '/hsapi/capabilities/'
        
    def tearDown(self):
        User.objects.all().delete()

    def test_generic(self):
        res = create_resource('GenericResource',self.user,'res1')
        resp = self.api_client.post(self.url, pk=res.short_id)

        self.assertValidJSONResponse(resp)

        capabilities=self.deserialize(resp)

        self.assertEqual(capabilities, None)
                
        
    def test_other_types(self):
        pass
        
    
