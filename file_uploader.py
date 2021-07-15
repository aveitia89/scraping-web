from minio import Minio
from minio.error import S3Error


def file_upload(file_img, object_name):
    client = Minio(
        endpoint="localhost:9001",
        access_key="administrador",
        secret_key="admin123",
        secure=False
    )
    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists("vanguardia")
    if not found:
        client.make_bucket("vanguardia")
    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
    client.fput_object(
        "vanguardia", object_name, file_img,
    )
    return True
