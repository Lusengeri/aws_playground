# We import the 'boto3' library which is the Python AWS SDK

import boto3

# We then connect to the 'ec2' service

#ec2 = boto3.client('ec2',
#                   ap-south-1',
#                   aws_access_key_id='',
#                   aws_secret_access_key='')

ec2 = boto3.client('ec2')

conn = ec2.run_instances(InstanceType="t2.micro", MaxCount=1, MinCount=1, ImageId="ami-0dd0ccab7e2801812")

print(conn)
