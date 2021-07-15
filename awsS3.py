import logging
import requests
import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = 'reactvang'


def upload_file(file_name, object_name=None, bucket = BUCKET_NAME):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name) if type(file_name) == str else s3_client.upload_fileobj(file_name, BUCKET_NAME, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def list_bucket_objects():
    # # Create a client
    # client = boto3.client('s3', region_name='us-west-2')

    # # Create a reusable Paginator
    # paginator = client.get_paginator('list_objects')

    # # Create a PageIterator from the Paginator
    # page_iterator = paginator.paginate(Bucket='my-bucket')

    # for page in page_iterator:
    #     print(page['Contents'])
    s3 = boto3.resource('s3')
    bucket_objects = s3.Bucket(name=BUCKET_NAME).objects.all()
    for bucket in bucket_objects:
        print(bucket)
        # delete_bucket_object(bucket.key)

def delete_bucket_object(key):
    s3 = boto3.resource('s3')
    s3.Object(BUCKET_NAME, key).delete()

def downloand(url="https://vanguardia.com.mx/sites/default/files/styles/paragraph_image_large_desktop_1x/public/amlo-pemex-lopez-obrador-plan-nacional-gas-petroleo-gob-mx.jpg_114089499.jpg"):
    return requests.get(url, stream=True, headers={'User-agent': 'Mozilla/5.0'})

# img_raw = downloand().raw
# img = img_raw.read()
# s3 = boto3.resource('s3')
# s3.Bucket(name=BUCKET_NAME).put_object(Key="amloq.jpg", Body=img)
# upload_file(img_raw, BUCKET_NAME, "DIRECTORY/THAT/YOU/WANT/TO/CREATE/amloqe.jpg",)
# delete_bucket_object("amlo.jpg")
# list_bucket_objects()
# s3 = boto3.client('s3')
# s3.download_file(BUCKET_NAME, 'amlo.jpg', 'amlo.jpg')