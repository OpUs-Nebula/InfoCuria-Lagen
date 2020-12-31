from bs4 import BeautifulSoup
import requests

base_url = "https://lagen.nu/search/?"

def search_by_id(id):
	search_string = base_url+"num={}".format(id)
	html_doc = requests.get(search_string).text
	soup = BeautifulSoup(html_doc, 'html.parser')
	return soup

def get_printable(doc_url):
	printable_url = doc_url.replace("document.jsf","document_print.jsf")
	printable_soup = BeautifulSoup(requests.get(printable_url).text)
	list(map(lambda tag: tag.decompose(), printable_soup("script")))
	return printable_soup.get_text(" ")

def extract_case_info(soup):
	judgement_link = soup.find_all(id="mainForm:aff:0:j_id73:0:dec:0:j_id220:0:j_id258:22")
	opinion_link = soup.find_all(id="mainForm:aff:0:j_id73:0:dec:0:j_id220:1:j_id258:22")
	return {
	"judgement":get_printable(judgement_link[0].a["href"]),
	"opinion":get_printable(opinion_link[0].a["href"])
	}

def case_by_id(id):
	return extract_case_info(search_by_id(id))


"""
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
