import os
import json
import argparse
from datetime import datetime

# 12-Factor: Configuration via Environment or Relative Path (Never Hardcoded)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_CONFIG_PATH = os.path.join(BASE_DIR, 'incident-response', 'config', 'metadata.json')
CONFIG_PATH = os.environ.get('SRE_METADATA_PATH', DEFAULT_CONFIG_PATH)

def load_config():
    if not os.path.exists(CONFIG_PATH):
        print(f"Error: Config file not found at {CONFIG_PATH}")
        return None
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def save_config(data):
    try:
        with open(CONFIG_PATH, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully updated configuration at {CONFIG_PATH}")
    except Exception as e:
        print(f"Failed to save config: {e}")

def add_service_interactive(config):
    print("\n--- Add New Service ---")
    service_name = input("Service Name (e.g., Payment-Gateway): ").strip()
    owner = input("Owning Team (e.g., Checkout-Squad): ").strip()
    tier = input("Service Tier (A/B/C): ").strip().upper()
    
    if "services" not in config:
        config["services"] = []
        
    # Check for duplicates
    for s in config["services"]:
        if s["name"].lower() == service_name.lower():
            print("Error: Service already exists!")
            return config

    new_service = {
        "name": service_name,
        "owner": owner,
        "tier": tier
    }
    config["services"].append(new_service)
    print(f"Service '{service_name}' added to memory.")
    return config

def generate_postmortem(config):
    print("\n--- Generate Postmortem ---")
    if "services" not in config or not config["services"]:
        print("No services found in metadata. Please add one first.")
        return

    print("Select Service:")
    for idx, svc in enumerate(config["services"]):
        print(f"{idx + 1}. {svc['name']} (Tier {svc['tier']})")
    
    try:
        choice = int(input("Enter number: ")) - 1
        selected_service = config["services"][choice]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    title = input("Incident Title: ")
    filename = f"postmortem-{datetime.now().strftime('%Y%m%d')}-{selected_service['name'].lower()}.md"
    
    content = f"""# Postmortem: {title}
> **BLAMELESS DISCLAIMER:** This document is blameless.

- **Service:** {selected_service['name']}
- **Tier:** {selected_service['tier']}
- **Owner:** {selected_service['owner']}
- **Date:** {datetime.now().strftime('%Y-%m-%d')}

## What Happened?
...
"""
    with open(filename, 'w') as f:
        f.write(content)
    print(f"\nGenerated: {filename}")

def main():
    parser = argparse.ArgumentParser(description="SRE Postmortem Tool")
    parser.add_argument('--add-service', action='store_true', help="Interactive mode to register a new service")
    args = parser.parse_args()

    config = load_config()
    if not config:
        return

    if args.add_service:
        updated_config = add_service_interactive(config)
        save_config(updated_config)
    else:
        generate_postmortem(config)

if __name__ == "__main__":
    main()
