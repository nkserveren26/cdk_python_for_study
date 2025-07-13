from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class NatGatewayConstruct(Construct):
    def __init__(self, scope: Construct, id: str,
                 public_subnet_id: str, private_route_table_id: str):
        super().__init__(scope, id)

        # 1. Elastic IP
        eip = ec2.CfnEIP(self, "NatEIP")

        # 2. NAT Gateway（パブリックサブネットに配置）
        nat_gw = ec2.CfnNatGateway(
            self, "NatGateway",
            allocation_id=eip.attr_allocation_id,
            subnet_id=public_subnet_id,
            tags=[{"key": "Name", "value": "NatGateway"}]
        )

        # 3. プライベートルートテーブルにデフォルトルートを追加
        ec2.CfnRoute(
            self, "PrivateDefaultRoute",
            route_table_id=private_route_table_id,
            destination_cidr_block="0.0.0.0/0",
            nat_gateway_id=nat_gw.ref
        )
