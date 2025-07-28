from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from lib.my_constructs.network.nat_gateway_construct import NatGatewayConstruct
from lib.my_constructs.network.route_table_construct import RouteTableConstruct
from lib.my_constructs.network.subnet_construct import SubnetConstruct
from lib.my_constructs.network.vpc_construct import VpcConstruct
from lib.my_constructs.storage.s3_bucket_construct import S3BucketConstruct
from lib.my_constructs.storage.aurora_construct import AuroraClusterConstruct

class CdkPythonForStudyStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        vpc = VpcConstruct(self, "TestVPC")

        '''
        azs = self.availability_zones[:2]  # 最初の2つのAZを取得
        subnet = SubnetConstruct(self, "TestSubnet", vpc.vpc.ref, azs)

        igw_id = vpc.igw.ref

        route_table = RouteTableConstruct(
            self,
            "RouteTableConstruct",
            vpc_id=vpc.vpc.ref,
            igw_id=igw_id,
            public_subnet_ids=[s.ref for s in subnet.public_subnets],
            private_subnet_ids=[s.ref for s in subnet.private_subnets]
        )
        '''

        '''
        
        nat_gateway = NatGatewayConstruct(
            self,
            "NatGatewayConstruct",
            public_subnet_ids=[s.ref for s in subnet.public_subnets],
            private_route_table_ids=[r.ref for r in route_table.private_route_tables]
        )
        '''

        bucket_construct = S3BucketConstruct(
            self,
            "MyAppBucket",
            bucket_name="myapp-sample-bucket-123456",
            versioned=True,
            block_public_access=True
        )

        aurora_construct = AuroraClusterConstruct(
            self,
            "Aurora",
            vpc=vpc.vpc
        )
