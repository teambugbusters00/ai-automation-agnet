"""
Proxy script to run test_both.py from the root folder.
Automatically sets path and changes directory context to automationagnet.
"""

import sys
import os

# Add project subdirectory to sys.path
project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "automationagnet")
sys.path.insert(0, project_dir)

# Change current working directory to project folder
os.chdir(project_dir)

# Import and execute the actual test suite
import test_both
if __name__ == "__main__":
    test_both.main()
