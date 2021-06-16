terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "3.42.0"
    }
  }
}

provider "aws" {
    region = "us-east-1"
  
}
resource "aws_security_group" "tf-sec-gr" {
    name = "tf-project"
    ingress   {
      cidr_blocks = [ "0.0.0.0/0" ]
      from_port = 443
      protocol = "tcp"
      to_port = 443
    } 

    ingress   {
      cidr_blocks = [ "0.0.0.0/0" ]
      from_port = 80
      protocol = "tcp"
      to_port = 80
    } 

    ingress   {
      cidr_blocks = [ "0.0.0.0/0" ]
      from_port = 22
      protocol = "tcp"
      to_port = 22
    } 

    egress  {
      cidr_blocks = [ "0.0.0.0/0" ]
      from_port = 0
      protocol = -1
      to_port = 0
    } 
}

resource "aws_instance" "apache-instance" {
    ami = data.aws_ami.amazon-linux-2.id
    instance_type = "t2.micro"
    key_name = "pablokeys"
    count = 2
    security_groups = [ "tf-project" ]
    user_data = file("create_apache.sh")
    tags = {
      Name = "terraform ${element(var.mytags, count.index)} instance"

    }
  
    provisioner "local-exec" {
      command = "echo ${self.private_ip} >> private_ip.txt"
    }
    provisioner "local-exec" {
      command = "echo ${self.public_ip} >> public_ip.txt"
    }


}

data "aws_ami" "amazon-linux-2" {
    most_recent = true
    owners = ["amazon"]
  filter {
    name = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name = "name"
    values = ["amzn2-ami-hvm*"]
  }
  filter {
    name = "architecture"
    values = ["x86_64"]
  }
}

variable "mytags" {
  type    = list
  default = ["first", "second"]
}

output "mypublicip0" {
  value = "http://${aws_instance.apache-instance[0].public_ip}"
}
output "mypublicip1" {
  value = "http://${aws_instance.apache-instance[1].public_ip}"
}