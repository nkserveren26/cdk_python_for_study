from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class RouteTableConstruct(Construct):
    def __init__(self, scope: Construct, id: str, vpc_id: str, igw_id: str,
                 public_subnet_ids: list[str], private_subnet_ids: list[str]):
        super().__init__(scope, id)

        # パブリックルートテーブル作成
        self.public_rt = ec2.CfnRouteTable(
            self, "PublicRouteTable",
            vpc_id=vpc_id,
            tags=[{"key": "Name", "value": "PublicRouteTable"}]
        )

        # パブリックルートテーブルにIGWへのルート追加
        ec2.CfnRoute(
            self, "PublicDefaultRoute",
            route_table_id=self.public_rt.ref,
            destination_cidr_block="0.0.0.0/0",
            gateway_id=igw_id
        )

        # パブリックサブネットとルートテーブル関連付け
        for i, subnet_id in enumerate(public_subnet_ids):
            ec2.CfnSubnetRouteTableAssociation(
                self, f"PublicSubnetAssociation{i+1}",
                route_table_id=self.public_rt.ref,
                subnet_id=subnet_id
            )

        # プライベートルートテーブル作成（NAT Gateway経由ルートはここに追加予定）
        self.private_rt = ec2.CfnRouteTable(
            self, "PrivateRouteTable",
            vpc_id=vpc_id,
            tags=[{"key": "Name", "value": "PrivateRouteTable"}]
        )

        # プライベートサブネットとルートテーブル関連付け
        for i, subnet_id in enumerate(private_subnet_ids):
            ec2.CfnSubnetRouteTableAssociation(
                self, f"PrivateSubnetAssociation{i+1}",
                route_table_id=self.private_rt.ref,
                subnet_id=subnet_id
            )
