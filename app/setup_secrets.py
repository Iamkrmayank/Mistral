#!/usr/bin/env python3
"""
Helper script to create .streamlit/secrets.toml from .env file
Run this from the project root: python app/setup_secrets.py
"""
import os
from pathlib import Path

def main():
    project_root = Path(__file__).parent.parent
    env_file = project_root / ".env"
    secrets_file = project_root / ".streamlit" / "secrets.toml"
    
    print("🔐 Streamlit Secrets Setup Helper\n")
    
    # Check if .env exists
    if not env_file.exists():
        print("❌ .env file not found!")
        print(f"   Expected location: {env_file}")
        print("\n📝 Please create .streamlit/secrets.toml manually:")
        print("   See app/SECRETS_SETUP.md for instructions")
        return
    
    # Read .env file
    env_vars = {}
    with open(env_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                env_vars[key.strip()] = value.strip()
    
    # Create .streamlit directory
    secrets_file.parent.mkdir(exist_ok=True)
    
    # Check if secrets.toml already exists
    if secrets_file.exists():
        response = input(f"\n⚠️  {secrets_file} already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("❌ Cancelled. Existing file not modified.")
            return
    
    # Create secrets.toml
    ocr_endpoint = env_vars.get("MISTRAL_OCR_ENDPOINT", "")
    api_key = env_vars.get("API_KEY", "")
    model = env_vars.get("MISTRAL_MODEL", "mistral-document-ai-2505")
    
    if not ocr_endpoint or not api_key:
        print("❌ Missing required values in .env:")
        if not ocr_endpoint:
            print("   - MISTRAL_OCR_ENDPOINT")
        if not api_key:
            print("   - API_KEY")
        print("\n📝 Please create .streamlit/secrets.toml manually:")
        print("   See app/SECRETS_SETUP.md for instructions")
        return
    
    secrets_content = f"""# Streamlit Secrets Configuration
# Auto-generated from .env file
# DO NOT commit this file to git!

[mistral]
ocr_endpoint = "{ocr_endpoint}"
api_key = "{api_key}"
model = "{model}"
"""
    
    with open(secrets_file, 'w', encoding='utf-8') as f:
        f.write(secrets_content)
    
    print(f"✅ Created {secrets_file}")
    print("\n📋 Contents:")
    print("-" * 50)
    print(secrets_content)
    print("-" * 50)
    print("\n✅ You can now run: streamlit run app/streamlit_app.py")

if __name__ == "__main__":
    main()

