class Config:
    def __init__(self, panel_url: str, username: str, password: str):
        """
        Initialize configuration for XUI API client
        
        Args:
            panel_url (str): URL of the panel
            username (str): Username for authentication
            password (str): Password for authentication
        """
        self.panel_url = panel_url.rstrip('/')
        self.username = username
        self.password = password
        self.session_cookie = None
