import json
from InfoCuria.search_scraping import *

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

if __name__ == "__main__":
	print(get_case_info(search_by_id("c-362/14")))
	print("Script Done")