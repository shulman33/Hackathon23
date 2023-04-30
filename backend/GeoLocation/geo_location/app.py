import json
import boto3
from utils import haversine_distance
from decimal import Decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FinServicesTable')


def fetch_service_providers_from_database():
    response = table.scan()
    return response['Items']


def get_service_providers_near_user(user_location, max_distance=10):
    all_service_providers = fetch_service_providers_from_database()
    nearby_service_providers = list(filter(lambda provider: haversine_distance(
        float(user_location['latitude']),
        float(user_location['longitude']),
        float(provider['latitude']),
        float(provider['longitude'])
    ) <= max_distance, all_service_providers))

    sorted_providers = sorted(nearby_service_providers, key=lambda provider: haversine_distance(
        float(user_location['latitude']),
        float(user_location['longitude']),
        float(provider['latitude']),
        float(provider['longitude'])
    ))
    return sorted_providers


def lambda_handler(event, context):
    user_location = {
        'latitude': float(event['queryStringParameters']['latitude']),
        'longitude': float(event['queryStringParameters']['longitude'])
    }
    max_distance = float(event.get('queryStringParameters', {}).get('max_distance', 10))

    nearby_service_providers = get_service_providers_near_user(user_location, max_distance)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(nearby_service_providers, cls=DecimalEncoder)
    }


