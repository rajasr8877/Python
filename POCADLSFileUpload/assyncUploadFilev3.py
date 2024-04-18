import asyncio
import base64
import json
import os
import time
import uuid
import xml.etree.ElementTree as ET
from types import SimpleNamespace

import aiofiles
import aiohttp
from azure.storage.blob import BlobBlock


def xml_data_of_blocklist(data):
    root = ET.Element("BlockList")
    for item in data:
        block = ET.SubElement(root, item["state"])
        block_id = base64.b64encode(item["id"].encode()).decode()
        block.text = block_id
    xml_data = ET.tostring(root, encoding="utf-8").decode()
    return xml_data

# chunk_size=4194304 4 MB
# chunk_size=2097152 2 MB

async def read_large_file(file_path, key:str, filename:str, chunk_size=2097152):
    start_time = time.time()
    print(f"Start Time ============= {start_time}")
    async with aiofiles.open(file_path, mode='rb') as f:
        block_list = []
        while True:
            blk_id = str(uuid.uuid4())
            # block_list_t = []
            chunk = await f.read(chunk_size)
            if not chunk:
                break
            headers :dict = get_header_value(key, filename)
            headers.update({"blockId": blk_id})
            await make_request(chunk,headers)
            block_list.append(BlobBlock(block_id=blk_id))
            # block_list_t.append(BlobBlock(block_id=blk_id))
        await make_blocklist_request(block_list, headers)
        # headers :dict = get_header_value(key, filename)
        # await make_blocklist_request(block_list, headers)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Upload complete. Time duration: {duration} seconds.")

async def make_request(chunk, headers:dict):
    async with aiohttp.ClientSession() as session:
        async with session.put('https://apimtestprocedure.azure-api.net/echo/putBlock', data=chunk, headers=headers) as response:
            body = await response.text()
            data = json.loads(body,  object_hook=lambda d: SimpleNamespace(**d))
            print(data.response.statusCode)

async def make_blocklist_request(blocklist, headers:dict):
    if "blockId" in headers:
        headers.pop("blockId")
    data = xml_data_of_blocklist(blocklist)
    async with aiohttp.ClientSession() as session:
        async with session.put('https://apimtestprocedure.azure-api.net/echo/putBlockListIM', data=data, headers=headers) as response:
            body = await response.text()
            print(body)
            return data


def get_header_value(key: str, filename: str):
    header_values = dict()
    header_values.update({"Ocp-Apim-Subscription-Key": key})
    header_values.update({"filename": filename})
    header_values.update({"datetime": "10/10/2018"})
    header_values.update({"procedureNo": "1"})
    header_values.update({"type": "Vedios"})
    header_values.update({"Content-Type": "application/octet-stream"})
    return header_values


async def put_request(url, headers, chunk_data):
    async with aiohttp.ClientSession() as session:
        async with session.put(url, headers=headers, data=chunk_data) as response:
            body = await response.text()
            print(f"body = {body}")
            return response

def file_upload_without_chunk(file_path, filename, key):
    url = "https://apimtestprocedure.azure-api.net/echo/uploadFileTest"
    with open(file_path, "rb") as data:
        headers: dict = get_header_value(filename=filename, key=key)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(put_request(url=url, headers=headers, chunk_data=data))
        if response.status != 200:
            print(f"Error sending chunk : {response.text}")


def main():
    # file_path = "C:\\Raja\\Src\\VSCode-win32-x64-1.87.2.zip" #130 MB file
    # file_path = "C:\\Raja\\Src.zip" #4.25 GB MB file
    file_path = "C:\\Raja\\Src\\ppt\\UI mocks predesign.pptx" #8 MB File took 4.15 sec
    # file_path = "C:\\Raja\\Src\\Anaconda3-2024.02-1-Windows-x86_64_988743.exe" #930 MB File took 296.67 Sec
    filename = os.path.basename(file_path)
    subscripion_key = "f42419223b5d493e9837983665bb6a75"
    # file_upload_without_chunk(file_path, filename, subscripion_key)
    asyncio.run(read_large_file(file_path,subscripion_key,filename))


if __name__ == '__main__':
    # asyncio.run(main())
    main()
