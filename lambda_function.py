import json
import InfoCuria.search_scraping as IC
import Lagen.search_scraping as LG

def case_by_source_type(id):
	if id.contains("NJA"):
		return LG.case_by_id(id)
	else:
		return IC.case_by_id(id)

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

if __name__ == "__main__":
	print(IC.case_by_id("c-362/14"))
	print("Script Done")