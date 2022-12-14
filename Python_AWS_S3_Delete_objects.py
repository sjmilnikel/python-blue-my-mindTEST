import boto3
#delete single object

s3_resource=boto3.client("s3")
s3_resource.delete_object(Bucket='totaltecho1',
Key='aws-cert.png')


#delete multiple objects
import os
import glob
#find all the objects from the bucket
objects=s3_resource.list_objects(Bucket="totaltecho1")["Contents"]

#iteration
for object in objects:
    s3_resource.delete_object(Bucket='totaltecho1',
    Key=object["Key"])
    
    