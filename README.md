# Overview
TBD

## Setup

### initialize project
When creating the project initially, be sure to begin with a _local_ backend, if an AWS backend is desired. 
>`cdktf init --template="python" --local`


### provider install
add desired providers to `cdktf.json` and execute to install
>`cdktf get`

### migrate state
Now that providers are handy, add in a remote state configuration.

```python
S3Backend(
    self,
    bucket="bucket-name",
    key="path/to/tfstate",
    encrypt=True,
    region=provider.region,
    profile=provider.profile
)
```

1. run `cdktf synth`
2. then `cdktf deploy`

