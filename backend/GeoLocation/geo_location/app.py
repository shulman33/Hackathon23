import json
import boto3
from utils import haversine_distance

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FinancialServiceProviders')


def fetch_service_providers_from_database():
    response = table.scan()
    return response['Items']


def get_service_providers_near_user(user_location, max_distance=10):
    all_service_providers = fetch_service_providers_from_database()
    nearby_service_providers = list(filter(lambda provider: haversine_distance(
        user_location['latitude'],
        user_location['longitude'],
        provider['latitude'],
        provider['longitude']
    ) <= max_distance, all_service_providers))

    sorted_providers = sorted(nearby_service_providers, key=lambda provider: haversine_distance(
        user_location['latitude'],
        user_location['longitude'],
        provider['latitude'],
        provider['longitude']
    ))

    return sorted_providers


def lambda_handler(event, context):

    user_location = {
        'latitude': event['latitude'],
        'longitude': event['longitude']
    }
    max_distance = event.get('max_distance', 10)

    nearby_service_providers = get_service_providers_near_user(user_location, max_distance)

    return {
        'statusCode': 200,
        'body': json.dumps(nearby_service_providers)
    }
