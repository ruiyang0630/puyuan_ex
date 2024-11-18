from django.utils import timezone
from rest_framework.response import Response

def timeformat(data):
    return timezone.localtime(data).strftime('%Y-%m-%d %H:%M:%S')

def strboolToint(data):
    return int(bool(data))

def delete_data(request, model, ids):
    for i in ids:
        data = model.objects.get(id=i)
        if data.user_id == request.user:
            data.delete()
    return 0

def database_check(request, data, model): #修正
    try:
        user_models = model.objects.filter(user_id=request.user)
        update = False
        for i in user_models:
            if data['recorded_at'] == timeformat(i.recorded_at):
                user_models = i
                update = True
                break
        if not update:
            user_models = model.objects.create(user_id=request.user)
    except:
        user_models = model.objects.create(user_id=request.user)
    return user_models

