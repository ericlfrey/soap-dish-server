from soapdishapi.models import Soaper
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Soaper

    Method arguments:
      request -- The full HTTP request object
    '''
    # uid = request.data['uid']
    uid = request.META['HTTP_AUTHORIZATION']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    soaper = Soaper.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if soaper is not None:
        data = {
            'id': soaper.id,
            'uid': soaper.uid,
            'first_name': soaper.first_name,
            'last_name': soaper.last_name
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new soaper for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    uid = request.META['HTTP_AUTHORIZATION']
    soaper = Soaper.objects.create(
        # uid=request.data['uid'],
        uid=uid,
        first_name=request.data['firstName'],
        last_name=request.data['lastName']
    )

    # Return the soaper info to the client
    data = {
        'id': soaper.id,
        'uid': soaper.uid,
        'first_name': soaper.first_name,
        'last_name': soaper.last_name
    }
    return Response(data)
