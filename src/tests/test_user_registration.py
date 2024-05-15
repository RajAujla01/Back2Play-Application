from django.test import TestCase
from account.models import Account

class Test_User_Registration(TestCase):
    def setUp(self):
        Account.objects.create(email="lion@hotmail.com", username="roar", password="1s3d4g5h76/.RD45")

    def test_acwr_calculator_works(self):
        #get created account 
        name_test = Account.objects.get(username="roar")
        email_address_test = Account.objects.get(email="lion@hotmail.com")
        password_test = Account.objects.get(password="1s3d4g5h76/.RD45")
        
        #check value of fields is correct 
        self.assertEqual(name_test.email, 'lion@hotmail.com')
        self.assertEqual(email_address_test.username, "roar")
        self.assertEqual(password_test.password, '1s3d4g5h76/.RD45')

