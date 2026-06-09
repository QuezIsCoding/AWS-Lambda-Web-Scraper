import json

def lambda_handler(event, context):
        # Cloudwatch log for debugging purposes
        print('LOG: Phase 1 lambda has been triggered')
        # Step 1: Look inside the incoming package for query params.
        query_params = event.get('queryStringParameters') or {}

        # Step 2: Extract the specific piece of data labeled 'url'
        target_url = query_params.get('url')

        # Cloudwatch log for debugging purposes
        print(f"log': f'The target URL is {target_url}")

        # Step 3: Return  the URL back to the screen for verification
        return{
            'statusCode': 200,
            'body': json.dumps({
                'message' : 'Successfully read the URL from the test event.!',
                'url': target_url
            })
       
    }
