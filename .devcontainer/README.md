# Development Container for Strands Agents Demo

This directory contains configuration files for setting up a development container for the Strands Agents Demo project.

## What's Included

- Python 3.10 environment
- Required Python packages:
  - strands-agents
  - strands-agents-tools
- VS Code extensions for Python development
- AWS region configured for Amazon Bedrock (us-west-2)

## Getting Started

1. Install [Docker](https://www.docker.com/products/docker-desktop) on your machine
2. Install [Visual Studio Code](https://code.visualstudio.com/)
3. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension for VS Code
4. Clone this repository
5. Open the repository in VS Code
6. When prompted, click "Reopen in Container" or use the command palette (F1) and select "Remote-Containers: Reopen in Container"

## AWS Credentials

For the Amazon Bedrock model provider, you'll need to configure your AWS credentials. You can do this by:

1. Creating a `~/.aws/credentials` file in the container
2. Setting the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables

Example credentials file:
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
region = us-west-2
```

Make sure you have model access enabled for Claude 3.7 Sonnet in the us-west-2 region.

## Running the Demo Scripts

Once the container is running, you can run the demo scripts from the terminal:

```bash
python demo_agent.py
python advanced_agent.py
python multi_agent_system.py
```