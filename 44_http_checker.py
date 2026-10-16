"""Distinct Python example #44."""
from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError
url=input("URL: ")
try:
 with urlopen(Request(url,method="HEAD"),timeout=5) as response:print(response.status,response.reason)
except (URLError,HTTPError,TimeoutError) as error:print("Unavailable:",error)
