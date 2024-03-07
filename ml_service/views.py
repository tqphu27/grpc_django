from concurrent import futures
import grpc
from django.http import HttpResponse, JsonResponse
from django.views import View
from ml_pb2_grpc import MachineLearningServicer
from ml_pb2_grpc import add_MachineLearningServicer_to_server
from ml_pb2 import SetUpResponse, ImportResponse, ActionResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from oauth2_provider.models import AccessToken
import threading

class MachineLearningServicer(MachineLearningServicer):
    def __init__(self):
        self.ml_status = "Inactive"  
    
    def SetUp(self, request, context):
        try:
            token = request.token
            try:
                AccessToken.objects.get(token=token)
            except AccessToken.DoesNotExist:
                context.set_code(grpc.StatusCode.UNAUTHENTICATED)
                context.set_details("Access token is invalid")
                return SetUpResponse(ml_status=self.ml_status)

            # Cập nhật ml_status
            self.ml_status = "Active"
            return SetUpResponse(ml_status=self.ml_status)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details(e)
            return SetUpResponse(ml_status=self.ml_status)
    
    def Import(self, request, context):
        try:
            for file_data in request.files:
                filename = file_data.filename
                content = file_data.content

            # Lưu trữ hoặc xử lý file
                
            self.ml_status = "Imported"
            return ImportResponse(ml_status=self.ml_status)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details(e)
            return SetUpResponse(ml_status=self.ml_status)

    def PerformAction(self, request, context):
        try:
            action_type = request.action_type
            if action_type == 0:
                self.ml_status = "PREDICT"
            elif action_type == 1:
                self.ml_status = "EXPORT"
            elif action_type == 2:
                self.ml_status = "CREATE_DATASET"
            elif action_type == 3:
                self.ml_status = "LOGS"
            elif action_type == 4:
                self.ml_status = "DOWNLOAD_CHECKPOINT"

            return ActionResponse(ml_status=self.ml_status)
        except Exception as e:
                context.set_code(grpc.StatusCode.UNAUTHENTICATED)
                context.set_details(e)
                return SetUpResponse(ml_status=self.ml_status)

@method_decorator(csrf_exempt, name='dispatch')
class GRPCView(View):
    server = None

    def get(self, request):
        return HttpResponse("Welcome to gRPC server")
    
    def post(self, request):
        try:
            if GRPCView.server is None:
                GRPCView.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
                add_MachineLearningServicer_to_server(MachineLearningServicer(), GRPCView.server)
                GRPCView.server.add_insecure_port('[::]:50052')  # Define your desired port
                threading.Thread(target=GRPCView.server.start).start()
                return JsonResponse({'message': 'gRPC server is starting'})
            else:
                return JsonResponse({'message': 'gRPC server is already running'})
        except Exception as e:
            return JsonResponse({'message': e})

@csrf_exempt
def stop_grpc_server(request):
    try:
        if request.method == 'POST':
            if GRPCView.server:
                GRPCView.server.stop(None)
                GRPCView.server = None
                return JsonResponse({'message': 'gRPC server stopped'})
            else:
                return JsonResponse({'message': 'gRPC server is not running'})
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)
        
    except Exception as e:
            return JsonResponse({'message': e})