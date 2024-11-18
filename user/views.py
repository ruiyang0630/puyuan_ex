import random
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from user.models import UserProfile, Default, Setting, BloodPressure, Weight, BloodSugar, DiaryDiet, HbA1c, MedicalInfo, DrugInfo, UserCare
from user.process import timeformat, strboolToint, delete_data

response_success = {
    'status': '0',
    'message': '成功'
}
response_error = {
    'status': '1',
    'message': '失敗'
}

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def user(request):
    if request.method == 'GET':
        try:
            user_profile, _ = UserProfile.objects.get_or_create(id=request.user)
            user_setting, _ = Setting.objects.get_or_create(id=request.user)
            user_default, _ = Default.objects.get_or_create(id=request.user)
            if user_profile.inviteCode == 'null':
                user_profile.inviteCode = f'{random.randint(0, 999999):06d}'
                user_profile.save()
            return Response({
                'status': '0',
                'user': {
                    'id': request.user.id,
                    'fcm_id': 'null',
                    'name': user_profile.name,
                    'account': request.user.email,
                    'status': 'VIP',
                    'fb_id': 'null',
                    'birthday': user_profile.birthday,
                    'height': user_profile.height,
                    'gender': strboolToint(user_profile.gender),
                    'address': user_profile.address,
                    'weight': user_profile.weight,
                    'phone': request.user.phone,
                    'email': request.user.email,
                    'inviteCode': user_profile.inviteCode,
                    'unread_records': [
                        0,
                        0,
                        0
                    ],
                    'verified': strboolToint(request.user.verified),
                    'privacy_policy': strboolToint(request.user.privacy_policy),
                    'must_change_password': strboolToint(request.user.must_change_password),
                    'login_times': 1,
                    'created_at': timeformat(user_profile.created_at),
                    'updated_at': timeformat(user_profile.updated_at),
                    'setting': {
                        'id': user_setting.id_id,
                        'user_id': user_setting.id_id,
                        'after_recording': strboolToint(user_setting.after_recording),
                        'no_recording_for_a_day': strboolToint(user_setting.no_recording_for_a_day),
                        'over_max_or_under_min': strboolToint(user_setting.over_max_or_under_min),
                        'after_meal': strboolToint(user_setting.after_meal),
                        'unit_of_sugar': strboolToint(user_setting.unit_of_sugar),
                        'unit_of_weight': strboolToint(user_setting.unit_of_weight),
                        'unit_of_height': strboolToint(user_setting.unit_of_height),
                        'created_at': timeformat(user_setting.created_at),
                        'updated_at': timeformat(user_setting.updated_at)
                    },
                    "vip": {
                    "id": request.user.id,
                    "user_id": request.user.id,
                    "level": 0,
                    "remark": 0.0,
                    "started_at": "",
                    "ended_at": "",
                    "created_at": "",
                    "updated_at": ""
                    },
                    'group': 'null',
                    'default': {
                        'id': user_default.id_id,
                        'user_id': request.user.id,
                        'sugar_morning_max': user_default.sugar_morning_max,
                        'sugar_morning_min': user_default.sugar_morning_min,
                        'sugar_evening_max': user_default.sugar_evening_max,
                        'sugar_evening_min': user_default.sugar_evening_min,
                        'sugar_before_max': user_default.sugar_before_max,
                        'sugar_before_min': user_default.sugar_before_min,
                        'sugar_after_max': user_default.sugar_after_max,
                        'sugar_after_min': user_default.sugar_after_min,
                        'systolic_max': user_default.systolic_max,
                        'systolic_min': user_default.systolic_min,
                        'diastolic_max': user_default.diastolic_max,
                        'diastolic_min': user_default.diastolic_min,
                        'pulse_max': user_default.pulse_max,
                        'pulse_min': user_default.pulse_min,
                        'weight_max': user_default.weight_max,
                        'weight_min': user_default.weight_min,
                        'bmi_max': user_default.bmi_max,
                        'bmi_min': user_default.bmi_min,
                        'body_fat_max': user_default.body_fat_max,
                        'body_fat_min': user_default.body_fat_min,
                        'created_at': timeformat(user_default.created_at),
                        'updated_at': timeformat(user_default.updated_at)
                    }
                },
                'message': 'ok'
            }, status=200)
        except:
            return Response(response_error, status=404)
        
    elif request.method == 'PATCH':
        parameters = ['name', 'birthday', 'gender', 'address', 'weight', 'height']
        email = request.data.get('email')
        phone = request.data.get('phone')
        data = {i: request.data.get(i) for i in parameters}
        user_profile = UserProfile.objects.get(id=request.user)
        user_auth = user_profile.id
        try:
            if email and phone:
                user_auth.email = email
                user_auth.username = email
                user_auth.phone = phone
            for key, value in data.items():
                if value != '':
                    setattr(user_profile, key, value)
            user_auth.save()
            user_profile.save()
            return Response(response_success, status=200)
        except:
            return Response(response_error, status=400)
    
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def default(request):
    parameters = ['sugar_morning_max', 'sugar_morning_min', 'sugar_evening_max', 'sugar_evening_min', 'sugar_before_max', 'sugar_before_min', 'sugar_after_max', 'sugar_after_min', 'systolic_max', 'systolic_min', 'diastolic_max', 'diastolic_min', 'pulse_max', 'pulse_min', 'weight_max', 'weight_min', 'bmi_max', 'bmi_min', 'body_fat_max', 'body_fat_min']
    data = {i: request.data.get(i) for i in parameters}
    user_default = Default.objects.get(id=request.user)
    try:
        for key, value in data.items():
            setattr(user_default, key, value)
        user_default.save()
        return Response(response_success, status=200)
    except:
        return Response(response_error, status=400)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def setting(request):
    parameters = ['after_recording', 'no_recording_for_a_day', 'over_max_or_under_min', 'after_meal', 'unit_of_sugar', 'unit_of_weight', 'unit_of_height']
    data = {i: request.data.get(i) for i in parameters}
    user_setting, _ = Setting.objects.get_or_create(id=request.user)
    try:
        for key, value in data.items():
            setattr(user_setting, key, value)
        user_setting.save()
        return Response(response_success, status=200)
    except:
        return Response(response_error, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def badge(request):
    badge = request.data.get('badge')
    user_profile, _ = UserProfile.objects.get_or_create(id=request.user)
    try:
        user_profile.badge = badge
        user_profile.save()
        return Response(response_success, status=200)
    except:
        return Response(response_error, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def blood_pressure(request):
    parameters = ['systolic', 'diastolic', 'pulse', 'recorded_at']
    data = {i: request.data.get(i) for i in parameters}
    user_blood_pressure = BloodPressure.objects.create(user_id=request.user)
    try:
        for key, value in data.items():
            setattr(user_blood_pressure, key, value)
        user_blood_pressure.save()
        return Response(response_success, status=200)
    except:
        return Response(response_error, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def weight(request):
    parameters = ['weight', 'body_fat', 'bmi', 'recorded_at']
    data = {i: request.data.get(i) for i in parameters}
    user_weight = Weight.objects.create(user_id=request.user)
    try:
        for key, value in data.items():
            setattr(user_weight, key, value)
        user_weight.save()
        return Response(response_success, status=200)
    except:
        return Response(response_error, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def blood_sugar(request):
    parameters = ['sugar', 'timeperiod', 'recorded_at']
    data = {i: request.data.get(i) for i in parameters}
    user_blood_sugar = BloodSugar.objects.create(user_id=request.user)
    try:
        for key, value in data.items():
            setattr(user_blood_sugar, key, value)
        user_blood_sugar.save()
        return Response(response_success, status=200)
    except:
        return Response(response_error, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def diet(request):
    parameters = ['description', 'meal', 'tag[]', 'image', 'lat', 'lng', 'recorded_at']
    data = {i: request.data.get(i) for i in parameters}
    user_diary_diet = DiaryDiet.objects.create(user_id=request.user)
    try:
        for key, value in data.items():
                if key == 'tag[]' and value:
                    user_diary_diet.tag = ','.join(data['tag[]'])
                else:
                    setattr(user_diary_diet, key, value)
        user_diary_diet.save()
        return Response({
            'status': '0',
            'message': 'ok',
            'image_url': ''
        }, status=200)
    except:
        return Response(response_error, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def last_upload(request):
    try:
        user_blood_pressure = BloodPressure.objects.filter(user_id=request.user).latest('recorded_at')
        user_weight = Weight.objects.filter(user_id=request.user).latest('recorded_at')
        user_blood_sugar = BloodSugar.objects.filter(user_id=request.user).latest('recorded_at')
        user_diary_diet = DiaryDiet.objects.filter(user_id=request.user).latest('recorded_at')
        return Response({
            'status': '0',
            'last_upload': {
            'blood_pressure': timeformat(user_blood_pressure.recorded_at),
            'weight': timeformat(user_weight.recorded_at),
            'blood_sugar': timeformat(user_blood_sugar.recorded_at),
            'diet': timeformat(user_diary_diet.recorded_at)
            }
        }, status=200)
    except:
        return Response(response_error, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def diary(request):
    try:
        date = request.query_params.get('date')
        user_diary_diet = DiaryDiet.objects.filter(user_id=request.user, recorded_at__icontains=date)
        user_blood_pressure = BloodPressure.objects.filter(user_id=request.user, recorded_at__icontains=date)
        user_weight = Weight.objects.filter(user_id=request.user, recorded_at__icontains=date)
        user_blood_sugar = BloodSugar.objects.filter(user_id=request.user, recorded_at__icontains=date)
        base = {
            "id": 0,
            "user_id": 0,
            "systolic": 0,
            "diastolic": 0,
            "pulse": 0,
            "weight": 0.0,
            "body_fat": 0.0,
            "bmi": 0.0,
            "sugar": 0.0,
            "exercise": 0,
            "drug": 0,
            "timeperiod": 0,
            "description": "",
            "meal": 0,
            "tag": [
                {
                    "name": [],
                    "message": "ok"
                }
            ],
            "image": [],
            "location": {
                "lat": "",
                "lng": ""
            },
            "reply": "",
            "recorded_at": "",
            "type": ""
        }
        diary_data = []
        if user_diary_diet.exists():
            for i in user_diary_diet:
                data = base.copy()
                data['id'] = i.id
                data['user_id'] = i.user_id_id
                data['description'] = str(i.description)
                data['meal'] = i.meal
                data['tag'][0]['name'] = i.tag.split(',')
                data['image'] = [str(i.image)]
                data['location']['lat'] = str(i.lat)
                data['location']['lng'] = str(i.lng)
                data['recorded_at'] = timeformat(i.recorded_at)
                data['type'] = 'diet'
                diary_data.append(data)
        if user_blood_pressure.exists():
            for i in user_blood_pressure:
                data = base.copy()
                data['id'] = i.id
                data['user_id'] = i.user_id_id
                data['systolic'] = i.systolic
                data['diastolic'] = i.diastolic
                data['pulse'] = i.pulse
                data['recorded_at'] = timeformat(i.recorded_at)
                data['type'] = 'blood_pressure'
                diary_data.append(data)
        if user_weight.exists():
            for i in user_weight:
                data = base.copy()
                data['id'] = i.id
                data['user_id'] = i.user_id_id
                data['weight'] = i.weight
                data['body_fat'] = i.body_fat
                data['bmi'] = i.bmi
                data['recorded_at'] = timeformat(i.recorded_at)
                data['type'] = 'weight'
                diary_data.append(data)
        if user_blood_sugar.exists():
            for i in user_blood_sugar:
                data = base.copy()
                data['id'] = i.id
                data['user_id'] = i.user_id_id
                data['sugar'] = i.sugar
                data['timeperiod'] = i.timeperiod
                data['recorded_at'] = timeformat(i.recorded_at)
                data['type'] = 'blood_sugar'
                diary_data.append(data)
        return Response({
            'status': '0',
            'message': 'ok',
            'diary': diary_data
        }, status=200)
    except:
        return Response(response_error, status=404)

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def records(request):
    if request.method == 'POST':
        try:
            user_blood_pressure = BloodPressure.objects.filter(user_id=request.user).last()
            user_blood_sugar = BloodSugar.objects.filter(user_id=request.user).last()
            user_weight = Weight.objects.filter(user_id=request.user).last()
            if user_blood_pressure is None:
                blood_pressures_data = {
                    'systolic': 0,
                    'diastolic': 0,
                    'pulse': 0
                }
            else:
                blood_pressures_data = {
                    'systolic': user_blood_pressure.systolic,
                    'diastolic': user_blood_pressure.diastolic,
                    'pulse': user_blood_pressure.pulse
                }
            if user_blood_sugar is None:
                user_blood_sugar_data = {
                    'sugar': 0
                }
            else:
                user_blood_sugar_data = {
                    'sugar': user_blood_sugar.sugar
                }
            if user_weight is None:
                user_weight_data = {
                    'weight': 0
                }
            else:
                user_weight_data = {
                    'weight': user_weight.weight
                }
            return Response({
                'status': '0',
                'message': 'ok',
                'blood_pressures': blood_pressures_data,
                'blood_sugars': user_blood_sugar_data,
                'weights': user_weight_data
            }, status=200)
        except:
            return Response(response_error, status=400)
        
    elif request.method == 'DELETE':
        try:  
            deleteObject = request.data.get('deleteObject')
            if deleteObject.get('blood_pressures') != None:
                delete_data(request, BloodPressure, deleteObject.get('blood_pressures'))
            if deleteObject.get('blood_sugars') != None:
                delete_data(request, BloodSugar, deleteObject.get('blood_sugars'))
            if deleteObject.get('weights') != None:
                delete_data(request, Weight, deleteObject.get('weights'))
            if deleteObject.get('diets') != None:
                delete_data(request, DiaryDiet, deleteObject.get('diets'))
            return Response(response_success, status=200)
        except:
            return Response(response_error, status=400)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def a1c(request):
    if request.method == 'GET':
        try:
            user_a1c = HbA1c.objects.filter(user_id=request.user)
            a1cs = []
            for i in user_a1c:
                a1cs.append({
                    'id': i.id,
                    'a1c': str(i.a1c),
                    'recorded_at': timeformat(i.recorded_at),
                    'updated_at': timeformat(i.updated_at),
                    'created_at': timeformat(i.created_at),
                    'user_id': i.user_id_id
                })
            return Response({
                'status': '0',
                'message': 'ok',
                'a1cs': a1cs
            }, status=200)
        except:
            return Response(response_error, status=404)

    elif request.method == 'POST':
        try:
            a1c = request.data.get('a1c')
            recorded_at = request.data.get('recorded_at')
            HbA1c.objects.create(user_id=request.user, a1c = a1c, recorded_at = recorded_at)
            return Response(response_success, status=200)
        except:
            return Response(response_error, status=400)
        
    elif request.method == 'DELETE':
        try:
            delete_data(request, HbA1c, request.data.get('ids[]'))
            return Response({
                "status": "0",
                "message": "ok",
            }, status=200)
        except:
            return Response(response_error, status=400)
        
@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def medical(request):
    if request.method == 'GET':
        try:
            user_medical, _ = MedicalInfo.objects.get_or_create(id=request.user)
            return Response({
                'status': '0',
                'medical_info': {
                    'id': user_medical.id_id,
                    'user_id': user_medical.id_id,
                    'oad': strboolToint(user_medical.oad),
                    'insulin': strboolToint(user_medical.insulin),
                    'anti_hypertensives': strboolToint(user_medical.anti_hypertensives),
                    'diabetes_type': user_medical.diabetes_type,
                    'updated_at': timeformat(user_medical.updated_at),
                    'created_at': timeformat(user_medical.created_at)
                },
                'message': 'ok'
            }, status=200)
        except:
            return Response(response_error, status=404)
        
    elif request.method == 'PATCH':
        try:
            parameters = ['oad', 'insulin', 'anti_hypertensives', 'diabetes_type']
            data = {i: request.data.get(i) for i in parameters}
            user_medical, _ = MedicalInfo.objects.get_or_create(id=request.user)
            for key, value in data.items():
                setattr(user_medical, key, value)
            user_medical.save()
            return Response(response_success, status=200)
        except:
            return Response(response_error, status=400)
        
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def drug_used(request):
    if request.method == 'GET':
        try:
            user_drug = DrugInfo.objects.filter(user_id=request.user)
            drug_useds = []
            for i in user_drug:
                drug_useds.append({
                    'id': i.id,
                    'name': i.drugname,
                    'type': strboolToint(i.drug_type),
                    'recorded_at': timeformat(i.recorded_at),
                    'updated_at': timeformat(i.updated_at),
                    'created_at': timeformat(i.created_at),
                    'user_id': i.user_id_id
                })
            return Response({
                'status': '0',
                'message': 'ok',
                'drug_useds': drug_useds
            }, status=200)
        except:
            return Response(response_error, status=404)
    
    elif request.method == 'POST':
        try:
            drug_type = request.data.get('type')
            drugname = request.data.get('name')
            recorded_at = request.data.get('recorded_at')
            DrugInfo.objects.create(user_id=request.user, drug_type=drug_type, drugname=drugname, recorded_at=recorded_at)
            return Response(response_success, status=200)
        except:
            return Response(response_error, status=400)
    
    elif request.method == 'DELETE':
        try:
            delete_data(request, DrugInfo, request.data.get('ids[]'))
            return Response({
                "status": "0",
                "message": "ok",
            }, status=200)
        except:
            return Response(response_error, status=400)
        
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def care(request):
    if request.method == 'GET':
        try:
            user_care = UserCare.objects.filter(user_id=request.user)
            cares = []
            for i in user_care:
                cares.append({
                    'id': i.id,
                    'user_id': i.user_id_id,
                    'member_id': i.member_id,
                    'reply_id': i.reply_id,
                    'message': i.message,
                    'created_at': timeformat(i.created_at),
                    'updated_at': timeformat(i.updated_at)
                })
            return Response({
                'status': '0',
                'message': 'ok',
                'cares': cares
            }, status=200)
        except:
            return Response(response_error, status=404)
    
    elif request.method == 'POST':
        try:
            message = request.data.get('message')
            UserCare.objects.create(user_id=request.user, message=message)
            return Response(response_success, status=200)
        except:
            return Response(response_error, status=400)