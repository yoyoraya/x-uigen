class XUIError(Exception):
    """Base exception for XUI related errors"""
    pass

class LoginError(XUIError):
    """Raised when login fails"""
    pass

class DatabaseDownloadError(XUIError):
    """Raised when database download fails"""
    pass
