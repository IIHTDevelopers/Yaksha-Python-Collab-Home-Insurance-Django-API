from rest_framework.test import APITestCase
from insuranceapp.models import *
from insuranceapp.test.TestUtils import TestUtils
class HomeInsuranceAPIExceptionalTest(APITestCase):
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

    def test_register_user_error(self):
        url='http://127.0.0.1:8000/user/'
        data= {
        "user_id": 1,
        "first_name": "Shibu",
        "last_name": "Darshan",
        #"user_name": "Shibu Darshan",
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        #print(response.status_code)
        if response.status_code==400:
            test_obj.yakshaAssert("User_TestRegisterUserError", True, "exceptional")
            print("User_TestRegisterUserError = Passed")
        else:
            test_obj.yakshaAssert("User_TestRegisterUserError", False, "exceptional")
            print("User_TestRegisterUserError = Failed")


    def test_get__user_by_id_error(self):# new
        url='http://127.0.0.1:8000/user/2/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("User_TestGetUserByIdError", True, "exceptional")
            print("User_TestGetUserByIdError = Passed")
        else:
            test_obj.yakshaAssert("User_TestGetUserByIdError", False, "exceptional")
            print("User_TestGetUserByIdError = Failed")

    def test_create_quote_error(self):
        url='http://127.0.0.1:8000/createquote/?user_id=22'
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
        if response.status_code==500:
            test_obj.yakshaAssert("Quote_TestCreateQuoteError", True, "exceptional")
            print("Quote_TestCreateQuoteError = Passed")
        else:
            test_obj.yakshaAssert("Quote_TestCreateQuoteError", False, "exceptional")
            print("Quote_TestCreateQuoteError = Failed")

    def test_get_quote_error(self):
        url='http://127.0.0.1:8000/getquote/?quote_id=22&user_id=22'
        response=self.client.get(url)
        test_obj = TestUtils()
        #print(response.status_code)
        if response.status_code==500:
            test_obj.yakshaAssert("Quote_TestGetQuoteError", True, "exceptional")
            print("Quote_TestGetQuoteError = Passed")
        else:
            test_obj.yakshaAssert("Quote_TestGetQuoteError", False, "exceptional")
            print("Quote_TestGetQuoteError = Failed")

    def test_buy_policy_error(self):
        url='http://127.0.0.1:8000/buypolicy/?quote_id=22'
        data= {
        "quote_id":2,
        "policy_term": "2 years",
        "policy_effective_date": "2022-09-01",
        "policy_end_date": "2035-01-01"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("Policy_TestBuyPolicyError", True, "exceptional")
            print("Policy_TestBuyPolicyError = Passed")
        else:
            test_obj.yakshaAssert("Policy_TestBuyPolicyError", False, "exceptional")
            print("Policy_TestBuyPolicyError = Failed")

    def test_show_policy_error(self):
        url='http://127.0.0.1:8000/showpolicy/11/'
        response=self.client.get(url)
        test_obj = TestUtils()
        #print(response.status_code)
        if response.status_code==500:
            test_obj.yakshaAssert("Policy_TestShowPolicyError", True, "exceptional")
            print("Policy_TestShowPolicyError = Passed")
        else:
            test_obj.yakshaAssert("Policy_TestShowPolicyError", False, "exceptional")
            print("Policy_TestShowPolicyError = Failed")

    def test_renew_policy_error(self):
        url='http://127.0.0.1:8000/renewpolicy/11/'
        data= {
        "status":"Renewed"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("Policy_TestRenewPolicyError", True, "exceptional")
            print("Policy_TestRenewPolicyError = Passed")
        else:
            test_obj.yakshaAssert("Policy_TestRenewPolicyError", False, "exceptional")
            print("Policy_TestRenewPolicyError = Failed")

    def test_cancel_policy_error(self):
        url='http://127.0.0.1:8000/renewpolicy/11/'
        data= {
        "status":"Cancelled"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("Policy_TestCancelPolicyError", True, "exceptional")
            print("Policy_TestCancelPolicyError = Passed")
        else:
            test_obj.yakshaAssert("Policy_TestCancelPolicyError", False, "exceptional")
            print("Policy_TestCancelPolicyError = Failed")
