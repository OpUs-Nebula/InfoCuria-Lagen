from bs4 import BeautifulSoup
import requests

base_url = "http://curia.europa.eu/juris/liste.jsf?"

def search_by_id(id):
	search_string = base_url+"num={}".format(id)
	html_doc = requests.get(search_string).text
	soup = BeautifulSoup(html_doc, 'html.parser')
	return soup

def get_case_info(soup):
	judgement_link = soup.find_all(id="mainForm:aff:0:j_id73:0:dec:0:j_id220:1:j_id258:22")
	return judgement_link

