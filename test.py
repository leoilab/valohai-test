from boto3 import client

print("Hello!")

client = client('s3')
for key in client.list_objects_v2(Bucket='leo-platform-images-staging', Prefix='imagine/')['Contents']:
    print(key['Key'])
object = client.get_object(Bucket='leo-platform-images-staging', Key='imagine/17d8889b-8698-49b7-b626-49306aa062ec')
print(object)
