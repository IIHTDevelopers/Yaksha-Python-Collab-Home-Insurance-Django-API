
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from insuranceapp.serializers import UserSerializer,QuoteSerializer,PolicySerializer
from insuranceapp.models import UserModel,QuoteModel,PolicyModel
from insuranceapp.exceptions import PolicyKeyDoesNotExist,IdDoesNotExist,UserDoesNotExist,QuoteIdDoesNotExist
from insuranceapp.service  import PolicyService

#User
class UserView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def post(self, request,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
#Quote
class QuoteView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def post(self, request,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

#Quote
class GetAllQuoteView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

#Policy        
class BuyPolicyView(APIView):
    def post(self, request,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
#Policy
class ShowPolicyView(APIView):
    def get(self,request,pk=None,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
#Policy
class RenewPolicyView(APIView):
    def patch(self,request,pk,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
#Policy
class CancelPolicyView(APIView):
    def patch(self,request,pk,format=None):
        #Write your logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
