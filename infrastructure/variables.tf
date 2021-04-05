variable "project_tag" {
  default = "ramp-up-devops"
}

variable "responsible_tag" {
  default = "jose.posadam"
}

variable "region" {
  type = string
}

variable "vpc_id" {
  type = string
}

variable "subnet_id_public_0" {
  type = string
}

variable "amis" {
  type = map(string)
}

variable "key_name" {
  type = string
}

variable "instance_type" {
  type = string
}

variable "api_port" {
  type = string
}

variable "auth_port" {
  type = string
}

variable "employees_port" {
  type = string
}

variable "db_port" {
  type = string
}

variable "kibana_port" {
  type = string
}
