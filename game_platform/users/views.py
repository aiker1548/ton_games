# В файле views.py вашего приложения
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from users.models import CustomUser  # Предполагается, что модель CustomUser находится в users/models.py

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        wallet_adress = data.get('wallet_adress')

        # Проверка наличия обязательных полей
        if not username or not password:
            return JsonResponse({'error': 'Требуется указать имя пользователя и пароль.'}, status=400)

        # Проверка наличия пользователя с таким же именем
        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Пользователь с таким именем уже существует.'}, status=400)

        # Создание пользователя
        user = CustomUser.objects.create_user(username=username, email=email, password=password, wallet_adress=wallet_adress)
        return JsonResponse({'success': 'Пользователь успешно зарегистрирован.'}, status=201)

    return JsonResponse({'error': 'Разрешены только запросы методом POST.'}, status=405)
