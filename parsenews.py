#!/usr/bin/env python3

import json
from newsplease import NewsPlease

def lambda_handler(event, context):
    '''Support the HTTP CORS pre-flight, then respond to the actual request.
    '''
    context.log('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz!')
    context.log(event)
    context.log(str(event.keys()))
    if 'queryStringParameters' in event:
        context.log('000000000000000000000000')
        context.log(event['queryStringParameters'])
        context.log('2222222222222222!')
        res = json.dumps(
            NewsPlease.from_url(event['queryStringParameters']['url']).get_dict(),
            default=str)
        context.log('3333333333333333333333333')
        return res
    else:
        context.log('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy!')
        return "returning nothing"
