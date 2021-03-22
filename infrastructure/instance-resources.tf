resource "aws_instance" "perf-summit-grp4-instance" {
  ami                         = var.amis[var.region]
  instance_type               = var.instance_type
  key_name                    = var.key_name
  associate_public_ip_address = true
  subnet_id                   = var.subnet_id_public_0
  vpc_security_group_ids      = [aws_security_group.perf-summit-grp4-instance-sg.id]

  user_data_base64 = base64encode(data.template_file.userdata.rendered)

  tags = {
    Name        = "perf-summit-grp4-instance"
    project     = var.project_tag
    responsible = var.responsible_tag
  }

  volume_tags = {
    project     = var.project_tag
    responsible = var.responsible_tag
  }
}

resource "aws_security_group" "perf-summit-grp4-instance-sg" {
  name        = "perf-summit-grp4-instance-sg"
  description = "Instance security"
  vpc_id      = var.vpc_id

  ingress {
    description = "API port"
    from_port   = var.api_port
    to_port     = var.api_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Kibana port"
    from_port   = var.kibana_port
    to_port     = var.kibana_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH port"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["181.62.31.62/32"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "perf-summit-grp4-instance-sg"
    project     = var.project_tag
    responsible = var.responsible_tag
  }
}

data "template_file" "userdata" {
  template = file("scripts/userdata.sh")

  # vars = {
  #   api_port = var.api_port
  #   user     = "ubuntu"
  # }
}
