import os
import datetime
import re

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), '../incident-response/postmortem-template.md')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../incident-response/postmortems')

def slugify(text):
    text = text.lower()
    return re.sub(r'[\W_]+', '-', text).strip('-')

def main():
    print("--- SRE Postmortem Generator ---")
    
    # 1. Gather Input
    title = input("Enter Incident Title (e.g. Login Failure): ").strip()
    if not title:
        print("Error: Title is required.")
        return

    severity = input("Enter Severity (SEV-1, SEV-2...): ").strip().upper()
    authors = input("Enter Authors (comma separated): ").strip()
    
    # 2. Prepare Metadata
    today = datetime.date.today().isoformat() # YYYY-MM-DD
    filename = f"{today}-{slugify(title)}.md"
    output_path = os.path.join(OUTPUT_DIR, filename)

    # 3. Read Template
    if not os.path.exists(TEMPLATE_PATH):
        print(f"Error: Template not found at {TEMPLATE_PATH}")
        return

    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 4. Replace Placeholders (Basic replacement)
    # Note: The template is static, so we essentially prepend/replace metadata headers
    # Or typically we just write a fresh header and append the rest.
    
    # Let's replace the top block simply
    content = content.replace("**Date:** YYYY-MM-DD", f"**Date:** {today}")
    content = content.replace("**Authors:**", f"**Authors:** {authors}")
    content = content.replace("**Severity:** [SEV-1 | SEV-2 ...]", f"**Severity:** {severity}")

    # 5. Write File
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# Postmortem: {title}\n\n")
        f.write(content)

    print(f"\nSUCCESS! Postmortem created at:\n{os.path.abspath(output_path)}")
    print("\nNext Steps:")
    print(f"1. Open the file.")
    print(f"2. Fill in the timeline and 5 Whys.")

if __name__ == "__main__":
    main()
