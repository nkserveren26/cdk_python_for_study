import aws_cdk as cdk
from aws_cdk import aws_s3 as s3
from constructs import Construct

class S3BucketConstruct(Construct):
    def __init__(self, scope: Construct, id: str,
                 bucket_name: str,
                 versioned: bool = True,
                 block_public_access: bool = True):
        super().__init__(scope, id)

        self.bucket = s3.Bucket(
            self, "S3Bucket",
            bucket_name=bucket_name,
            versioned=versioned,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL if block_public_access else None,
            removal_policy=cdk.RemovalPolicy.DESTROY,  # 開発中用：本番では RETAIN を検討
            auto_delete_objects=True                   # 上とセット：開発中のみ推奨
        )
