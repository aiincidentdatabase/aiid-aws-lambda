import boto3
import json
from newsplease import NewsPlease

def respond(err, res=None):
    article = NewsPlease.from_url('https://seanbmcgregor.com/DeepfakeDetectionGame.html')
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(article),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
    }

def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.
    '''
    operation = event['httpMethod']
    if operation in ['GET', 'POST', 'PUT', 'OPTIONS']:
        payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
        return respond(None, {})
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
