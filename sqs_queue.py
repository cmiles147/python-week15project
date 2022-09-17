#Create an SQS Queue

import boto3

sqs = boto3.client('sqs')
response = sqs.create_queue(
    QueueName='week15-queue',
)

print(response)



#Send message to SQS queue from lambda function

import json
from datetime import datetime


def lambda_handler(event, context):
    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y %H:%M:%S")
    
    sqs = boto3.client('sqs')
    
    response = sqs.send_message(
        QueueUrl= 'https://queue.amazonaws.com/134733923762/week15-queue',
        MessageBody= date_time,
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent!')
    }
