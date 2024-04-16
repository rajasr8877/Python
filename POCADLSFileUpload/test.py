import base64
import xml.etree.ElementTree as ET
import json
from types import SimpleNamespace
import os
import mimetypes

file_path = "C:\\Raja\\Src\\ppt\\UI mocks predesign.pptx" #8 MB File took 4.15 sec
# file_path = "C:\\Raja\\Src\\Anaconda3-2024.02-1-Windows-x86_64_988743.exe" #930 MB File took 296.67 Sec
filename = os.path.basename(file_path)

# Get the file type
# file_type = mimetypes.guess_type(filename)[0]
file_type, encoding = mimetypes.guess_type(filename)
print(f"The file type of '{filename}' is '{file_type}'")

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
print(x)
print(x.name, x.hometown.name, x.hometown.id)

