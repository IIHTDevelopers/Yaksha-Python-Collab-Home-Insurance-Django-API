from rest_framework.test import APITestCase
from insuranceapp.test.TestUtils import TestUtils
class HomeInsuranceAPIBoundaryTest(APITestCase):
    def test_boundary(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("User_TestBoundary",True,"boundary")
        print("User_TestBoundary = Passed")
