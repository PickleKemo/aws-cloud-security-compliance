import boto3

def list_iam_users():
    iam = boto3.client('iam')
    users = iam.list_users()
    for user in users['Users']:
        print(f"User: {user['UserName']} - Created: {user['CreateDate']}")

if __name__ == '__main__':
    list_iam_users()