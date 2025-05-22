# commercializeiq-transfer-service

## assets

- cf template: commercializeiq-transfer-ingest
- s3 bucket: commercializeiq-transfer-ingest
- policies: ciq-transfer-ingest
  - ciq-transfer-ingest-iam_role_user_base
  - ciq-transfer-ingest-iam_policy_user_standard
  - ciq-transfer-ingest-iam_role_user_admin
- roles: ciq-transfer-ingest
  - ciq-transfer-ingest-iam_role_user_base
  - ciq-transfer-ingest-iam_role_user_standard
  - ciq-transfer-ingest-iam_role_user_admin
- sns: commercializeiq-transfer-service-sns
  - ciq-transfer-ingest-s3-notification-sns-uploads
  - ciq-transfer-ingest-lambda-sns-handler

## resources

- [Setting up an Amazon API Gateway method as a custom identity provider](https://docs.aws.amazon.com/transfer/latest/userguide/gateway-api-tutorial.html)
- [AWS SFTP Server - Part 3: Password Authentication - Programming with Alex](https://www.youtube.com/watch?v=ZaFIjWg12MI)

---

## to-do

- [x] login
- [x] users
- [x] security for S3
- [WIP] SNS // Email Notifications
- [ ] Web Application Firewall // IP block
- [ ]

---

xoxo,  
_fog_
