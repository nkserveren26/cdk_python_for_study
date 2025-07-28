from aws_cdk import (
    aws_ec2 as ec2,
    aws_rds as rds,
    aws_secretsmanager as secretsmanager,
)

from constructs import Construct

class AuroraClusterConstruct(Construct):

    def __init__(self, scope: 
        Construct, id: str, vpc: ec2.Vpc, **kwargs):
        super().__init__(scope, id, **kwargs)

        # DBクレデンシャルをSecrets Managerで自動生成
        db_credentials = rds.Credentials.from_generated_secret(
            username="admin"
        )

        # セキュリティグループ
        security_group = ec2.SecurityGroup(
            self, "AuroraSecurityGroup",
            vpc=vpc,
            description="Security group for Aurora cluster",
            allow_all_outbound=True
        )

        
        # Aurora クラスターを作成
        self.cluster = rds.DatabaseCluster(
            self, "AuroraCluster",
            engine=rds.DatabaseClusterEngine.aurora_mysql(
                version=rds.AuroraMysqlEngineVersion.VER_3_06_0
            ),
            credentials=db_credentials,
            writer=rds.ClusterInstance.provisioned("writer",instance_type=ec2.InstanceType("t3.medium")),
            default_database_name="mydatabase",
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            security_groups=[security_group]
        )
