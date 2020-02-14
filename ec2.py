import boto3

class XelerateEC2:
        '''This is a class for describing ec2 instances spawned for xelerate deployment'''
        def __init__(self, region):
                self.ec2 = boto3.client('ec2',region)

        def listAll(self):
                return self.ec2.describe_instances()

        def listRunning(self):
                return self.ec2.describe_instances(Filters=[{'Name': 'instance-state-name','Values': ['Running']}])

        def listStopped(self):
                return self.ec2.describe_instances(Filters=[{'Name': 'instance-state-name','Values': ['Stopped']}])

#ec2 = XelerateViewEC2('us-east-1')

