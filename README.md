# snapshotalyzer-3000
demo project to manage AWS EC2 instance snapshot

##cofiguring
shotty uses the configuration file created by the AWS cli

'aws configure --profile shotty'

##Running

'pipenv run python shotty/shotty.py <command> <subcommand> <--project=PROJECT>


*command* is instances, volumes, or snapshots
*subcommand* depends on command
*project* is optional
