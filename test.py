import os
import json

import boto3

from starpipe.database_reader import get_datawarehouse_database_hostname, get_database_connection


sm = boto3.client("secretsmanager", region_name='eu-central-1')

secret_id = "arn:aws:secretsmanager:eu-central-1:500476720534:secret:valohai/valohai-datawarehouse-password-Ut3TUl"

secret = json.loads(sm.get_secret_value(SecretId=secret_id)["SecretString"])
os.environ["DATAWAREHOUSE_USERNAME"] = secret["username"]
os.environ["DATAWAREHOUSE_PASSWORD"] = secret["password"]

print('----- Hello from dw -------')
host = get_datawarehouse_database_hostname()
con = get_database_connection(host, "backbone_raw")
cursor = con.cursor()
query = "SELECT count(`case`.id) from `case`"
cursor.execute(query)
result, *_ = cursor.fetchone()
print(f'{query} = ', result)

print()

print('----- Hello from imagine bucket -----')
summary, *_ = boto3.client("s3").list_objects(Bucket='leo-platform-images-staging', Prefix='imagine/', MaxKeys=1)['Contents']
o = boto3.client('s3').get_object(Bucket='leo-platform-images-staging', Key=summary['Key'])
print(summary)
print(o)
