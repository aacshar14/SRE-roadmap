output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.app_container.id
}

output "app_url" {
  description = "URL to access the app"
  value       = "http://localhost:${var.external_port}"
}
