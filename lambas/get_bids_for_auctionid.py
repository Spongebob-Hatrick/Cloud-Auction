import json
import boto3
from decimal import Decimal
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("HW10-Bids")

# Helper function to convert Decimals to floats for JSON
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError


def lambda_handler(event, context):
    # auctionId can be passed in from API Gateway as a query parameter,
    # or from Step Functions as event["auctionId"]
    
    auction_id = None
    
    # API Gateway: GET /bid?auctionId=123
    if "queryStringParameters" in event and event["queryStringParameters"]:
        auction_id = event["queryStringParameters"].get("auctionId")
    
    # Step Function input: { "auctionId": "123" }
    if not auction_id and "auctionId" in event:
        auction_id = event["auctionId"]
    
    if not auction_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing auctionId"})
        }
    
    try:
        # Query DynamoDB for items with this auctionId
        response = table.query(
            KeyConditionExpression=Key('auctionId').eq(auction_id),
            ScanIndexForward=True   # True = sort ascending by timestamp (SK)
        )
        
        bids = response.get('Items', [])
        
        return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST"
        },
        "body": json.dumps(bids, default=decimal_default)
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }