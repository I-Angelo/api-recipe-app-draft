
import os
# from azure.storage.blob import BlobServiceClient
# import string, random, requests
from werkzeug.utils import secure_filename
# from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from flask import Flask, request, redirect
# from azure.storage.blob import PublicAccess
from flask import Blueprint, render_template, request, redirect, url_for, flash



ACCOUNT_NAME = "photoappalbum"
ACCOUNT_KEY = "1Njz9FB2kSEpsmbJWn7/V9FlIlRE4SoB4fPoM/ZiuVUb8BpigdrqCfXu22PNkDpvFtykDQd+C0kC+AStXmD8ww=="
CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=photoappalbum;AccountKey=1Njz9FB2kSEpsmbJWn7/V9FlIlRE4SoB4fPoM/ZiuVUb8BpigdrqCfXu22PNkDpvFtykDQd+C0kC+AStXmD8ww==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "powerapps"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])




site = Blueprint('site', __name__, template_folder = 'site_templates') 

# connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
# blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)



@site.route('/')
def home():
    return render_template('index.html') 

@site.route('/profile')
def profile():
    return render_template('profile.html')


 

@site.route("/album")
def display_images():

    ACCOUNT_NAME = "photoappalbum"
    ACCOUNT_KEY = "1Njz9FB2kSEpsmbJWn7/V9FlIlRE4SoB4fPoM/ZiuVUb8BpigdrqCfXu22PNkDpvFtykDQd+C0kC+AStXmD8ww=="
    CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=photoappalbum;AccountKey=1Njz9FB2kSEpsmbJWn7/V9FlIlRE4SoB4fPoM/ZiuVUb8BpigdrqCfXu22PNkDpvFtykDQd+C0kC+AStXmD8ww==;EndpointSuffix=core.windows.net"
    CONTAINER_NAME = "powerapps"
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])
  

    # blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

    # container_client = blob_service_client.get_container_client(CONTAINER_NAME)

    # blob_list = container_client.list_blobs()

    # blob_list2 = container_client.list_blobs()

    # blobs = [blob.name for blob in blob_list2]

    # blob_urls = [(container_client.url + "/" + blob.name) for blob in blob_list]
    # print(blob_urls)


    # blob_list = []
    # for blob in container_client.list_blobs():
    #     blob_list.append(blob.name)

 

    return render_template("images_album.html")#image_names=image_names, blobs=blobs, blob_list=blob_list

@site.route('/delete', methods=['POST'])
def delete():
    # Retrieve the list of image blobs to delete from the HTML form
    # blobs_to_delete = request.form.getlist('blob')
    

    # blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    
    # for blob_name in blobs_to_delete:
    #     blob_client = blob_service_client.get_blob_client(CONTAINER_NAME, blob_name)
    #     blob_client.delete_blob()
        # blob_service_client.delete_blob('powerapps', blob_name)
    
    # Redirect to the home page
    return redirect('/album')




@site.route('/search-recipes')
def search_recipes():
    # Get the uploaded images from the request
    # images = request.files.getlist('images')

    # Get the container client
    # CONTAINER_NAME = "powerapps"
    # container_client = blob_service_client.get_container_client(CONTAINER_NAME)

    # for image in images:
    #     try:
    #         # Create a BlobClient to upload the image
    #         blob_name = os.path.basename(image.filename)
    #         print(blob_name)
    #         blob_client = container_client.get_blob_client(blob_name)
    #         print(blob_name)

    #         # Upload the image
    #         blob_client.upload_blob(image)
    #     except Exception as e:
                    
                    
            # return    """     <h3>"Ignoring duplicates!!</h3>. """, 5000 
            


    return render_template('search_recipes.html')


@site.route('/update', methods=['PUT'])
def update_images():
    # Get the uploaded images from the request
    # blobs_to_update = request.form.getlist('blob')
    

    # blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    
    # for blob_name in blobs_to_update:
    #     blob_client = blob_service_client.get_blob_client(CONTAINER_NAME, blob_name)
    #     blob_client.delete_blob()
    #     # blob_service_client.delete_blob('powerapps', blob_name)

    #     comment = request.form.get(f'comment_{{blob_name}}')

    #     blob_client.set_blob_metadata(metadata={'comment': comment})
    
    # Redirect to the home page
    return redirect('/album')

