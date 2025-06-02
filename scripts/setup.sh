#!/usr/bin/env bash
# setup.sh - Cross-platform (Linux/macOS) onboarding script for Windsurf Project Startup Pack
# Purpose: Robust, automated setup for plug-and-play onboarding, agent orchestration, and workflow automation.

set -e

# --- Onboarding Banner ---
echo "\n==============================="
echo " Windsurf Project Startup Pack Setup "
echo "===============================\n"

# --- Prerequisite Checks ---
command -v python3 >/dev/null 2>&1 || { echo >&2 "Python 3.x is required. Aborting."; exit 1; }
PYTHON_VERSION=$(python3 -c 'import sys; print("{}.{}".format(sys.version_info[0], sys.version_info[1]))')
if [[ "$PYTHON_VERSION" < "3.9" ]]; then
  echo "Python >=3.9 required. Detected: $PYTHON_VERSION"
  exit 1
fi

command -v pip3 >/dev/null 2>&1 || { echo >&2 "pip3 is required. Aborting."; exit 1; }

# --- Install Python dependencies ---
if [[ -f "tools/requirements.txt" ]]; then
  echo "Installing Python dependencies from tools/requirements.txt..."
  pip3 install -r tools/requirements.txt
elif [[ -f "requirements.txt" ]]; then
  echo "Installing Python dependencies from requirements.txt..."
  pip3 install -r requirements.txt
else
  echo "No requirements.txt found. Skipping Python dependency installation."
fi

# --- Optional: Playwright install ---
if command -v playwright >/dev/null 2>&1; then
  echo "Installing Playwright browsers..."
  playwright install
else
  echo "Playwright not found. To enable browser automation, run: pip3 install playwright && playwright install"
fi

# --- Onboarding Documentation ---
echo "\nFor onboarding, see:"
echo "  - README.md"
echo "  - docs/ONBOARDING.md (if present)"
echo "  - CONTRIBUTING.md"
echo "  - agents_config.yaml, cascades.yaml, notifications.yaml"
echo "\nSetup complete! Ready for multi-agent, collaborative workflows."
