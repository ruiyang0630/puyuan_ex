from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from other.models import Notification, Share

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
def news(request):
    try:
        user_notification = Notification.objects.filter(member_id=request.user)
        key = ['id', 'member_id', 'group', 'title', 'message', 'created_at', 'updated_at']
        parameters = ['id', 'member_id', None, None, 'message', 'created_at', 'updated_at']
        news = []
        for i in user_notification:
            news_info = {}
            for k, p in zip(key, parameters):
                if k == 'group':
                    news_info['group'] = 0
                elif k == 'title':
                    news_info['title'] = "0"
                else:
                    news_info[k] = getattr(i, p, None)
        return Response({
            'status': '0',
            'message': 'ok',
            'news': news
        }, status=200)
    except:
        return Response(response_error, status=404)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def share(request, data_type=None):
    if request.method == 'GET':
        try:
            records = []
            user_share = Share.objects.filter(data_type=data_type)
            for i in user_share:
                share_data = {
                    "id": i.id,
                    "user_id": request.user.id,
                    "sugar": 0.0,
                    "timeperiod": 0,
                    "weight": 0.0,
                    "body_fat": 0.0,
                    "bmi": 0.0,
                    "systolic": 0,
                    "diastolic": 0,
                    "pulse": 0,
                    "meal": 0,
                    "tag": [],
                    "image": [],
                    "location": {
                        "lat": "0",
                        "lng": "0"
                    },
                    "relation_type": i.relation_type,
                    "relation_id": 0,
                    "message": "0",
                    "type": i.data_type,
                    "url": "0",
                    "recorded_at": "2023-06-26 17:10:11",
                    "created_at": "2023-06-26 17:10:11",
                    "user": {
                        "id": request.user.id,
                        "name": '0',
                        "account": request.user.email
                    }
                }
                records.append(share_data)
            return Response({
                'status': '0',
                'message': 'ok',
                'records': records
            }, status=200)
        except:
            return Response(response_error, status=404)
        
    elif request.method == 'POST':
        try:
            data_type = request.data.get('type')
            fid = request.data.get('id')
            relation_type = request.data.get('relation_type')
            user_share = Share.objects.create(fid=fid, data_type=data_type, relation_type=relation_type)
            user_share.save()
            return Response(response_success, status=200)
        except:
            return Response(response_error, status=400)
    