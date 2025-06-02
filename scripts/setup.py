#!/usr/bin/env python3
"""
setup.py - Cross-platform onboarding script for Windsurf Project Startup Pack
Purpose: Robust, automated setup for plug-and-play onboarding, agent orchestration, and workflow automation.
"""
import os
import sys
import subprocess

REQUIRED_PYTHON = (3, 9)

BANNER = """
===============================
 Windsurf Project Startup Pack Setup
===============================
"""

def check_python():
    if sys.version_info < REQUIRED_PYTHON:
        sys.exit(f"Python >= {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]} required. Detected: {sys.version_info.major}.{sys.version_info.minor}")

def install_requirements():
    req_files = ["tools/requirements.txt", "requirements.txt"]
    for req in req_files:
        if os.path.isfile(req):
            print(f"Installing dependencies from {req}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req])
            return
    print("No requirements.txt found. Skipping Python dependency installation.")

def install_playwright():
    try:
        import playwright
        print("Installing Playwright browsers...")
        subprocess.check_call([sys.executable, "-m", "playwright", "install"])
    except ImportError:
        print("Playwright not found. To enable browser automation, run: pip install playwright && playwright install")

def main():
    print(BANNER)
    check_python()
    install_requirements()
    install_playwright()
    print("\nFor onboarding, see:")
    print("  - README.md")
    print("  - docs/ONBOARDING.md (if present)")
    print("  - CONTRIBUTING.md")
    print("  - agents_config.yaml, cascades.yaml, notifications.yaml")
    print("\nSetup complete! Ready for multi-agent, collaborative workflows.")

if __name__ == "__main__":
    main()
