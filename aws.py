import boto3
import boto3.session
import threading

class MyTask(threading.Thread):
    def run(self):
        session = boto3.session.Session()
        s3 = session.resource('s3')
        # ... do some work with S3 ...


# S3 list all keys with the prefix 'photos/'
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    for obj in bucket.objects.filter(Prefix='photos/'):
        print('{0}:{1}'.format(bucket.name, obj.key))

def list_bucket():
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

# Upload a new file
data = open('test.jpg', 'rb')
s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)

