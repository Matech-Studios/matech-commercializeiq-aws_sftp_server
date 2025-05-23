import boto3


def lambda_handler(event, context):
    filepath = event["Records"][0]["s3"]["object"]["key"]
    size = event["Records"][0]["s3"]["object"]["size"]
    typeEvent = event["Records"][0]["eventName"]

    client = boto3.client("sns")

    client.publish(
        TargetArn="<<sns_topic_arn>>",
        Message=f'File "{filepath}" has been uploaded to the SFTP server. Event: "{typeEvent}". File size: {size} bytes',
        Subject="SFTP Upload Notification",
    )
