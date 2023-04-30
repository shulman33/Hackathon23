import json
import boto3
from botocore.exceptions import ClientError
from warrant.aws_srp import AWSSRP


def lambda_handler(event, context):
    cognito = boto3.client('cognito-idp')
    client_id = '2faktl10ctmbssu9qt3h093als'
    user_pool_id = 'us-east-1_M99TFERtF'

    body = json.loads(event['body'])
    email = body['email']
    password = body['password']

    aws_srp_client = AWSSRP(username=email, password=password, pool_id=user_pool_id, client_id=client_id, client=cognito)

    try:
        response = aws_srp_client.authenticate_user()
    except ClientError as e:
        print("Error authenticating:", e.response["Error"]["Message"])
        return {
            "statusCode": 400,
            "body": json.dumps({"error": e.response["Error"]["Message"]})
        }

    access_token = response['AuthenticationResult']['AccessToken']
    print("Login successful")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Login successful",
            "access_token": access_token
        })
    }
