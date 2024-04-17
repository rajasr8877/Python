import json
import time
from types import SimpleNamespace
import aiohttp
import asyncio
import base64
import os
import uuid
import xml.etree.ElementTree as ET
from azure.storage.blob import BlobBlock


def xml_data_of_blocklist(data):
    root = ET.Element("BlockList")
    for item in data:
        block = ET.SubElement(root, item["state"])
        block_id = base64.b64encode(item["id"].encode()).decode()
        block.text = block_id
    xml_data = ET.tostring(root, encoding="utf-8").decode()
    return xml_data


async def put_request(url, headers, chunk_data):
    async with aiohttp.ClientSession() as session:
        async with session.put(url, headers=headers, data=chunk_data) as response:
            body = await response.text()
            print(f"body = {body}")
            return response

async def put_request_res(url, headers, chunk_data):
    async with aiohttp.ClientSession() as session:
        async with session.put(url, headers=headers, data=chunk_data) as response:
            body = await response.text()
            print(f"body = {body}")
            data = json.loads(body,  object_hook=lambda d: SimpleNamespace(**d))
            return data

def get_header_value(key: str, filename: str):
    header_values = dict()
    header_values.update({"Ocp-Apim-Subscription-Key": key})
    header_values.update({"filename": filename})
    header_values.update({"datetime": "10/09/2018"})
    header_values.update({"procedureNo": "1"})
    header_values.update({"type": "Vedios"})
    header_values.update({"Content-Type": "application/octet-stream"})
    return header_values


def put_block_list_api_call(url, block_list, filename, key):
    value = xml_data_of_blocklist(block_list)
    print(value)
    headers = get_header_value(filename=filename, key=key)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    response = loop.run_until_complete(put_request(url, headers=headers, chunk_data=value))
    # response = loop.run_until_complete(put_request_res(url, headers=headers, chunk_data=value))
    # print(response)
    if response.status != 200:
        print(f"Error sending remaining chunk: {response.status}")
        print(response.text)

# Open the file in binary mode
def file_upload(file_path, filename, key):
    # url = "https://apimtestprocedure.azure-api.net/echo/uploadChunk"
    url = "https://apimtestprocedure.azure-api.net/echo/uploadFileTest"
    # putBlockListurl = "https://apimtestprocedure.azure-api.net/echo/putBlockList"
    start_time = time.time()
    print(f"Start Time ============= {start_time}")
    with open(file_path, "rb") as f:
        # Get the file size
        file_size = os.path.getsize(file_path)
        print(file_size)
        chunk_size = 4 * 1024 * 1024
        block_list = []
        for i in range(0, file_size, chunk_size):
            print(f"for loop {i}")
            chunk =  f.read(chunk_size)
            blk_id = str(uuid.uuid4())
            headers: dict = get_header_value(filename=filename, key=key)
            headers.update({"blockId": blk_id})
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            response = loop.run_until_complete(put_request(url=url, headers=headers, chunk_data=chunk))
            if response.status != 201:
                print(f"Error sending chunk {i}: {response.text}")
                break
            block_list.append(BlobBlock(block_id=blk_id))

        print(f"Print i value {i}: and file_size == {file_size}")
    end_time = time.time()
    duration = end_time - start_time
    print(f"Upload complete. Time duration: {duration} seconds.")



def main():
    # file_path = "C:\\Raja\\Src\\VSCode-win32-x64-1.87.2.zip" #130 MB file
    # file_path = "C:\\Raja\\Src.zip" #4.25 GB MB file
    file_path = "C:\\Raja\\Src\\ppt\\UI mocks predesign.pptx" #8 MB File took 4.15 sec
    # file_path = "C:\\Raja\\Src\\Anaconda3-2024.02-1-Windows-x86_64_988743.exe" #930 MB File took 296.67 Sec
    filename = os.path.basename(file_path)
    subscripion_key = "f42419223b5d493e9837983665bb6a75"
    file_upload(file_path, filename, subscripion_key)


if __name__ == '__main__':
    # asyncio.run(main())
    main()