terraform {
  backend "s3" {
    bucket = "terraform-state-rekognispa"
    key    = "global/s3/terraform.tfstate"
    region = "ca-central-1"
  }
}