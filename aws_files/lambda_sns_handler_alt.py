import boto3


def lambda_handler(event, context):
    filepath = event["Records"][0]["s3"]["object"]["key"]
    size = event["Records"][0]["s3"]["object"]["size"]
    typeEvent = event["Records"][0]["eventName"]

    client = boto3.client("sns")

    client.publish(
        TargetArn="arn:aws:sns:us-east-2:841344318949:commercializeiq-transfer-service-sns",
        Message=f'File "{filepath}" has been "{typeEvent}" (event). File size: {size} bytes',
        Subject="SFTP Upload Notification",
    )
