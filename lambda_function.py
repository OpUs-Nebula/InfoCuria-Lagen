import json
import base64
import InfoCuria.search_scraping as IC
import Lagen.search_scraping as LG

def case_by_source_type(title):
    if True in list(map(lambda court: court in title,["JO"])):
        return LG.case_by_id(title)
    else:
        return IC.case_by_id(title)

def lambda_handler(event, context):
    # TODO implement
    if event["isBase64Encoded"]:
        base64_bytes = event["body"].encode("ascii") 
        string_bytes = base64.b64decode(base64_bytes) 
        event["body"] = string_bytes.decode("ascii") 
    
    case_title = event["body"].strip()
    return {
        'statusCode': 200,
        'body': json.dumps(case_by_source_type(case_title))
    }

if __name__ == "__main__":
    #print(IC.case_by_id("C-131/12 (Mario Costeja González – the right to be forgotten)"))
    print("Script Done")
    print(LG.case_by_id("JO 2016-01-05 dnr 7041-2013 (Radering av videoinspelningar)"))
    event = {"body":"JO, 2014-09-09, dnr 3032-2011"}
    lambda_handler(event,None)