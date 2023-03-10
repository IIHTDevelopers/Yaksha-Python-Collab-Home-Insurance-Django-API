from rest_framework.test import APITestCase
from insuranceapp.models import *
from insuranceapp.test.TestUtils import TestUtils
class HomeInsuranceAPIFunctionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create(
        user_id= 2,
        first_name= "Venu",
        last_name= "Gopal",
        user_name="Venu Gopal"
        )

        QuoteModel.objects.create(
        user_id=2,
        quote_id=2,
        hno= "21-133",
        city= "Nijamaabad",
        state= "TS",
        country= "India",
        residance_type= "Individual",
        residance_use= "living",
        detached_structure= "structure2",
        market_value= "7000000.00",
        year_build= 2015,
        square_foot_value= 350,
        dwelling_style= "style2",
        roof_material= "material2",
        garage_type= "type1",
        numfullBaths= 1,
        numhalfBaths= 2
        )

        PolicyModel.objects.create(
        policy_key=1,
        quote_id=2,
        policy_term= "2 years",
        policy_effective_date= "2022-09-01",
        policy_end_date= "2035-01-01"
        )

    def test_register_user(self):
        url='http://127.0.0.1:8000/user/'
        data= {
        "user_id": 1,
        "first_name": "Shibu",
        "last_name": "Darshan",
        "user_name": "Shibu Darshan",
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("User_TestRegisterUser", True, "functional")
            print("User_TestRegisterUser = Passed")
        else:
            test_obj.yakshaAssert("User_TestRegisterUser", False, "functional")
            print("User_TestRegisterUser = Failed")


    def test_get_all_users(self):# new
        url='http://127.0.0.1:8000/user/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("User_TestGetAllUsers", True, "functional")
            print("User_TestGetAllUsers = Passed")
        else:
            test_obj.yakshaAssert("User_TestGetAllUsers", False, "functional")
            print("User_TestGetAllUsers = Failed")


    def test_get__user_by_id(self):# new
        url='http://127.0.0.1:8000/user/2/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("User_TestGetUserById", True, "functional")
            print("User_TestGetUserById = Passed")
        else:
            test_obj.yakshaAssert("User_TestGetUserById", False, "functional")
            print("User_TestGetUserById = Failed")


    def test_create_quote(self):
        url='http://127.0.0.1:8000/createquote/?user_id=2'
        data= {
        "quote_id": 2,
        "user_id": 2,
        "hno": "21-133",
        "city": "Nijamaabad",
        "state": "TS",
        "country": "India",
        "residance_type": "Individual",
        "residance_use": "living",
        "detached_structure": "structure2",
        "market_value": "7000000.00",
        "year_build": 2015,
        "square_foot_value": 350,
        "dwelling_style": "style2",
        "roof_material": "material2",
        "garage_type": "type1",
        "numfullBaths": 1,
        "numhalfBaths": 2
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("Quote_TestCreateQuote", True, "functional")
            print("Quote_TestCreateQuote = Passed")
        else:
            test_obj.yakshaAssert("Quote_TestCreateQuote", False, "functional")
            print("Quote_TestCreateQuote = Failed")

    def test_get_quote(self):
        url='http://127.0.0.1:8000/getquote/?quote_id=2&user_id=2'
        response=self.client.get(url)
        test_obj = TestUtils()
        #print(response.status_code)
        if response.status_code==200:
            test_obj.yakshaAssert("Quote_TestGetQuote", True, "functional")
            print("Quote_TestGetQuote = Passed")
        else:
            test_obj.yakshaAssert("Quote_TestGetQuote", False, "functional")
            print("Quote_TestGetQuote = Failed")


    def test_get_all_quotes(self):# new
        url='http://127.0.0.1:8000/getallquote/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Quote_TestGetAllQuotes", True, "functional")
            print("Quote_TestGetAllQuotes = Passed")
        else:
            test_obj.yakshaAssert("Quote_TestGetAllQuotes", False, "functional")
            print("Quote_TestGetAllQuotes = Failed")


    def test_buy_policy(self):
        url='http://127.0.0.1:8000/buypolicy/?quote_id=2'
        data= {
        "quote_id":2,
        "policy_term": "2 years",
        "policy_effective_date": "2022-09-01",
        "policy_end_date": "2035-01-01"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("Policy_TestBuyPolicy", True, "functional")
            print("Policy_TestBuyPolicy = Passed")
        else:
            test_obj.yakshaAssert("Policy_TestBuyPolicy", False, "functional")
            print("Policy_TestBuyPolicy = Failed")

    def test_show_policy(self):
        url='http://127.0.0.1:8000/showpolicy/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        #print(response.status_code)
        if response.status_code==200:
            test_obj.yakshaAssert("Policy_TestShowPolicy", True, "functional")
            print("Policy_TestShowPolicy = Passed")
        else:
            test_obj.yakshaAssert("Policy_TestShowPolicy", False, "functional")
            print("Policy_TestShowPolicy = Failed")

    def test_renew_policy(self):
        url='http://127.0.0.1:8000/renewpolicy/1/'
        data= {
        "status":"Renewed"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Policy_TestRenewPolicy", True, "functional")
            print("Policy_TestRenewPolicy = Passed")
        else:
            test_obj.yakshaAssert("Policy_TestRenewPolicy", False, "functional")
            print("Policy_TestRenewPolicy = Failed")

    def test_cancel_policy(self):
        url='http://127.0.0.1:8000/renewpolicy/1/'
        data= {
        "status":"Cancelled"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("Policy_TestCancelPolicy", True, "functional")
            print("Policy_TestCancelPolicy = Passed")
        else:
            test_obj.yakshaAssert("Policy_TestCancelPolicy", False, "functional")
            print("Policy_TestCancelPolicy = Failed")
