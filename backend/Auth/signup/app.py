import json
import boto3

# import requests

USER_POOL_ID = 'us-east-1_M99TFERtF'
CLIENT_ID = '2faktl10ctmbssu9qt3h093als'

cognito = boto3.client('cognito-idp')


def lambda_handler(event, context):
    body = json.loads(event['body'])

    email = body['email']
    given_name = body['given_name']
    surname = body['surname']
    password = body['password']

    try:
        response = cognito.sign_up(
            ClientId=CLIENT_ID,
            Username=email,
            Password=password,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': email
                },
                {
                    'Name': 'given_name',
                    'Value': given_name
                },
                {
                    'Name': 'family_name',
                    'Value': surname
                }
            ]
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'User signed up successfully',
                'user': response['UserSub']
            })
        }
    except cognito.exceptions.ClientError as e:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({
                'message': e.response['Error']['Message']
            })
        }

