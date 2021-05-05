# cfn-nextcloud-webcron

## Parameters

| Parameter   | Default Value   | Description                             |
|-------------|-----------------|-----------------------------------------|
| WebCronUrl  | -               | The URL of the cron.php on your server. |
| WebCronRate | rate(5 minutes) | Web cron rate.                          |


## Setup

### AWS CLI

``` bash
brew install awscli
```

### Configure AWS credentials

Create Access key then configure the AWS credentials

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
