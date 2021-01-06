from bs4 import BeautifulSoup
import requests

base_url = "http://curia.europa.eu/juris/liste.jsf?"

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

def case_by_id(title):
	print(title)
	case_id = [ word for word in title.split() if word.startswith('C-')]
	return extract_case_info(search_by_id(case_id[0]))