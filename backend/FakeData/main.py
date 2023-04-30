import boto3
import random
from faker import Faker

# Create a Faker instance
fake = Faker()

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FinServicesTable')

# Define the number of records to generate
num_records = 50

# Define service types
service_types = ['Banking', 'Insurance', 'Investment', 'Credit Score', 'Loans', 'Mortgage', 'Retirement']

# Generate and insert fake data
for _ in range(num_records):
    provider_name = fake.company()
    service_type = random.choice(service_types)
    description = fake.text(max_nb_chars=200)
    fee = random.randint(5, 500)  # Random fee between 5 and 500
    certifications = ', '.join(fake.words(nb=3))  # Random certifications (3 words)
    latitude = round(fake.latitude(), 6)
    longitude = round(fake.longitude(), 6)

    # Create the item for DynamoDB
    item = {
        'providerName': provider_name,
        'serviceType': service_type,
        'description': description,
        'fee': fee,
        'certifications': certifications,
        'latitude': latitude,
        'longitude': longitude
    }

    # Put the item into the DynamoDB table
    table.put_item(Item=item)

    # Print the item for debugging purposes
    print(f"Inserted item: {item}")


