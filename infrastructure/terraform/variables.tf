variable "aws_region" {
  default = "ca-central-1"
  type = string
}
variable "instance_type" {
  default = "t2.micro"
  description = "ec2 instance type"
  type = string
}
variable "ports" {
  type = list(number)
  default = ["80", "443", "22"]
  description = "ingress ports for ec2"
}
variable "app_volume_size" {
  type        = number
  description = "app server volume size"
  default     = 10
}
variable "bucket_name" {
  type = string
  default = "app-s3-id-43343"
}