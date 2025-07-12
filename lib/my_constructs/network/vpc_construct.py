from constructs import Construct
from aws_cdk import aws_ec2 as ec2

class VpcConstruct(Construct):
    def __init__(self, scope: Construct, id: str, *, cidr: str = "10.0.0.0/16"):
        super().__init__(scope, id)

        self.vpc = ec2.CfnVPC(
            self, "MyVPC",
            cidr_block=cidr,
            enable_dns_support=True,
            enable_dns_hostnames=True,
            tags=[{"key": "Name", "value": "MyVPC"}]
        )

        self.igw = ec2.CfnInternetGateway(
            self, "MyIGW",
            tags=[{"key": "Name", "value": "MyIGW"}]
        )

        ec2.CfnVPCGatewayAttachment(
            self, "IGWAttachment",
            vpc_id=self.vpc.ref,
            internet_gateway_id=self.igw.ref
        )
