variable "container_name" {
  description = "Name of the container"
  type        = string
  default     = "terraform-golden-app"
}

variable "external_port" {
  description = "External port to expose"
  type        = number
  default     = 8080
}
