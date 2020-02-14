import boto3
import json


class XelerateEKS:
        '''This is a class for describing EKS cluster spawned for xelerate deployment'''
        def __init__(self, region):
                self.eks = boto3.client('eks')
		self.eksClusterName = ''
		self.eksNodeGroups = []

        def listAll(self):
                return self.eks.list_clusters()


        def listNodeGroups(self, cluster_name):
                return self.eks.list_nodegroups(clusterName=cluster_name)


        def describeNodeGroup(self, cluster_name, nodegroup_name):
                return self.eks.describe_nodegroup(clusterName=cluster_name,nodegroupName=nodegroup_name)


	def populate(self, cluster_name):
		self.eksClusterName = cluster_name
		for nodeGroup in self.listNodeGroups(cluster_name)['nodegroups']:
				self.eksNodeGroups.append(self.describeNodeGroup(cluster_name,nodeGroup))


#eks = XelerateEKS('us-east1')
#eksClusters = eks.listAll()
#for cluster in eksClusters['clusters']:
#	eks.populate(cluster)
#	print(eks.eksNodeGroups)

