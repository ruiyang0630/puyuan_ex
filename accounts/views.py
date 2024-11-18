import random
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import authenticate, get_user_model
from .process import Register, send_email


User = get_user_model()
response_error = {
    'status': '1',
    'message': '失敗'
}

@api_view(['POST'])
def register(request):
    write_data = Register(data=request.data)
    if write_data.is_valid():
        write_data.save()
        return Response({
            'status': '0',
            'message': '成功'
        }, status=201)
    return Response(response_error, status=400)

@api_view(['POST'])
def auth(request):
    username = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token = AccessToken.for_user(user)
        return Response({
            'status': '0',
            'token': str(token)
        }, status=200)
    else:
        return Response(response_error, status=400)
    
@api_view(['POST'])
def send(request):
    email = request.data.get('email')
    if email:
        try:
            user = User.objects.get(email=email)
            verification_code = f'{random.randint(0, 999999):06d}'
            user.code = verification_code
            user.save()
            send_email(email, verification_code, 'code')
            return Response({
                'status': '0',
                'code': verification_code,
                'message': '成功'
            }, status=200)
        except User.DoesNotExist:
            return Response(response_error, status=404)
        except:
            return Response(response_error, status=500)
    else:
        return Response(response_error, status=400)
    
@api_view(['POST'])
def verification_check(request):
    email = request.data.get('email')
    code = request.data.get('code')
    if email and code:
        try:
            user = User.objects.get(email=email, code=code)
            user.verified = True
            user.save()
            return Response({
                'status': '0',
                'message': '成功'
            }, status=200)
        except User.DoesNotExist:
            return Response(response_error, status=404)
        except:
            return Response(response_error, status=500)
    else:
        return Response(response_error, status=400)
    
@api_view(['POST'])
def forgot(request):
    email = request.data.get('email')
    if email:
        try:
            user = User.objects.get(email=email)
            temporary_password = f'{random.randint(0, 999999):06d}'
            user.set_password(temporary_password)
            user.must_change_password = True
            user.save()
            send_email(email, temporary_password, 'forget')
            return Response({
                'status': '0',
                'message': '成功'
            }, status=200)
        except User.DoesNotExist:
            return Response(response_error, status=404)
        except:
            return Response(response_error, status=500)
    else:
        return Response(response_error, status=400)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reset(request):
    try:
        user = request.user
        password = request.data.get('password')
        user.set_password(password)
        user.must_change_password = False
        user.save()
        return Response({
            'status': '0',
            'message': '成功'
        }, status=200)
    except:
        return Response(response_error, status=400)
    
@api_view(['GET'])
def register_check(request):
    try:
        email = request.query_params.get('email')
        User.objects.get(email=email)
        return Response(response_error, status=400)
    except User.DoesNotExist:
        return Response({
            'status': '0',
            'message': '成功'
        }, status=200)
    except:
        return Response(response_error, status=400)