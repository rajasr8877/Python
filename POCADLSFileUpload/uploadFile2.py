import base64
import hashlib
import os
import uuid
import requests
from azure.storage.blob import BlobBlock
import xml.etree.ElementTree as ET

def xml_data_of_blocklist(data):
    root = ET.Element("BlockList")
    for item in data:
        block = ET.SubElement(root, item["state"])
        block_id = base64.b64encode(item["id"].encode()).decode()
        block.text = block_id
    xml_data = ET.tostring(root, encoding="utf-8").decode()
    return xml_data
# Define the API endpoint
url = "https://apimtestprocedure.azure-api.net/echo/uploadChunk"
putBlockListurl = "https://apimtestprocedure.azure-api.net/echo/putBlockList"

# Define the file path
file_path = "C:\\Raja\\Src\\ppt\\UI mocks predesign.pptx"
filename = os.path.basename(file_path)

def get_header_value(key: str, filename: str):
    header_values = dict()
    header_values.update({"Ocp-Apim-Subscription-Key": key})
    header_values.update({"filename": filename})
    return header_values

# Open the file in binary mode


def put_block_list_api_call(block_list):
    value = xml_data_of_blocklist(block_list)
    print(value)
    headers2 = {"Content-Type": "application/octet-stream", "Ocp-Apim-Subscription-Key": "f42419223b5d493e9837983665bb6a75",
                "filename": filename}
    response = requests.put(putBlockListurl, data=value, headers=headers2)
    if response.status_code != 201:
        print(f"Error sending remaining chunk: {response.status_code}")




def file_upload():
    with open(file_path, "rb") as f:
        # Get the file size
        file_size = os.path.getsize(file_path)
        print(file_size)
        # Send the first chunk (100 MB)
        # chunk_size = 1 * 1024 * 1024
        chunk_size = 4 * 1024 * 1024
        block_list = []
        for i in range(0, file_size, chunk_size):
            print(f"for loop {i}")
            chunk = f.read(chunk_size)
            blk_id = str(uuid.uuid4())
            headers : dict = get_header_value()
            headers.update({"blockId": blk_id})
            headers.update({"Content-Type": "application/octet-stream"})
            headers.update({"Content-Range": f"bytes {i}-{i + chunk_size - 1}/{file_size}"})
            response = requests.put(url, headers=headers, data=chunk)
            block_list.append(BlobBlock(block_id=blk_id))
            if response.status_code != 201:
                print(f"Error sending chunk {i}: {response.text}")
                break

    # Send the remaining chunk (if any)
        if i < file_size:
            chunk = f.read(file_size - i)
            blk_id = str(uuid.uuid4())
            headers : dict = get_header_value()
            headers.update({"blockId": blk_id})
            headers.update({"Content-Type": "application/octet-stream"})
            headers.update({"Content-Range": f"bytes {i}-{i + chunk_size - 1}/{file_size}"})
            response = requests.put(url, headers=headers, data=chunk)
            block_list.append(BlobBlock(block_id=blk_id))
            if response.status_code != 201:
                print(f"Error sending remaining chunk: {response.status_code}")
        print(block_list)
        put_block_list_api_call(block_list=block_list)

        
