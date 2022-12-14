import boto3
#how to upload single file

s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="aws-certified-developer-associate.png", #replace with your file name
    Bucket="totaltecho1", #replace with your bucket name
    Key="aws-cert.png") #replace with your new file name

#how to upload multiple files
import os
import glob
cwd=os.getcwd()
cwd=cwd+"/multiple_files/" #replace with your folder name
files=glob.glob(cwd+"*.png")

for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="totaltecho1", 
    Key=file.split("/")[-1])


