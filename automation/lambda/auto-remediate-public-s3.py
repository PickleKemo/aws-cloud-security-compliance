import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        acl = s3.get_bucket_acl(Bucket=bucket)
        for grant in acl['Grants']:
            if grant['Grantee'].get('URI', '') == 'http://acs.amazonaws.com/groups/global/AllUsers':
                s3.put_bucket_acl(Bucket=bucket, ACL='private')
                print(f"Remediated public S3 bucket: {bucket}")
    return {"status": "complete"}