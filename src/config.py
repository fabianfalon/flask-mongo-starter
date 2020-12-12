import os


class BaseConfig:
    """Base configuration"""

    DEBUG = False
    TESTING = False
    SECRET_KEY = "PB3aGvTmCkzaLGRAxDc3aMayKTPTDd5usT8gw4pCmKOk5AlJjh12pTrnNgQyOHCH"
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    DEBUG = True
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Testing configuration"""

    TESTING = True
