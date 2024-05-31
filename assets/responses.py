import json

def get_bin_response(bins, bin_id):

    if len(bins) == 0:
        return {
            'statusCode': 404,
            'body': json.dumps({
                'detail': f'Bin not found: {bin_id}'
            }),
            'headers': {
                "Content-Type": "application/json"
            }
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps(bins, default=str),
            'headers': {
                "Content-Type": "application/json"
            }
        }
    
#Get location shares this handler to avoid redundancy.
def get_bins_response(bins):
    if len(bins) == 0:
        return {
            'statusCode': 404,
            'body': json.dumps({
                'detail': f'Bins not found'
            }),
            'headers': {
                "Content-Type": "application/json"
            }
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps(bins, default=str),
            'headers': {
                "Content-Type": "application/json"
            }
        }
    
def get_usage_response(bins, bin_id, valid_date):
    if valid_date == False:
        return {
            'statusCode': 404,
            'body': json.dumps({
                'detail': f'Invalid Dates'
            }),
            'headers': {
                "Content-Type": "application/json"
            }
        }
    if len(bins) == 0:
        return {
            'statusCode': 404,
            'body': json.dumps({
                'detail': f'No data found for bin: {bin_id}'
            }),
            'headers': {
                "Content-Type": "application/json"
            }
        }
    
    else:
        return {
            'statusCode': 200,
            'body': json.dumps(bins, default=str),
            'headers': {
                "Content-Type": "application/json"
            }
        }