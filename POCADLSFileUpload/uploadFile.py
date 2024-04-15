
import base64
import time
from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import os
import requests
import yaml
import uuid
import aiohttp
import asyncio
import aiofiles

from azure.storage.blob import ContainerClient, BlobBlock, BlobServiceClient, BlobClient
# app = Flask(__name__)

# SWAGGER_URL = "/swagger"
# API_URL = "/static/swagger.json"

# swagger_ui_blueprint = get_swaggerui_blueprint(base_url=SWAGGER_URL, api_url=API_URL, config={
#     'app_name': 'Azure Function Procedure Access API'
# })

# app.register_blueprint(blueprint=swagger_ui_blueprint, url_prefix=SWAGGER_URL)


# def load_config():
#     dir_root =os.path.dirname(os.path.abspath(__file__))
#     with open(dir_root +"/config.yaml","r") as yamlfile:
#         return yaml.load(yamlfile,Loader=yaml.FullLoader)


# def dummy():
#     print("Executing the dummy")

# @app.route('/upload', methods=['POST'])
# def uoload_file():
#     if 'media' not in request.files:
#         return jsonify({'error': 'No media file provided'}), 400

#     media_file = request.files['media']
#     media_data = base64.b64encode(media_file.read()).decode('utf-8')

#     print(media_file)
#     print(media_data)


#     media_path = os.path.join(directory, media_file.filename)
#     print(media_path)
#     with open(media_path, 'wb') as f:
#         f.write(media_file.read())
#     return jsonify({'message': 'Media file uploaded successfully', 'media': media_data}), 200


# config = load_config();
# print(* config)
# dummy()


def get_header_value(key: str, filename: str):
    header_values = dict()
    header_values.update({"Ocp-Apim-Subscription-Key": key})
    header_values.update({"filename": filename})
    # header_values.update({"Content-Type": "multipart/form-data"})
    return header_values


async def put_request(url, headers, file_path):
    async with aiohttp.ClientSession(headers=headers) as session:
        with open(file_path, 'rb') as file:
            async with session.put(url, data=file) as response:
                return response


def apim_request_to_upload(url: str, file_path: str, key: str):
    file_name = os.path.basename(file_path)
    print(file_name)
    header_values = get_header_value(key, file_name)
    start_time = time.time()
    print(f"Start Time ============= {start_time}")
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(put_request(url, header_values, file_path))
    end_time = time.time()
    duration = end_time - start_time
    print(f"Upload complete. Time duration: {duration} seconds.")
    # Check the response status
    if response.status == 201:
        print("File uploaded successfully")
    else:
        print("Failed to upload file:", response.text)


# async def handle_file_upload_2(file_path,headers, filename):
#     async with aiofiles.open(file_path, mode='rb') as f:
#         file_content = await f.read()
#     print(filename)
#     chunk_size = 4096
#     chunks = (file_content[i:i + chunk_size] for i in range(0, len(file_content), chunk_size))
#     print(chunks)
#     async with aiohttp.ClientSession(headers=headers) as session:
#         for i, chunk in enumerate(chunks):
#             async with session.put(f'https://apimtestprocedure.azure-api.net/echo/upload?blockId={i}', data=aiohttp.ByteStream(chunk)) as response:
#                 response.raise_for_status()
#     return aiohttp.web.Response(text=f"File {filename} uploaded successfully")


# async def handle_upload(file_path, header_values, filename):
#     try:
#         response = await handle_file_upload_2(file_path, header_values, filename)
#         return response
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return aiohttp.web.Response(text="File upload failed")

# def read_in_chunks(file_object, chunk_size=1024):
#     while True:
#         data = file_object.read(chunk_size)
#         if not data:
#             break
#         yield data


# def upload_large_file(url, file_path):
#     file_name = os.path.basename(file_path)
#     print(file_name)
#     start_time = time.time()
#     print(f"Start Time ============= {start_time}")
#     header_values = get_header_value("f42419223b5d493e9837983665bb6a75", file_name)
#     with open(file_path, 'rb') as file_obj:
#         for file_chunk in read_in_chunks(file_obj):
#             files = {'file': file_chunk}
#             response = requests.put(url, headers=header_values, files=files)
#     end_time = time.time()
#     duration = end_time - start_time
#     print(f"Upload complete. Time duration: {duration} seconds.")


# async def put_request_2(url, header_values, read_data, block_id):
#     async with aiohttp.ClientSession(headers=header_values) as session:
#         url = f"{url}?blockId={block_id}"
#         async with session.put(url, data=read_data) as response:
#             return response
        
# def file_upload_chunks(filepath,url,header_values):
#     block_list=[]
#     chunk_size=1024*1024*4 
#     with open(filepath,'rb') as f:
#         while True:
#             read_data = f.read(chunk_size)
#             print("Print Read data")
#             # print(read_data)
#             if not read_data:
#                 break # done
#             blk_id = str(uuid.uuid4())
#             # ApI Call
#             start_time = time.time()
#             print(f"Start Time ============= {start_time}")
#             loop = asyncio.get_event_loop()
#             response = loop.run_until_complete(put_request_2(url, header_values, read_data, blk_id))
#             end_time = time.time()
#             duration = end_time - start_time
#             print(f"Upload complete. Time duration: {duration} seconds.")
#             # Check the response status 
#             if response.status == 201:
#                 print("File uploaded successfully")
#             else:
#                 print("Failed to upload file:", response.text)
#             block_list.append(BlobBlock(block_id=blk_id))

# Handle the response as needed (e.g., check status code, etc.)# Example usage:
if __name__ == '__main__':
    url = "https://apimtestprocedure.azure-api.net/echo/upload"
    # url = "https://apimtestprocedure.azure-api.net/echo/uploadChunk"
    file_path = "C:\\Raja\\Src\\ppt\\UI mocks predesign.pptx"
    # file_path = "C:\\Raja\\Src.zip"
    filename = os.path.basename(file_path)
    print(filename)
    subscripion_key = "f42419223b5d493e9837983665bb6a75"
    # header_values = get_header_value(subscripion_key, filename)
    # header_values = dict()
    # header_values.update({"Ocp-Apim-Subscription-Key": subscripion_key})
    # header_values.update({"filename": filename})
    # upload_large_file(url, file_path)
    # file_upload_chunks(file_path, url, header_values)
    apim_request_to_upload(url=url, file_path=file_path, key=subscripion_key)
