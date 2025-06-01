import json

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))
        
        # Extract JSON body if called from API Gateway
        if 'body' in event:
            body = json.loads(event['body'])  # Parse stringified JSON
        else:
            body = event  # fallback for direct testing

        message = body.get("message", "No message received")

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({"response": f"Message received: {message}"})
        }
    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

