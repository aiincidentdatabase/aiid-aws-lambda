#!/usr/bin/env python3

import json
from newsplease import NewsPlease

def lambda_handler(event, context):
    '''Support the HTTP CORS pre-flight, then respond to the actual request.
    '''
    context.log('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz!')
    context.log(event)
    context.log(str(event.keys()))
    if 'body' in event:
        context.log('000000000000000000000000')
        context.log(event['rawQueryString'])
        context.log('2222222222222222!')
        context.log(json.loads(event['body']))
        context.log('333333333333')
        context.log(event['rawQueryString'])
        context.log('4444444444444')
        req = json.loads(event['body'])
        context.log(req.keys())
        res = json.dumps(
            NewsPlease.from_url(req['url']).get_dict(),
            default=str)
        return res
    else:
        context.log('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy!')
        return "returning nothing"
