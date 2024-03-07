# grpc_django

Cách sử dụng ứng dụng

1. Clone code về và chạy ứng dụng
```
git clone https://github.com/tqphu27/grpc_django.git
```
2. Khởi chạy ứng dụng
```
git checkout dev
bash build.sh
```

3. Thực hiện các chức năng ứng dụng
  - Nếu chưa có super user thì có thể tạo user user
```
python manage.py createsuperuser 
```
  -  Sau đó truy cập vào http://localhost:8000/admin/oauth2_provider/application/ để lấy thông tin grant_type, client_id, client_secret
  -  Sau khi có được thông tin trên, thực hiện tạo ra access-token:
```
curl --location 'http://localhost:8000/o/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: csrftoken=74erCbmX3EfWIFvjHhwdXn89SNxxNDd1n9J9dhvm8FkjTNu4Lc50qd5VRCazOFY3' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'client_id=upwerF0jrragaxxkNXHDMTGGe8ciMwJN6yVoIOAu' \
--data-urlencode 'client_secret=3aa4PCcNRwyXzs86QP0PWnOnko0ZW6ym4WD0W539XjjOuPDggxO6r5bKSdOxW1HkLwBiwLEIxAf5SzmR2qTBoRo1a7dj2E4ur84zde9tbBO7ykGaoKrYgTG53ZsKWFUi'
```
  - Sau đó, khởi chạy grpc server:
```
curl --location 'http://localhost:8000/grpc/start/' \
--header 'Content-Type: application/json' \
--header 'Authorization: valid_token' \
--header 'Cookie: csrftoken=74erCbmX3EfWIFvjHhwdXn89SNxxNDd1n9J9dhvm8FkjTNu4Lc50qd5VRCazOFY3' \
--data '{"data": "your_base64_encoded_data"}'
```
- Để ngắt grpc server :
```
curl --location 'http://localhost:8000/grpc/start/' \
--header 'Content-Type: application/json' \
--header 'Authorization: valid_token' \
--header 'Cookie: csrftoken=74erCbmX3EfWIFvjHhwdXn89SNxxNDd1n9J9dhvm8FkjTNu4Lc50qd5VRCazOFY3' \
--data '{"data": "your_base64_encoded_data"}'
```

4. Kiểm thử hệ thống 
  - Chạy file oauth_client.py để kiểm tra Oauth server đã hoạt động chưa, nếu thành công nó sẽ hiện:
```
{
  'message': 'Successfully!'
}
```
  - Chạy file grbc_client.py để kiểm tra 3 api

    a. Setup, truyền vào token
  - Nếu thành công: 
```
{
  SetUp method works. ML status: Active
}
```
  b. Import - cho phép upload ảnh, các file
  - Nếu thành công 
```
{
   Import method works: ml_status: "Imported"
}
```
  c. Action -truyền vào các action (PREDICT, EXPORT, CREATE_DATASET, LOGS, DOWNLOAD_CHECKPOINT)
```
{
   PerformAction method works: ml_status: "PREDICT"
}
```
