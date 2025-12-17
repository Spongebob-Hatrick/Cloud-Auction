import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("HW10-Auctions")

# Helper function to convert Decimals to floats for JSON
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def lambda_handler(event, context):
    try:
        # Scan retrieves all auctions (fine for small data sets)
        response = table.scan()
        items = response.get("Items", [])

        # Normalize field names and types
        auctions = [
            {
                "auctionId": item.get("auctionId"),
                "itemName": item.get("itemName"),
                "reserve": float(item.get("reserve", 0)),
                "description": item.get("description", ""),
                "auctionStatus": item.get("auctionStatus", "open"),
                "winningUserId": item.get("winningUserId")
            }
            for item in items
        ]

        # Return proper API Gateway proxy response
        return {
           "statusCode": 200,
        "headers": {"Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST"
        },
        "body": json.dumps(auctions, default=decimal_default),
        }

# return {
#         "statusCode": 200,
#         "headers": {"Content-Type": "application/json",
#         "Access-Control-Allow-Origin": "*",
#         "Access-Control-Allow-Headers": "*",
#         "Access-Control-Allow-Methods": "OPTIONS,GET,POST"
#         },
#         "body": json.dumps(users, default=decimal_default),
       
#     }
    except Exception as e:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }
