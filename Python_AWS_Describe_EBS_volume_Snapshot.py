# how to describe AWS EBS volume Snapshot using boto3 python

import boto3
ec2_boto3=boto3.client("ec2")
ec2_boto3.describe_snapshots(SnapshotIds=['snap-046281ab24d756c50'])