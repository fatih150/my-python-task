from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import pandas as pd
import requests
from io import StringIO
from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

@csrf_exempt
def upload_csv(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file and file.name.endswith('.csv'):
            csv_content = file.read().decode('utf-8')
            df = pd.read_csv(StringIO(csv_content), delimiter=';')

            try:
                token = get_access_token()
                resources = fetch_resources(token)
                resources_df = pd.DataFrame(resources)
                combined_df = pd.concat([resources_df, df], ignore_index=True).drop_duplicates()
                combined_df = combined_df[combined_df['hu'].notna()]

                result = combined_df.to_dict(orient='records')
                return JsonResponse(result, safe=False)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)

        return JsonResponse({'error': 'Invalid file type'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_access_token():
    url = "https://api.baubuddy.de/index.php/login"
    payload = {
        "username": "365",
        "password": "1"
    }
    headers = {
        "Authorization": "Basic QVBJX0V4cGxvcmVyOjEyMzQ1NmlzQUxhbWVQYXNz",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()
    return response_data.get('oauth', {}).get('access_token')

def fetch_resources(token):
    api_url = "https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    return response.json()
