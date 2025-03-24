import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YOUR_TABLE_NAME')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        event_time = record['eventTime']
        
        # In the demo I used object_key as my partition key 
        # If you opted for another name you should replace it down here as well
        table.put_item(
            Item={
                'object_key': object_key,
                'bucket_name': bucket_name,
                'upload_time': event_time
            }
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps('DynamoDB entry created successfully!')
    }
