# how to delete VPC with Python
import boto3
client=boto3.client("ec2")
response = client.delete_vpc(
    VpcId='vpc-055b36094b145a9f5'
)
