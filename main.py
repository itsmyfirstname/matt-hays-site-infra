#!/usr/bin/env python
from os import name
from constructs import Construct
from cdktf import App, TerraformStack, S3Backend
from imports.aws.provider import AwsProvider
from imports.aws.s3_bucket import S3Bucket


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        provider = AwsProvider(
            self,
            "AWS",
            region="us-east-1",
            profile="mehays-deployer"
        )
        
        S3Backend(
            self,
            bucket="mehays-terraform",
            key="main/tfstate",
            encrypt=True,
            region=provider.region,
            profile="mehays-deployer",
        )

        site_bucket = S3Bucket(
            self,
            "site",
            bucket="matthays.dev"
        )

        #TODO: Decide how to build and publish the site
        #TODO: Config parser with "envs" deploying to different buckets
app = App()
MyStack(app, "matt-hays-site-infra")

app.synth()
