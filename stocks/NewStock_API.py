import urllib
from bs4 import BeautifulSoup

base_url = 'http://money.rediff.com/companies/'

def Get_content(symbol):
    symbol.upper()
    url = base_url+symbol
    text = urllib.urlopen(url).read()
    soup = BeautifulSoup(text)
    return soup

def Get_Quote(symbol):
    soup = Get_content(symbol)
    result = soup.find("span", {"id": "ltpid"}).contents[0]
    return result

def Get_previous_close(symbol):
    soup = Get_content(symbol)
    result = soup.find("span", {"id": "PrevClose"}).contents[0]
    return result

def Get_percent_change(symbol):
    soup = Get_content(symbol)
    result = soup.find("span", {"id": "ChangePercent"}).contents[0]
    return result

def Get_Days_high(symbol):
    soup = Get_content(symbol)
    result = soup.find("span", {"id": "highlow"}).contents[0]
    final_result = result.split()
    return final_result[0]

def Get_Days_low(symbol):
    soup = Get_content(symbol)
    result = soup.find("span", {"id": "highlow"}).contents[0]
    final_result = result.split()
    return final_result[2]

def Get_volume(symbol):
    soup = Get_content(symbol)
    result = soup.find("span", {"id": "Volume"}).contents[0]
    return result

def Get_52_week_high(symbol):
    soup = Get_content(symbol)
    result = soup.find("span", {"id": "FiftyTwoHighlow"}).contents[0]
    final_result = result.split()
    return final_result[0]

def Get_52_week_low(symbol):
    soup = Get_content(symbol)
    result = soup.find("span", {"id": "FiftyTwoHighlow"}).contents[0]
    final_result = result.split()
    return final_result[2]

def Get_52_week_high_low(symbol):
    soup = Get_content(symbol)
    result = soup.find("span", {"id": "FiftyTwoHighlow"}).contents[0]
    return result

def Get_days_high_low(symbol):
    soup = Get_content(symbol)
    result = soup.find("span", {"id": "highlow"}).contents[0]
    return result


