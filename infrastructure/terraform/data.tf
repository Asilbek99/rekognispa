data "aws_ami" "ubuntu" {
  most_recent = true
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["099720109477"]
}

data "aws_iam_policy_document" "ec2" {
  statement {
    actions   = ["ssm:*"]
    resources = ["*"]
    effect = "Allow"
  }
  statement {
    actions   = ["ssmmessages:*"]
    resources = ["*"]
    effect = "Allow"
  }
  statement {
    actions   = ["ec2messages:*"]
    resources = ["*"]
    effect = "Allow"
  }
  statement {
    actions   = ["ec2:DescribeInstanceStatus"]
    resources = ["*"]
    effect = "Allow"
  }
  statement {
    actions   = ["ds:CreateComputer", "ds:DescribeDirectories"]
    resources = ["*"]
    effect = "Allow"
  }
  statement {
    actions   = ["logs:*"]
    resources = ["*"]
    effect = "Allow"
  }

  statement {
    actions   = ["s3:*"]
    resources = ["*"]
    effect = "Allow"
  }
}
