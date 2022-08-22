terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

# Configure the GitHub Provider
#Copy the token from github and paste it
provider "github" {
    token='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'
}

