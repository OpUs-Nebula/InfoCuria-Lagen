from bs4 import BeautifulSoup
import requests

base_url = "https://lagen.nu/"

def search_by_id(id):
	results = ""
	if "JO" in id:
		dnr = id.split("dnr")[-1].strip()
		url = base_url+"avg/jo/{}".format(dnr)
		html_doc = requests.get(url).text
		results = BeautifulSoup(html_doc, 'html.parser')
	return results

def extract_case_info(soup):
	return {
	"judgement":soup.get_text(),
	"opinion":""
	}

def case_by_id(title):
	search_id = ""

	if "JO" in title:
		case_info = title.split("(")[0]
		dnr = case_info.split("dnr")[-1]
		search_id = "JO dnr "+dnr.strip()

	return extract_case_info(search_by_id(search_id))

	#return extract_case_info(search_by_id(id))




"""
ToDo:
- Fix case of two C- cases(Förenade målen C-509/09 och C-161/10 (eDate advertising))
- Set up ROGUE API
- 

Model notes:

InfoCuris: 7 samples
- All info exists in single space seperated substring

NJA: 7 samples
- ID-String ends after tf

JO: 20 samples
- Seperate out dnr and search for "JO dnr"

KamR: 17 samples
- String after målnr only necessary //Uniform

HFD: 22 samples
- rfd as binding string(search fomat: HFD YYYY:REF) //Not uniformly. Other formats exist.

"""
