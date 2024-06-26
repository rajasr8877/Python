import datetime
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
from requests import PreparedRequest


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

def get_date_value():
    d1 = datetime.date(year = 2018, month = 7, day = 12)
    d1  = d1.strftime("%m/%d/%Y")
    return d1

def get_url_with_query_params(url:str, params:dict):
    req = PreparedRequest()
    req.prepare_url(url, params)
    print(req.url)
    return req.url


def get_header_value(key: str, filename: str):
    header_values = dict()
    header_values.update({"Ocp-Apim-Subscription-Key": key})
    header_values.update({"filename": filename})
    header_values.update({"datetime": get_date_value()})
    header_values.update({"Content-Type": "application/octet-stream"})
    return header_values


def put_block_list_api_call(url, block_list, filename, key):
    data = xml_data_of_blocklist(block_list)
    print(data)
    headers = get_header_value(filename=filename, key=key)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # response = loop.run_until_complete(put_request(url, headers=headers, chunk_data=value))
    response = loop.run_until_complete(put_request_res(url, headers=headers, chunk_data=data))
    if response.response.statusCode != 200:
        print(f"Error sending remaining chunk: {response.response.statusCode}")
        print(response)
        print(response.response.message)

def api_call_method(url, data, headers):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # response = loop.run_until_complete(put_request(url, headers=headers, chunk_data=value))
    response = loop.run_until_complete(put_request_res(url, headers=headers, chunk_data=data))
    return response


# Open the file in binary mode
def file_upload(file_path, filename, key):
    url = "https://apimtestprocedure.azure-api.net/echo/uploadChunk"
    putBlockListurl = "https://apimtestprocedure.azure-api.net/echo/putBlockList"
    start_time = time.time()
    print(f"Start Time ============= {start_time}")
    with open(file_path, "rb") as f:
        # Get the file size
        file_size = os.path.getsize(file_path)
        print(file_size)
        # Send the first chunk (100 MB)
        chunk_size = 4 * 1024 * 1024
        block_list = []
        for i in range(0, file_size, chunk_size):
            print(f"for loop {i}")
            chunk =  f.read(chunk_size)
            blk_id = str(uuid.uuid4())
            headers: dict = get_header_value(filename=filename, key=key)
            headers.update({"blockId": blk_id})
            # headers.update({"Content-Range": f"bytes {i}-{i + chunk_size - 1}/{file_size}"})
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            # # response = loop.run_until_complete(put_request(url=url, headers=headers, chunk_data=chunk))
            response = loop.run_until_complete(put_request_res(url=url, headers=headers, chunk_data=chunk))
            # response = api_call_method(url, chunk, headers)
            if response.response.statusCode != 200:
                print(response)
                print(f"Error sending chunk {i}: {response.response.message}")
                break
            block_list.append(BlobBlock(block_id=blk_id))

        # Send the remaining chunk (if any)
        print(f"Print i value {i}: and file_size == {file_size}")
        # if i < file_size:
        #     chunk =  f.read(file_size - i)
        #     # blk_id = str(uuid.uuid4())
        #     headers: dict = get_header_value(filename=filename, key=key)
        #     headers.update({"blockId": blk_id})
        #     headers.update({"Content-Range": f"bytes {i}-{i + chunk_size - 1}/{file_size}"})
        #     loop = asyncio.new_event_loop()
        #     asyncio.set_event_loop(loop)
        #     response = loop.run_until_complete(put_request(url=url, headers=headers, chunk_data=chunk))
        #     # block_list.append(BlobBlock(block_id=blk_id))
        #     if response.status != 201:
        #         print(f"Error sending remaining chunk: {response.status}")
        #         print(f"Error sending chunk {i}: {response.text}")
        # blk_id_temp = str(uuid.uuid4())
        # block_list.append(BlobBlock(block_id=blk_id_temp))
        put_block_list_api_call(putBlockListurl, block_list, filename, key)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Upload complete. Time duration: {duration} seconds.")



def main():
    # file_path = "C:\\Raja\\Src\\VSCode-win32-x64-1.87.2.zip" #130 MB file
    # file_path = "C:\\Raja\\Src.zip" #4.25 GB MB file
    file_path = "C:\\Raja\\Src\\ppt\\MasterTables_Design__.pdf" #8 MB File took 4.15 sec
    # file_path = "C:\\Raja\\Src\\Anaconda3-2024.02-1-Windows-x86_64_988743.exe" #930 MB File took 296.67 Sec
    filename = os.path.basename(file_path)
    subscripion_key = "f42419223b5d493e9837983665bb6a75"
    file_upload(file_path, filename, subscripion_key)


if __name__ == '__main__':
    # asyncio.run(main())
    main()