import json
import boto3
import os
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("HW10-Auctions")

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError
def lambda_handler(event, context):
    try:
        
        body = json.loads(event.get("body", "{}"))


        auctionId = body["auctionId"]
        itemName = body["itemName"]
        description = body.get("description", "")
        reserve = Decimal(str(body.get("reserve", 0)))
        auctionStatus = body.get("auctionStatus", "open")
        winningUserId = body.get("winningUserId", None)

        item = {
            "auctionId": auctionId,
            "itemName": itemName,
            "description": description,
            "reserve": reserve,
            "auctionStatus": auctionStatus
        }
        if winningUserId:
            item["winningUserId"] = winningUserId

        table.put_item(Item=item)
#trying cicd now lol
        return {
            "statusCode": 201,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Auction created successfully",
                "auction": item
            }, default=decimal_default),
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
