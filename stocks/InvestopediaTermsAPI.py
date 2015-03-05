import urllib
from bs4 import BeautifulSoup

def Definition(term):
    base_url = "http://www.investopedia.com/terms/"
    # Detecting first character because we need this in url
    letter = list(term)
    first_letter = letter[0]
    # In case where first character is a integer
    if first_letter == '5':
        first_letter = '1'
    # Adding all the terms together for making a complete url
    url = base_url+first_letter+'/'+term+'.asp'
    text = urllib.urlopen(url).read()
    soup = BeautifulSoup(text)
    # finding content with 'p' tag
    result = soup.p
    return result.contents[0]


