import requests
from typing import Optional
from config import Config
from utils.exceptions import LoginError, DatabaseDownloadError
from utils.logger import logger

class XUIApiClient:
    def __init__(self, config: Config):
        """
        Initialize XUI API client
        
        Args:
            config (Config): Configuration instance
        """
        self.config = config
        
    def login(self) -> bool:
        """
        Login to the panel and get session cookie
        
        Returns:
            bool: True if login successful, False otherwise
        
        Raises:
            LoginError: If login request fails
        """
        login_url = f"{self.config.panel_url}/login"
        data = {
            "username": self.config.username,
            "password": self.config.password
        }
        
        try:
            response = requests.post(login_url, json=data)
            response.raise_for_status()
            
            if 'session' in response.cookies:
                self.config.session_cookie = response.cookies['session']
                logger.info("Successfully logged in")
                return True
                
            raise LoginError("No session cookie received")
            
        except requests.exceptions.RequestException as e:
            raise LoginError(f"Login failed: {str(e)}")
            
    def download_database(self, output_path: str) -> bool:
        """
        Download the x-ui database file
        
        Args:
            output_path (str): Path where to save the database file
            
        Returns:
            bool: True if download successful, False otherwise
            
        Raises:
            DatabaseDownloadError: If download fails
        """
        if not self.config.session_cookie:
            raise DatabaseDownloadError("Not logged in. Please login first.")
            
        download_url = f"{self.config.panel_url}/xui/API/inbound/backup"
        cookies = {'session': self.config.session_cookie}
        
        try:
            response = requests.get(download_url, cookies=cookies)
            response.raise_for_status()
            
            with open(output_path, 'wb') as f:
                f.write(response.content)
            
            logger.info(f"Successfully downloaded database to {output_path}")
            return True
            
        except requests.exceptions.RequestException as e:
            raise DatabaseDownloadError(f"Failed to download database: {str(e)}")
        except IOError as e:
            raise DatabaseDownloadError(f"Failed to save database file: {str(e)}")
