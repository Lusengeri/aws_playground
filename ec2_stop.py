
# We import the 'boto3' library which is the Python AWS SDK

import boto3

# We then connect to the 'ec2' service

#ec2 = boto3.client('ec2',
#                   ap-south-1',
#                   aws_access_key_id='',
#                   aws_secret_access_key='')

ec2 = boto3.client('ec2')

all_instances = ec2.describe_instances()
    
instance_ids = []

# find instance-id based on instance name
# many for loops but should work
for reservation in all_instances['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

#first_instance_id = instance_ids[0]

print("Stopping Instances: ", instance_ids)

ec2.stop_instances(InstanceIds=instance_ids)

print("Instances stopped")
