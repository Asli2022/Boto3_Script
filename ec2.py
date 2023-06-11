import boto3
import csv

# Initialize Boto3 EC2 client
ec2_client = boto3.client('ec2')

# Retrieve information about EC2 instances
response = ec2_client.describe_instances()

# Extract instance name and type
data = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_name = instance.get('Tags', [{'Key': 'Name', 'Value': 'N/A'}])[0]['Value']
        instance_type = instance['InstanceType']
        data.append([instance_name, instance_type])

# Write data to CSV file
with open('ec2_instances.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Instance Name', 'Instance Type'])
    writer.writerows(data)

print("CSV file 'ec2_instances.csv' created successfully.")
