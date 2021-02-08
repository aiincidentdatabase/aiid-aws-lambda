#!/usr/bin/env python3

import json
from newsplease import NewsPlease

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else res,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
    }

def lambda_handler(event, context):
    '''Support the HTTP CORS pre-flight, then respond to the actual request.
    '''
    if 'url' in event:
        res = json.dumps(
            NewsPlease.from_url(event['url']).get_dict(),
            default=str)
        return respond(None, res)
    else:
        return respond(None, {})
