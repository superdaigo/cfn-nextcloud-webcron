# cfn-nextcloud-webcron

This AWS SAM CloudFormation template creates a Lambda function that periodically calls a cron.php on a Nextcloud server.

Ref. https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/background_jobs_configuration.html#webcron

## Cloudformation Parameters

| Parameter   | Description                             | Default Value   |
|-------------|-----------------------------------------|-----------------|
| WebCronUrl  | The URL of the cron.php on your server. | -               |
| WebCronRate | Web cron rate.                          | rate(5 minutes) |


## Setup

You need to setup the following tools.
- AWS CLI
- AWS SAM


The following steps are examples for Mac OS.


### AWS CLI

You have to have AWS CLI to use AWS SAM command.
See also https://brew.sh to install `brew` command.

``` bash
brew install awscli
```


### Configure AWS credentials

Create Access key on AWS console then configure the AWS credentials.

``` bash
aws configure
```

You can check your configuration by executing the following command.

``` bash
aws configure list
```

See more details in the following URL.
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html


### Install AWS SAM

https://aws.amazon.com/serverless/sam/

Example for Mac OS:
``` bash
brew tap aws/tap
brew install aws-sam-cli
```


### Install Pyenv

https://github.com/pyenv/pyenv#installation

``` bash
brew install pyenv pyenv-virtualenv
eval $(pyenv init -)
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
```


### Setup python environment

``` bash
cd cfn-nextcloud-webcron
pyenv install 3.8.5
pyenv virtualenv 3.8.5 cfn-nextcloud-webcron
pyenv local cfn-nextcloud-webcron
```


## Deploy

You'll asked parameters during the `sam deploy --guided` command interactivelly.

``` bash
sam build
sam deploy --guided
```

Here is an example of the `sam deploy --guided` command.
Once you save the config in the file (samconfig.toml by default), all values are stored in the toml file. Then you don't need to use `--guided` option from next time.

``` bash
$ sam deploy --guided

Configuring SAM deploy
======================

        Looking for config file [samconfig.toml] :  Not found

        Setting default arguments for 'sam deploy'
        =========================================
        Stack Name [sam-app]: nextcloud-webcron
        AWS Region [ap-northeast-1]:
        Parameter WebCronUrl []: https://your.nextcloud.server/cron.php
        Parameter WebCronRate [rate(5 minutes)]:
        #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
        Confirm changes before deploy [y/N]: 
        #SAM needs permission to be able to create roles to connect to the resources in your template
        Allow SAM CLI IAM role creation [Y/n]:
        Save arguments to configuration file [Y/n]:
        SAM configuration file [samconfig.toml]:
        SAM configuration environment [default]:

...

Previewing CloudFormation changeset before deployment
======================================================
Deploy this changeset? [y/N]: 

```


### Delete stack

If you don't need the function, you can delete all AWS resources using the following command.
You have to specify the same stack name with `sam deploy` command

``` bash
aws cloudformation delete-stack --stack-name nextcloud-webcron
```


## Development


### Create environment

``` bash
cd cfn-nextcloud-webcron
pyenv install 3.8.5
pyenv virtualenv 3.8.5 cfn-nextcloud-webcron
pyenv local cfn-nextcloud-webcron
pip install -r webcron/requirements.txt
pip install -r tests/requirements.txt
```


### Test

``` bash
python -m pytest tests
```
