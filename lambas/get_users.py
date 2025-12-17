'''getting all users in db'''
import json
import boto3
import os
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('USERS_TABLE', 'HW10-Users')
table = dynamodb.Table(table_name)

#Helper to serialize Decimal objects
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError



def lambda_handler(event, context):
    try:
        response = table.scan()
        items = response.get("Items", [])

        users = [
            {
                "userId": item.get("userId"),
                "name": item.get("name"),
                "acctBalance": float(item.get("acctBalance"))
            }
            for item in items
        ]

        return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST"
        },
        "body": json.dumps(users, default=decimal_default),
       
    }
        
        

    except Exception as e:
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }
