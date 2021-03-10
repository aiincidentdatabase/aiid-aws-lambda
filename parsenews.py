#!/usr/bin/env python3

import json
from newsplease import NewsPlease

def lambda_handler(event, context):
    '''Respond to GET requests with 'URL' as the only querystring parameter and return
    a parsed version of the content at the URL.
    '''
    if 'queryStringParameters' in event:
        res = json.dumps(
            NewsPlease.from_url(event['queryStringParameters']['url']).get_dict(),
            default=str)
        return res
    else:
        return "Query string not found in event. Please check the get request parameters"
