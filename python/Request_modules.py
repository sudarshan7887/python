import requests
r = requests.get("https://site.financialmodelingprep.com/developer")
# get a content in program through url
print(r.text)
print(r.status_code)
