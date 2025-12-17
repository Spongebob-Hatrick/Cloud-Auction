# Hello TA grading HW 10 (or 11) (now 12 lol) MS 2 for me :)

### Website
* `http://hw-10-11-auction.s3-website-us-east-1.amazonaws.com/` <br>


## ISSUES I HAVE
* For whatever reason, if you directly open my static website, it will be blank. Just click on one of the icons in the top right. 
  * I usually hit `Users`
  * Then everything works as normal. Just a hiccup getting started.
* I  tagged the new things as hw `12` for the new project submission
* I also only put this in a "dev" stage. I don't do my stuff in prod & it works so I'm not changing it now.  <br>


#### Things to watch/ what I used
* Cloudwatch: 
  * `/aws/lambda/hw10-create_auction`
  * `/aws/lambda/hw10-create_user`
  * `/aws/lambda/hw10-get_auctions`
  * `/aws/lambda/hw10-get_single_auction`
  * `/aws/lambda/hw10-get_users`
  * `/aws/lambda/hw10-get_bids_for_auctionid`
  * `/aws/vendedlogs/states/HW10-Close_Auction-Logs`
  * `/aws/vendedlogs/states/HW10-Bidding-Logs`


* S3: `hw10-11-auction`

* Dynamo
  * `HW10-Auctions`
  * `HW10-Bids`
  * `HW10-Users`


* API Gateway: `hw10-AucitonAPI (again)` <br>
  
* Lambda:
  * `hw10-create_auction`
  * `hw10-create_user`
  * `hw10-get_auctions`
  * `hw10-get_single_auction`
  * `hw10-get_users`
  * `hw10-get_bids_for_auctionid`
   <br>
  
*  State Machines/Step Functions
   * `HW10-Bidding`
   * `HW10-Close_Auction`
<br>
* SNS & SQS
  * `hw10-Bidding`
  * `hw10-Bidding`
    * It's the same for SNS & SQS
  
  Well that's it for this semester. Thanks y'all!
