"""
run_tests.py - Cross-platform test runner for Windsurf Project Startup Pack

Runs the test suite for the memory synchronization system and all agents/tools.
Provides parity with tools/run_tests.ps1 for onboarding, CI, and automation.

References:
- Onboarding: README.md, docs/AGENT_GUIDE.md
- Test/CI: requirements-dev.txt, tools/run_tests.ps1
- Memory Protocols: docs/memory-protocols.md

Usage:
    python run_tests.py                  # Run all tests
    python run_tests.py --pattern test_* # Run tests matching pattern
    python run_tests.py --coverage       # Run tests with coverage report

CI/Automation stub:
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    python run_tests.py --coverage
"""

import argparse
import os
import subprocess
import sys

TEST_DIR = "tests"
DEFAULT_PATTERN = "test_*.py"


def main():
    parser = argparse.ArgumentParser(description="Run the Windsurf test suite.")
    parser.add_argument('--coverage', action='store_true', help='Run tests with coverage report')
    parser.add_argument('--pattern', default=DEFAULT_PATTERN, help='Glob pattern for test files')
    args = parser.parse_args()

    # Ensure test directory exists
    if not os.path.isdir(TEST_DIR):
        os.makedirs(TEST_DIR)
        print(f"Created test directory: {TEST_DIR}")

    # Find test files
    import glob
    test_files = glob.glob(os.path.join(TEST_DIR, '**', args.pattern), recursive=True)
    test_files = [f for f in test_files if '__pycache__' not in f]
    if not test_files:
        print(f"No test files found matching pattern: {args.pattern}")
        sys.exit(0)

    print(f"Running tests...\nTest files: {', '.join(test_files)}")

    # Activate venv if present
    venv_path = os.path.join('.venv', 'Scripts' if os.name == 'nt' else 'bin')
    activate = os.path.join(venv_path, 'activate_this.py')
    if os.path.exists(activate):
        exec(open(activate).read(), {'__file__': activate})

    # Run tests
    if args.coverage:
        try:
            import coverage
        except ImportError:
            print("Installing coverage...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'coverage'])
        cmd = [sys.executable, '-m', 'coverage', 'run', '-m', 'pytest']
        if args.pattern != DEFAULT_PATTERN:
            cmd += ['-k', args.pattern]
        subprocess.run(cmd, check=True)
        subprocess.run([sys.executable, '-m', 'coverage', 'report', '-m'], check=True)
    else:
        cmd = [sys.executable, '-m', 'pytest']
        if args.pattern != DEFAULT_PATTERN:
            cmd += ['-k', args.pattern]
        subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
