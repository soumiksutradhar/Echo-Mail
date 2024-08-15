import boto3
import json
import requests

def lambda_handler(event, context):
    # Get the S3 bucket and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Parse the filename (key)
    filename = key.split('/')[-1]
    
    # Send a request to the EC2 instance
    ec2_url = "http://<Public-IP>/<folder_name to catch files in ec2>"
    
    # Prepare the data to be sent
    data = {
        'bucket': bucket,
        'key': key,
        'filename': filename,
        'sender_email': '<Email/Outlook ID>',
        'sender_password': '<Password>',
        'subject': '<Subject> ',
        'body': '<body>'
    }
    
    response = requests.post(ec2_url, json=data)
    return {
        'statusCode': 200,
        'body': json.dumps('Request sent to EC2')
    }
