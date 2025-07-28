from constructs import Construct
from aws_cdk import aws_ec2 as ec2

class VpcConstruct(Construct):
    def __init__(self, scope: Construct, id: str, *, cidr: str = "10.0.0.0/16"):
        super().__init__(scope, id)
        self.vpc = ec2.Vpc(
            self, "MyVpc",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=24),
                ec2.SubnetConfiguration(name="private", subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS, cidr_mask=24),
            ]
        )
