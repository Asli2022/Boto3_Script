import boto3

# Initialize Boto3 EC2 client
ec2_client = boto3.client('ec2')

# Retrieve information about running EC2 instances
response = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)

# Extract the instance IDs of running instances
instance_ids = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

# Terminate running EC2 instances
if instance_ids:
    ec2_client.terminate_instances(InstanceIds=instance_ids)
    print("Terminating the following EC2 instances:")
    for instance_id in instance_ids:
        print(instance_id)
else:
    print("No running EC2 instances found.")