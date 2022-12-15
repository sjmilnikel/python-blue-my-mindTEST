# how to describe VPC using Python
import boto3
client=boto3.client("ec2")
# how to describe all VPCs available in your account
x=client.describe_vpcs()
no_of_vpcs=x["Vpcs"]
len(no_of_vpcs)
for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    