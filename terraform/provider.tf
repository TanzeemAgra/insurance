resource "github_repository" "insurance" {
  name        = "insurance"
  description = "This repository is to demostrate ML/MLOps"

  visibility = "public"

  template {
    owner      = "github"
    repository = "terraform-module-template"
  }
}