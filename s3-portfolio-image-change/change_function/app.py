import os
import json
import boto3

def lambda_handler(event, context):
    AWS_S3_BUKET_NAME = 'test-bucket'
    AWS_S3_OBJECT_NAME = 'info.json'

    # SAM LOCAL実行時のエンドポイント切替
    if os.getenv("AWS_SAM_LOCAL"):
        s3 = boto3.resource('s3', endpoint_url='http://host.docker.internal:4572/')
    else:
        s3 = boto3.resource('s3', endpoint_url='http://localhost:4572/')

    obj = s3.Object(AWS_S3_BUKET_NAME, AWS_S3_OBJECT_NAME)

    response  = obj.get()
    json_file = json.loads(response['Body'].read())

    # S3から取得したJSONファイルの内容を書換える
    if json_file['info'] == "0":
        write_data   = {"info": "1"}
        obj.put(Body = json.dumps(write_data))
    else:
        write_data   = {"info": "0"}
        obj.put(Body = json.dumps(write_data))

    return {
        "message": "Changed S3 jsonfile ok"
    }
