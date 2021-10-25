import os
import json

import boto3

from starpipe.database_reader import get_datawarehouse_database_hostname, get_database_connection


sm = boto3.client("secretsmanager", region_name='eu-central-1')

secret_id = "arn:aws:secretsmanager:eu-central-1:500476720534:secret:valohai/valohai-datawarehouse-password-Ut3TUl"

secret = json.loads(sm.get_secret_value(SecretArn=secret_id)["SecretString"])
os.environ["DATAWAREHOUSE_USERNAME"] = secret["username"]
os.environ["DATAWAREHOUSE_PASSWORD"] = secret["password"]

host = get_datawarehouse_database_hostname()
con = get_database_connection(host, "backbone_raw")
cursor = con.cursor()
cursor.execute("SELECT count(`case`.id) from `case`")
result, *_ = cursor.fetchone()

print('----- Hello from dw -------')
print(result)
print()
print('----- Hello from imagine bucket -----')
print(boto3.client("s3").list_objects(Bucket='leo-platform-images-staging', Prefix='imagine/', MaxKeys=1))
