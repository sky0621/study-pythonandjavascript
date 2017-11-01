from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://developers.line.me/ja/docs/messaging-api/reference/'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_lineapi_soup():
    res = requests.get(BASE_URL+'#anchor-eab6741c0f596830bffc91eb993f5b3fcfc32b9a', headers=HEADERS)
    return BeautifulSoup(res.content, "lxmld")