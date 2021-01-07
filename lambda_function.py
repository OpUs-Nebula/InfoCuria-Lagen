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
        string_bytes = base64.b64decode(event["body"]) 
        event["body"] = string_bytes.decode() 
    
    case_title = event["body"].strip()
    return {
        'statusCode': 200,
        'body': json.dumps(case_by_source_type(case_title))
    }

if __name__ == "__main__":
    #print(IC.case_by_id("C-131/12 (Mario Costeja González – the right to be forgotten)"))
    print("Script Done")
    #print(LG.case_by_id("JO 2016-01-05 dnr 7041-2013 (Radering av videoinspelningar)"))
    #events = [{"body":"Qy0xMzEvMTIgKE1hcmlvIENvc3RlamEgR29uesOhbGV6IOKAkyB0aGUgcmlnaHQgdG8gYmUgZm9yZ290dGVuKQ==",
    #"isBase64Encoded":True},{"body":"Sk8gMjAxOS0wNi0wNCwgZG5yIDY3OTQtMjAxNw==","isBase64Encoded":True}]
    #results = list(map(lambda event: lambda_handler(event,None),events))
    #print(results)
    print(IC.case_by_id("Förenade målen C-509/09 och C-161/10 (eDate advertising"))