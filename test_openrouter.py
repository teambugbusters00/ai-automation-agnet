"""
test_openrouter.py — Dedicated OpenRouter AI Generation Test
"""
import sys
import os

# Add project subdirectory to sys.path
project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "automationagnet")
sys.path.insert(0, project_dir)
os.chdir(project_dir)

import config
from ai_agent import generate_message

# Colors
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def main():
    print(f"\n{BOLD}{CYAN}==============================================================={RESET}")
    print(f"  [+] DEDICATED OPENROUTER AI TEST")
    print(f"{BOLD}{CYAN}==============================================================={RESET}")
    
    key = os.environ.get("OPENROUTER_API_KEY", "")
    print(f"  - OpenRouter API Key: {GREEN}Yes (Starts with: {key[:8]}...){RESET}" if key else f"  - OpenRouter API Key: {RED}Not Set{RESET}")
    
    sample_lead = {
        "business_name": "Desert Glamping Tours",
        "owner_name": "Vijay",
        "business_type": "tour operator",
        "city": "Jodhpur",
        "website": "https://desertglampingjodhpur.com",
        "ig_followers": 3200,
        "google_reviews": 142
    }
    
    print("\n  - Requesting message from OpenRouter (Gemini 2.5 Flash)...")
    try:
        msg = generate_message(sample_lead, "whatsapp")
        print(f"  - {GREEN}Success! Generated Message:{RESET}")
        print("  +" + "-" * 60)
        for line in msg.split("\n"):
            safe_line = line.encode('ascii', errors='replace').decode('ascii')
            print(f"  | {safe_line}")
        print("  +" + "-" * 60)
    except Exception as e:
        print(f"  - {RED}AI Generation failed: {e}{RESET}")

if __name__ == "__main__":
    main()
