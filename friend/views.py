from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from friend.models import Friend
from user.models import UserProfile
from user.process import timeformat, strboolToint

response_success = {
    'status': '0',
    'message': '成功'
}
response_error = {
    'status': '1',
    'message': '失敗'
}

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def code(request):
    try:
        user_profile = UserProfile.objects.get(id=request.user)
        return Response({
            'status': '0',
            'message': 'ok',
            'invite_code': user_profile.inviteCode
        }, status=200)
    except:
        return Response(response_error, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list(request):
    try:
        user_friend_1 = Friend.objects.filter(relationid=request.user.id)
        user_friend_2 = Friend.objects.filter(userid=request.user)
        friends = []
        for i in user_friend_1:
            if i.status == 1:
                friends.append({
                    "id": i.userid_id,
                    "name": UserProfile.objects.get(id=i.userid_id).name,
                    "relation_type": i.friend_type
                })
        for i in user_friend_2:
            if i.status == 1:
                friends.append({
                    "id": i.relationid,
                    "name": UserProfile.objects.get(id=i.relationid).name,
                    "relation_type": i.friend_type
                })
        return Response({
            'status': '0',
            'message': 'ok',
            'friends': friends
        }, status=200)
    except:
        return Response(response_error, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def requests(request):
    try:
        user_friend = Friend.objects.filter(relationid=request.user.id)
        requests_data = []
        for i in user_friend:
            if i.status == 0:
                requests_data.append({
                    "id": i.id,
                    "user_id": i.userid_id,
                    "relation_id": i.relationid,
                    "type": i.friend_type,
                    "read": strboolToint(i.read),
                    "status": i.status,
                    "created_at": timeformat(i.created_at),
                    "updated_at": timeformat(i.updated_at),
                    "user": {
                        "id": i.userid_id,
                        "name": UserProfile.objects.get(id=i.userid_id).name,
                        "account": i.userid.email
                    }
                })
        return Response({
            'status': '0',
            'message': 'ok',
            'requests': requests_data
        }, status=200)
    except:
        return Response(response_error, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send(request):
    try:
        invite_code = request.data.get('invite_code')
        friend_type = request.data.get('type')
        user_profile = UserProfile.objects.get(inviteCode=invite_code)
        user_friend, _ = Friend.objects.get_or_create(userid=request.user, relationid=user_profile.id_id, friend_type=friend_type)
        user_friend.save()
        return Response(response_success, status=200)
    except:
        return Response(response_error, status=400)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def accept(request, friend_invite_id):
    try:
        user_friend = Friend.objects.get(id=friend_invite_id)
        user_friend.status = 1
        user_friend.save()
        return Response(response_success, status=200)
    except:
        return Response(response_error, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def refuse(request, friend_invite_id):
    try:
        user_friend = Friend.objects.get(id=friend_invite_id)
        user_friend.status = 2
        user_friend.save()
        return Response(response_success, status=200)
    except:
        return Response(response_error, status=404)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove(request):
    try:
        ids = request.data.get('ids[]')
        if Friend.objects.filter(userid_id = request.user, relationid = ids).exists():
            data = Friend.objects.get(userid_id = request.user, relationid = ids)
        elif Friend.objects.filter(relationid = request.user.id, userid = ids).exists():
            data = Friend.objects.get(relationid = request.user.id, userid = ids)
        data.delete()
        return Response({
            'status': '0',
            'message': 'ok'
        }, status=200)
    except:
        return Response(response_error, status=400)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def results(request):
    try:
        user_friend = Friend.objects.filter(userid=request.user)
        results_data = []
        for i in user_friend:
            if (i.status == 1 or i.status == 2) and i.read == False:
                i.read = True
                i.save()
                results_data.append({
                    "id": i.id,
                    "user_id": i.userid_id,
                    "relation_id": i.relationid,
                    "type": i.friend_type,
                    "status": i.status,
                    "read": strboolToint(i.read),
                    "created_at": timeformat(i.created_at),
                    "updated_at": timeformat(i.updated_at),
                    "relation": {
                        "id": i.relationid,
                        "name": UserProfile.objects.get(id=i.relationid).name,
                        "account": UserProfile.objects.get(id=i.relationid).id.email
                    }
                })
        return Response({
            'status': '0',
            'message': 'ok',
            'results': results_data
            }, status=200)
    except:
        return Response(response_error, status=404)