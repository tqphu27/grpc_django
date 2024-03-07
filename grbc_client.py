from ml_pb2_grpc import MachineLearningStub
from ml_pb2 import TokenRequest, ImportRequest, ActionRequest, FileData, ImportRequest
import grpc

def upload_file_to_server(file_path):
    with open(file_path, 'rb') as f:
        filename = file_path.split('/')[-1]  # Lấy tên file từ đường dẫn
        content = f.read()
        return FileData(filename=filename, content=content)
    
def test_machine_learning_service():
    channel = grpc.insecure_channel('localhost:50052')
    stub = MachineLearningStub(channel)

    # Test phương thức SetUp với token hợp lệ
    token_request = TokenRequest(token="oYhboFNYlczSrexoStBYSMeTgg1LuA")
    try:
        response = stub.SetUp(token_request)
        print("SetUp method works. ML status:", response.ml_status)
    except grpc.RpcError as e:
        print("SetUp method failed:", e)

    # Test phương thức Import
    # import_request = ImportRequest(data="your_base64_encoded_data")
    files = [upload_file_to_server('1.png'), upload_file_to_server('2.png')]
    import_request = ImportRequest(files=files)
    try:
        response = stub.Import(import_request)
        print("Import method works:", response)
    except grpc.RpcError as e:
        print("Import method failed:", e)

    # Test phương thức PerformAction
    # PREDICT = 0; EXPORT = 1; CREATE_DATASET = 2; LOGS = 3; DOWNLOAD_CHECKPOINT = 4;
    action_request = ActionRequest(action_type=ActionRequest.DOWNLOAD_CHECKPOINT)
    try:
        response = stub.PerformAction(action_request)
        print("PerformAction method works:", response)
    except grpc.RpcError as e:
        print("PerformAction method failed:", e)

if __name__ == "__main__":
    test_machine_learning_service()
