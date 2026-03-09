import boto3

s3 = boto3.client("s3")
s3.upload_file("pytest-report.xml", "cloud-api-automation-tests-bucket", "pytest-report.xml")
s3.upload_file("pytest-results.txt", "cloud-api-automation-tests-bucket", "pytest-results.txt")

print("Upload successful!")[201~.


import boto3

s3 = boto3.client("s3")
s3.upload_file("pytest-report.xml", "cloud-api-automation-tests-bucket", "pytest-report.xml")
s3.upload_file("pytest-results.txt", "cloud-api-automation-tests-bucket", "pytest-results.txt")

print("Upload successful!")
