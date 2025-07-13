from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class NatGatewayConstruct(Construct):
    def __init__(self, scope: Construct, id: str,
                 public_subnet_ids: list[str],  private_route_table_ids: list[str]):
        super().__init__(scope, id)

        self.nat_gateways = []

        for i, (subnet_id, route_table_id) in enumerate(zip(public_subnet_ids, private_route_table_ids)):
            # Elastic IP
            eip = ec2.CfnEIP(self, f"EIP{i}")

            # NAT Gateway（パブリックサブネットに設置）
            nat_gw = ec2.CfnNatGateway(
                self, f"NATGateway{i}",
                allocation_id=eip.attr_allocation_id,
                subnet_id=subnet_id,
                tags=[{"key": "Name", "value": f"NATGateway-{i}"}]
            )
            self.nat_gateways.append(nat_gw)

            # プライベートRTにデフォルトルート追加（NAT Gateway宛）
            ec2.CfnRoute(
                self, f"PrivateRoute{i}",
                route_table_id=route_table_id,
                destination_cidr_block="0.0.0.0/0",
                nat_gateway_id=nat_gw.ref
            )
