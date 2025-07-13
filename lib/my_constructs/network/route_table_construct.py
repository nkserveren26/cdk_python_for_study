from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class RouteTableConstruct(Construct):
    def __init__(self, scope: Construct, id: str, vpc_id: str, igw_id: str,
                 public_subnet_ids: list[str], private_subnet_ids: list[str]):
        super().__init__(scope, id)

        self.public_route_tables = []
        self.private_route_tables = []

        # 各パブリックサブネットに対してルートテーブル作成 + IGWルート追加 + 紐付け
        for i, subnet_id in enumerate(public_subnet_ids):
            rt = ec2.CfnRouteTable(
                self, f"PublicRouteTable{i}",
                vpc_id=vpc_id,
                tags=[{"key": "Name", "value": f"PublicRouteTable{i}"}]
            )
            self.public_route_tables.append(rt)

            ec2.CfnRoute(
                self, f"PublicDefaultRoute{i}",
                route_table_id=rt.ref,
                destination_cidr_block="0.0.0.0/0",
                gateway_id=igw_id
            )

            ec2.CfnSubnetRouteTableAssociation(
                self, f"PublicSubnetAssociation{i}",
                route_table_id=rt.ref,
                subnet_id=subnet_id
            )

        # 各プライベートサブネットに対してルートテーブル作成 + 紐付け
        for i, subnet_id in enumerate(private_subnet_ids):
            rt = ec2.CfnRouteTable(
                self, f"PrivateRouteTable{i}",
                vpc_id=vpc_id,
                tags=[{"key": "Name", "value": f"PrivateRouteTable{i}"}]
            )
            self.private_route_tables.append(rt)

            ec2.CfnSubnetRouteTableAssociation(
                self, f"PrivateSubnetAssociation{i}",
                route_table_id=rt.ref,
                subnet_id=subnet_id
            )
