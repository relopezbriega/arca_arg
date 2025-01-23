import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arca_api.wslpg import LPGService

if __name__ == "__main__":
    arca_service = LPGService()

    print(arca_service.server_status()) # Check server status

    