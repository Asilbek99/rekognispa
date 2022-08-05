output "ami_ubuntu" {
  value = data.aws_ami.ubuntu
}
output "app_server_eip" {
  value = aws_eip.ec2_ip.public_ip
}