from constructs import Construct
from aws_cdk import aws_ec2 as ec2

class SubnetConstruct(Construct):
    def __init__(self, scope: Construct, id: str, vpc_id: str, azs: list[str]):
        super().__init__(scope, id)

        self.public_subnets = []
        self.private_subnets = []

        for i, az in enumerate(azs):
            public_subnet = ec2.CfnSubnet(
                self, f"PublicSubnet{i+1}",
                vpc_id=vpc_id,
                cidr_block=f"10.0.{i}.0/24",
                availability_zone=az,
                map_public_ip_on_launch=True,
                tags=[{"key": "Name", "value": f"PublicSubnet-{az}"}]
            )
            self.public_subnets.append(public_subnet)

            private_subnet = ec2.CfnSubnet(
                self, f"PrivateSubnet{i+1}",
                vpc_id=vpc_id,
                cidr_block=f"10.0.{i+10}.0/24",
                availability_zone=az,
                map_public_ip_on_launch=False,
                tags=[{"key": "Name", "value": f"PrivateSubnet-{az}"}]
            )
            self.private_subnets.append(private_subnet)
