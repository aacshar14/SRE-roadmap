resource "docker_image" "app" {
  name         = "aacshar14/golden-signals-app:latest"
  keep_locally = false
}

resource "docker_container" "app_container" {
  image = docker_image.app.image_id
  name  = var.container_name
  ports {
    internal = 5000
    external = var.external_port
  }
}
