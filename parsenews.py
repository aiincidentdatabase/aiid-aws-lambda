#!/usr/bin/env python3

import json
from newsplease import NewsPlease

def lambda_handler(event, context):
    '''Support the HTTP CORS pre-flight, then respond to the actual request.
    '''
    context.log('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz!')
    context.log(event)
    context.log(str(event.keys()))
    if 'url' in event:
        context.log('2222222222222222!')
        context.log(event['url'])
        res = json.dumps(
            NewsPlease.from_url(event['url']).get_dict(),
            default=str)
        return res
    else:
        context.log('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy!')
        return "returning nothing"
