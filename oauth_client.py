import requests

def get_access_token(client_id, client_secret):
    token_url = 'http://localhost:8000/o/token/'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        return access_token
    else:
        return None


# Sử dụng access token để gửi yêu cầu bảo vệ tới các API của bạn
access_token = get_access_token('upwerF0jrragaxxkNXHDMTGGe8ciMwJN6yVoIOAu', '3aa4PCcNRwyXzs86QP0PWnOnko0ZW6ym4WD0W539XjjOuPDggxO6r5bKSdOxW1HkLwBiwLEIxAf5SzmR2qTBoRo1a7dj2E4ur84zde9tbBO7ykGaoKrYgTG53ZsKWFUi')
if access_token:
    api_url = 'http://localhost:8000/api/check_oauth/'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(api_url, headers=headers)
    print(response.json())
else:
    print('Failed to get access token')
