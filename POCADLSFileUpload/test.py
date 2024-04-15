import base64
import xml.etree.ElementTree as ET

data = [
    {'id': '3e1cd50f-1b93-4cc6-86f1-8239fc074497', 'state': 'Latest', 'size': None},
    {'id': '378ccaf0-b2b8-49eb-908f-5e1b6ad833b4', 'state': 'Latest', 'size': None}
]

root = ET.Element("BlockList")
for item in data:
    block = ET.SubElement(root, item["state"])
    block.text = item["id"] if item["size"] is None else base64.b64encode(item["id"].encode()).decode()

xml_data = ET.tostring(root, encoding="utf-8").decode()

print(xml_data)