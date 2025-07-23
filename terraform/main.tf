provider "aws" {
  region = var.region
}

resource "aws_guardduty_detector" "main" {
  enable = true
}

resource "aws_securityhub_account" "main" {}

resource "aws_config_configuration_recorder" "main" {
  name     = "main"
  role_arn = aws_iam_role.config_role.arn
}

# Add VPC, Security Group, IAM, and other resources as needed.
