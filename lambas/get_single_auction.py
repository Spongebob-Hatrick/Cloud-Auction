'''getting all users in db'''
import json
import boto3
import os
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('USERS_TABLE', 'HW10-Auctions')
table = dynamodb.Table(table_name)

#Helper to serialize Decimal objects
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)



def lambda_handler(event, context):
    try:

       # AuctionId comes from the path parameter: /auction/{auctionId}
        path_params = event.get('pathParameters') or {}
        auction_id = path_params.get('auctionId')

        if not auction_id:
            raise ValueError("Missing required path parameter: auctionId")

        # Fetch the auction from DynamoDB
        response = table.get_item(Key={'auctionId': auction_id})

        if 'Item' not in response:
            return {
                "statusCode": 404,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,GET"
                },
                "body": json.dumps({"error": "Auction not found"})
            }

        auction = response['Item']

        # Return the found auction
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "OPTIONS,GET"
            },
            "body": json.dumps(auction, cls=DecimalEncoder)
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "OPTIONS,GET"
            },
            "body": json.dumps({"error": str(e)})
        }