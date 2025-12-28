terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
  # Subscription ID is usually picked up from 'az login', or you can hardcode it here:
  # subscription_id = "xxxx-xxxx-xxxx"
}
