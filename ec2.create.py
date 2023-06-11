import boto3

# Initialize Boto3 EC2 resource
ec2_resource = boto3.resource('ec2')

# Define the parameters for creating the EC2 instance
image_id = 'ami-04a0ae173da5807d3'  # Replace with your desired AMI ID
instance_type = 't2.micro'
security_group_ids = ['sg-04f804a48e8dab7cb']  # Replace with your desired security group IDs
subnet_id = 'subnet-036a75425d808a4cc'  # Replace with your desired subnet ID
instance_name = 'Python EC2'  # Replace with the desired name for the EC2 instance


# Create the EC2 instance
instance = ec2_resource.create_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    SecurityGroupIds=security_group_ids,
    SubnetId=subnet_id,
    MinCount=1,
    MaxCount=1
)[0]  # Take the first instance from the returned list

# Add a name tag to the EC2 instance
instance.create_tags(
    Tags=[
        {'Key': 'Name', 'Value': instance_name}
    ]
)

# Print the ID and Name of the created instance
print("EC2 instance created with ID:", instance.id)
print("Instance Name:", instance_name)




