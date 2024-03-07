# grpc_django

1. Clone the code and run the application
```
git clone https://github.com/tqphu27/grpc_django.git
```
2. Launch the application
```
git checkout dev
bash build.sh
```

3. Execute application functionalities
  - If there is no superuser, you can create one using:
```
python manage.py createsuperuser 
```
  -  Then, access http://localhost:8000/admin/oauth2_provider/application/ to obtain grant_type, client_id, and client_secret information.
  -  After obtaining the above information, generate an access token:
```
curl --location 'http://localhost:8000/o/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: csrftoken=74erCbmX3EfWIFvjHhwdXn89SNxxNDd1n9J9dhvm8FkjTNu4Lc50qd5VRCazOFY3' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'client_id=upwerF0jrragaxxkNXHDMTGGe8ciMwJN6yVoIOAu' \
--data-urlencode 'client_secret=3aa4PCcNRwyXzs86QP0PWnOnko0ZW6ym4WD0W539XjjOuPDggxO6r5bKSdOxW1HkLwBiwLEIxAf5SzmR2qTBoRo1a7dj2E4ur84zde9tbBO7ykGaoKrYgTG53ZsKWFUi'
```
  - Then, start the grpc server:
```
curl --location 'http://localhost:8000/grpc/start/' \
--header 'Content-Type: application/json' \
--header 'Authorization: valid_token' \
--header 'Cookie: csrftoken=74erCbmX3EfWIFvjHhwdXn89SNxxNDd1n9J9dhvm8FkjTNu4Lc50qd5VRCazOFY3' \
--data '{"data": "your_base64_encoded_data"}'
```
- To stop the grpc server:
```
curl --location 'http://localhost:8000/grpc/start/' \
--header 'Content-Type: application/json' \
--header 'Authorization: valid_token' \
--header 'Cookie: csrftoken=74erCbmX3EfWIFvjHhwdXn89SNxxNDd1n9J9dhvm8FkjTNu4Lc50qd5VRCazOFY3' \
--data '{"data": "your_base64_encoded_data"}'
```

4. System testing
  - Run oauth_client.py file to check if the OAuth server is operational. If successful, it will display:
```
{
  'message': 'Successfully!'
}
```
  - Run grbc_client.py file to test the 3 APIs:

    a. Setup - pass the token
  - If successful:
```
{
  SetUp method works. ML status: Active
}
```

  b. Import - allows uploading images and files
  - If successful:
```
{
   Import method works: ml_status: "Imported"
}
```

  c. Action - pass actions (PREDICT, EXPORT, CREATE_DATASET, LOGS, DOWNLOAD_CHECKPOINT)
```
{
   PerformAction method works: ml_status: "PREDICT"
}
```
