import json
import boto3
import os
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("HW10-Users")

def lambda_handler(event, context):
    try:
        #this is really sus ngl
        # Ensure event['body'] exists and parse it
        body = json.loads(event.get("body", "{}"))
        user_id = body["userId"]
        name = body["name"]
        acct_balance = Decimal(str(body["acctBalance"]))

        # Insert into DynamoDB
        table.put_item(
            Item={
                "userId": user_id,
                "name": name,
                "acctBalance": acct_balance
            }
        )

        # Return proxy-compliant response
        return {
            "statusCode": 201,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "User created successfully",
                "user": {
                    "userId": user_id,
                    "name": name,
                    "acctBalance": float(acct_balance)
                }
            }),
            "isBase64Encoded": False
        }

    except KeyError as e:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": f"Missing field: {str(e)}"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }
