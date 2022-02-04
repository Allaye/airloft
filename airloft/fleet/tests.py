from re import A
from rest_framework.test import APITestCase
from rest_framework import status
from fleet.models import Aircraft, Airport, Flight
from django.urls import reverse


class TestFleetHelper(APITestCase):
    """a class that contains helper method to be used by other classes"""

    def authenticate_admin(self):
        """
        a function to create a new user and authenticate it.
        
        """
        account_creation_data = {
            'username': 'admin',
            'password': 'admin',
            'email': 'admin@user.com',
            'is_staff': 1
        }
        login_data = {
            'email': 'admin@user.com',
            'password': 'admin'
        }
        self.client.post(reverse("register"), account_creation_data, format='json')
        response = self.client.post(reverse("login"), login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")
    

    def authenticate_user(self):
        """
        a function to create a new user and authenticate it.
        
        """
        account_creation_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@user.com',
            'is_staff': 0
        }
        login_data = {
            'email': 'test@user.com',
            'password': 'testpassword'
        }
        self.client.post(reverse("register"), account_creation_data, format='json')
        response = self.client.post(reverse("login"), login_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")

    def create_aircraft(self, single=True):
        """
        method to create an aircraft
        """
        if single:
            request_data = {
                'name': 'Test Plane',
                'manufacturer': 'UAC',
                'model': 'A320',
            }
            project_response = self.client.post(reverse('add_project'), request_data, format='json')
            return project_response
        request_data = {
                'id': '1',
                "name": "Test Plane",
                'manufacturer': 'UAC',
                'serial_number': 'cba54b0f-2c82-47f9-a49d-9b4b30bdb55',
                'model': "A320"
            }
        aircraft_response = self.client.post(reverse('add_aircraft'), request_data, format='json')
        return aircraft_response

    def create_airport(self, member=True):
        """method to create airport object"""
        request_data = {
            'location': 'Uk',
            'name': "Airkiip Airport",
            'code': 'TPAk'
        }
        airport_response = self.client.post(reverse('add_airport'), request_data, format='json')
        return airport_response

# Create your tests here.
class TestAircraftUserCase(TestFleetHelper):
    """
    test case to test the Aircraft creation endpoints

    """
    def test_should_not_create_aircraft_with_normal_user(self):
        """
        test case to test if the aircraft creation endpoint will fail
        if the user is not an admin.
        """
        self.authenticate_user()
        aircraft = self.create_aircraft()
        self.assertEqual(aircraft.status_code, status.HTTP_403_FORBIDDEN)

    
    def test_should_create_aircraft_with_auth(self):
        """
        test case to test if the aircraft creation endpoint will succeed
        if the user is logged in.
        """
        previous_aircraft_count = Aircraft.objects.all().count()
        self.authenticate_admin()
        response = self.create_aircraft()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(Aircraft.objects.all().count(), previous_aircraft_count)
        self.assertEqual(response.data['serial_number'], 'cba54b0f-2c82-47f9-a49d-9b4b30bdb55')
        self.assertEqual(response.data['manufacturer'], 'UAC')
        

    def test_retrives_all_aircraft_with_auth(self):
        """
        test case to test if the aircraft retrival endpoint will succeed
        if the user is logged in.
        """
        self.authenticate_admin()
        response = self.client.get(reverse('list_aircraft'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertIsInstance(response.data['result'], list)
        response = self.create_aircraft()
        response = self.client.get(reverse('aircraft_list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
       

    def test_retrive_one_aircraft_with_auth(self):
        """
        with authendication, check if we can get a created aircraft from the db
        """
        self.authenticate_admin()
        response = self.create_aircraft()
        response = self.client.get(reverse('list_a_project', kwargs={'id': response.data['id']}), format='json')
        response.data = dict(response.data[0])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = Aircraft.objects.get(id=response.data['id'])
        self.assertEqual(response.data['serial_number'], 'cba54b0f-2c82-47f9-a49d-9b4b30bdb55')
        self.assertEqual(response.data['manufacturer'], 'UAC')


    