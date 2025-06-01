import json

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))
        message = event.get("message", "No message received")
        return {
            'statusCode': 200,
            'body': json.dumps({"response": f"Message received: {message}"})
        }
    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

