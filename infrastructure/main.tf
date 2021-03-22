terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.26.0"
    }
  }

  backend "s3" {
    profile = "default"
    bucket  = "perfexp-infra"
    key     = "summit-grp4/terraform_state/terraform.tfstate"
    region  = "us-east-2"
    encrypt = true
  }
}

provider "aws" {
  region  = var.region
  profile = "default"
}
