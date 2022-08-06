provider "aws" {
  region = var.aws_region
}

resource "aws_iam_role" "role" {
  name = "ssm-ec2"
  assume_role_policy = file("assume_role_policy.json")
  tags = {
    Name = "ssm-ec2"
  }
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "ssm-ec2"
  role = aws_iam_role.role.name
}
resource "aws_key_pair" "ssh_Key" {
  key_name    = "App-ssh-public-key"
  public_key  = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICSgMVN+RP1uTIpG1UNPfJNezfJUx0NuyuTtuj3lTuKw"
}

resource "aws_instance" "app" {
  instance_type          = var.instance_type
  ami                    = data.aws_ami.ubuntu.id
  iam_instance_profile   = aws_iam_instance_profile.ec2_profile.name
  key_name               = aws_key_pair.ssh_Key.key_name
  vpc_security_group_ids = [aws_security_group.ec2_sg.id]
  user_data = file("user_data.sh.tpl")
  root_block_device {
    volume_size           = var.app_volume_size
    delete_on_termination = "false"
  }
  tags = {
    Name = "app"
  }
}

resource "aws_eip" "ec2_ip" {
  instance = aws_instance.app.id
  vpc      = true
}


resource "aws_security_group" "ec2_sg" {
  name = "ec2-eip-sg"
  dynamic "ingress" {
    for_each = var.ports
    content {
      from_port        = ingress.value
      to_port          = ingress.value
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]
    }
  }
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
  tags = {
    Name    = "EIP-Security-Group"
  }

}

resource "aws_iam_user" "user" {
  name = "srv_${var.bucket_name}"
}

resource "aws_iam_access_key" "user_keys" {
  user = aws_iam_user.user.name
}

resource "aws_s3_bucket" "bucket" {
  bucket        = var.bucket_name
  force_destroy = "true"

}

resource "aws_iam_policy" "user_policy" {
  name        = "${var.bucket_name}_policy"
  policy      = data.aws_iam_policy_document.user_policy.json
}
resource "aws_iam_user_policy_attachment" "attach" {
  user       = aws_iam_user.user.name
  policy_arn = aws_iam_policy.user_policy.arn
}