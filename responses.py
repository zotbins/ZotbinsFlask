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
    