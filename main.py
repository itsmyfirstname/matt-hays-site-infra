#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, S3Backend
from imports.aws.provider import AwsProvider
import os

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        provider = AwsProvider(
            self,
            "default_provider",
            region="us-east-1"
        )

        S3Backend(
            self,
            bucket="mehays-terraform",
            key="main/tfstate",
            region=provider.region,
            access_key=os.getenv("ACCESS_KEY"),
            secret_key=os.getenv("SECRET_KEY")




        )


app = App()
MyStack(app, "matt-hays-site-infra")

app.synth()
