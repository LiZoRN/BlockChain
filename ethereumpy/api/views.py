from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import json
from .serializers import UserSerializer, GroupSerializer

from web3 import Web3, HTTPProvider
web3 = Web3(HTTPProvider('http://localhost:7545'))

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# web3.eth API
@api_view(['GET', 'POST'])
def getLatestBlock(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        return json.dumps(web3.eth.getBlock('latest'))