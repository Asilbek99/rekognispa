provider "aws" {
  region = var.aws_region
}

resource "aws_iam_role" "system_manger" {
  name               = "SystemManagerRole"
  assume_role_policy = file("assume_role_policy.json")
  tags = {
    Name = "SystemManagerRole"
  }
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "ssm-ec2"
  role = aws_iam_role.system_manger.name
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