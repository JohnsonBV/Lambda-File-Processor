import json

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))

        # Get the JSON body from the API Gateway event
        body = json.loads(event.get("body", "{}"))
        message = body.get("message", "No message received")

        return {
            'statusCode': 200,
            'body': json.dumps({'echo': message})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

