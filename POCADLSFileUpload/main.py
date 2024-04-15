
import base64
import logging
import time
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
import os
import yaml
import uuid

from azure.storage.blob import ContainerClient,BlobBlock,BlobServiceClient,BlobClient
# app = Flask(__name__)

# SWAGGER_URL = "/swagger"
# API_URL = "/static/swagger.json"

# swagger_ui_blueprint = get_swaggerui_blueprint(base_url=SWAGGER_URL, api_url=API_URL, config={
#     'app_name': 'Azure Function Procedure Access API'
# })

# app.register_blueprint(blueprint=swagger_ui_blueprint, url_prefix=SWAGGER_URL)


def load_config():
    dir_root =os.path.dirname(os.path.abspath(__file__))
    with open(dir_root +"/config.yaml","r") as yamlfile:
        return yaml.load(yamlfile,Loader=yaml.FullLoader)


def get_files(dir):
    with os.scandir(dir) as entires:
        for entry in entires:
            if entry.is_file() and not entry.name.startswith('.'):
                yield entry

# def get_files(dir):
#     return (entry for entry in os.scandir(dir) if entry.is_file() and not entry.name.startswith('.'))


def upload(files, connection_string, container_name):
    container_client = ContainerClient.from_connection_string(
        conn_str=connection_string, container_name=container_name)
    print("Upload in progress ********************* ")
    for file in files:
        if file.is_file():
            print("uploading the file of ********* "+ file.name)
            blob_client = container_client.get_blob_client(file.name)
            with open(file.path, "rb") as data:
                blob_client.upload_blob(data)
                print(f'file {file.name} upload compleded')


def dummy():
    print("Executing the dummy")

# @app.route('/upload', methods=['POST'])
# def home():
#     if 'media' not in request.files:
#         return jsonify({'error': 'No media file provided'}), 400

#     media_file = request.files['media']
#     media_data = base64.b64encode(media_file.read()).decode('utf-8')

#     print(media_file)
#     print(media_data)

#     # Save the media file to the server
#     directory  ="C:\Raja\Olympus\Dev\Workspace\Python\Azure\FunctionAppDemo\media"
#     if not os.path.exists(directory):
#         print("Yes available")
    
    # media_path = os.path.join(directory, media_file.filename)
    # if not os.path.exists(media_path):
    #     os.makedirs(media_path)

    # print(media_path)
    # with open(media_path, 'wb') as f:
    #     f.write(media_file.read())
    # return jsonify({'message': 'Media file uploaded successfully', 'media': media_data}), 200


def upload_multiple_files_using_chunck(self, directory_path, container_name):
    """
    Upload all files in a directory to an Azure Blob Storage container.
    """
    container_client = self.blob_service_client.get_container_client(container_name)

    # Get a list of all files in the directory
    files = list(get_files(directory_path))

    # Upload each file to the container
    for file in files:
        blob_file_path = file.name
        local_file_path = file.path
        print(f"Uploading {local_file_path} to {container_name}...")
        upload_file_chunks(container_client, blob_file_path, local_file_path)
        print(f"Uploaded {local_file_path} to {container_name}.")

def upload_file_chunks(container_client,blob_file_path,local_file_path):
    '''
    Upload large file to blob
    '''

    try:
        blob_client = container_client.get_blob_client(blob_file_path)
        print(f"Uploading {local_file_path} to Azure Blob container...")
        start_time = time.time()
        # upload data
        block_list=[]
        chunk_size=1024*1024*4
        with open(local_file_path,'rb') as f:
            while True:
                read_data = f.read(chunk_size)
                if not read_data:
                    break # done
                blk_id = str(uuid.uuid4())
                blob_client.stage_block(block_id=blk_id,data=read_data) 
                block_list.append(BlobBlock(block_id=blk_id))
        blob_client.commit_block_list(block_list)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Uploaded {local_file_path} to Azure Blob container...")
        print(f"Upload complete. Time duration: {duration} seconds.")
    except BaseException as err:
        print('Upload file error')
        print(err)




config = load_config();
# print(* config)

filesList = list(get_files(config["source_folder"]+"/ppt"))
# upload(filesList, config["azure_storage_connectionstring"],config["files_container_name"])

connection_string = config["azure_storage_connectionstring"]
container_name = config["files_container_name"]
# print("con String **** "+connection_string)
# print("container_name **** "+container_name)
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)

blob_file_path = "Src.zip"
local_file_path = "C:\\Raja\\Src.zip"
# local_file_path = "C:\\Raja\\Src\ppt\\UI mocks predesign.pptx"
upload_file_chunks(container_client,blob_file_path=blob_file_path,local_file_path=local_file_path)



# if __name__ == '__main__':
#     app.run(debug=True)