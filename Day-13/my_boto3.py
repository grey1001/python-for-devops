import boto3
client = boto3.client('s3')
response = client.list_buckets()    

for bucket_names in response['Buckets']:
    if bucket_names['Name'] == 'abiwon-bucket':
        response = client.delete_bucket(
            Bucket='abiwon-bucket'
        )
        print(response)
    else:
        print(bucket_names['Name'])