import sys
from config import Config
from api_client import XUIApiClient
from utils.exceptions import XUIError
from utils.logger import logger

def main():
    """Main entry point for the XUI database extractor"""
    if len(sys.argv) != 4:
        logger.error("Invalid number of arguments")
        print("Usage: python main.py <panel_url> <username> <password>")
        print("Example: python main.py https://your-panel.com admin admin123")
        sys.exit(1)
        
    panel_url = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    
    try:
        # Initialize configuration and client
        config = Config(panel_url, username, password)
        client = XUIApiClient(config)
        
        # Login and download database
        client.login()
        output_file = "x-ui.db"
        client.download_database(output_file)
        
    except XUIError as e:
        logger.error(str(e))
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
