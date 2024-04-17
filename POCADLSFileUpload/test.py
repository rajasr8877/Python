import base64
import xml.etree.ElementTree as ET
import json
from types import SimpleNamespace
import os
import mimetypes
# import furl
import datetime
from urllib import parse

from requests.models import PreparedRequest
url = 'http://example.com/search'
params = {'lang':'en','tag':'python'}
req = PreparedRequest()
req.prepare_url(url, params)
print(req.url)
# aa = parse.urlencode({'lang':'en','tag':'python'})


def get_url_with_query_params(url:str, params:dict):
    # url += ('&' if parse.urlparse(url).query else '?') + parse.urlencode(params)
    url += ('&', '?')[parse.urlparse(url).query == ''] + parse.urlencode(params)
    # print(url)
    return url


# url = "https://stackoverflow.com/search"
# params = {'lang':'en','tag':'python'}

# url += ('&' if parse.urlparse(url).query else '?') + parse.urlencode(params)

print(get_url_with_query_params(url,params))
# get current date
current_date = datetime.date.today()
print(current_date)

# get the current date and time
now = datetime.datetime.now()
print(now)

print(dir(datetime),"\n")

d1 = datetime.date(year = 2018, month = 7, day = 12)
print("Custom date d1 :", d1,"\n")
d1  = d1.strftime("%m/%d/%Y")
print("Custom Fomated date d1 :", d1,"\n")

t = now.strftime("%H:%M:%S")
print("Time:", t,"\n")

s1 = now.strftime("%m/%d/%Y")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

file_path = "C:\\Raja\\Src\\ppt\\UI mocks predesign.pptx" #8 MB File took 4.15 sec
# file_path = "C:\\Raja\\Src\\Anaconda3-2024.02-1-Windows-x86_64_988743.exe" #930 MB File took 296.67 Sec
filename = os.path.basename(file_path)

# Get the file type
# file_type = mimetypes.guess_type(filename)[0]
file_type, encoding = mimetypes.guess_type(filename)
# print(f"The file type of '{filename}' is '{file_type}'")

data = [
    {'id': '3e1cd50f-1b93-4cc6-86f1-8239fc074497', 'state': 'Latest', 'size': None},
    {'id': '378ccaf0-b2b8-49eb-908f-5e1b6ad833b4', 'state': 'Latest', 'size': None}
]

# root = ET.Element("BlockList")
# for item in data:
#     block = ET.SubElement(root, item["state"])
#     block.text = item["id"] if item["size"] is None else base64.b64encode(item["id"].encode()).decode()

# xml_data = ET.tostring(root, encoding="utf-8").decode()

# print(xml_data)



data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
# print(x)
# print(x.name, x.hometown.name, x.hometown.id)

