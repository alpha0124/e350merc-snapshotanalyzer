#!/usr/bin/python3
import boto3

if __name__ == '__main__':
    sss = boto3.Session
    s3 = sss.resource('s3')
    sss = boto3.Session()
    s3 = sss.resource('s3')
    for i in s3.buckets.all():
        print (i)
