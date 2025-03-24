import os
from dotenv import load_dotenv

load_dotenv(override=True)

required_env_vars = ["SOFIA_USER_EMAIL", "SOFIA_USER_PASSWORD", "SOFIA_DOMAIN"]

for var in required_env_vars:
    if not os.getenv(var):
        raise ValueError(f"Environment variable {var} is not set")

class Constants:
    def __init__(self):
        self.SOFIA_USER_EMAIL: str = os.getenv("SOFIA_USER_EMAIL") or ""
        self.SOFIA_USER_PASSWORD: str = os.getenv("SOFIA_USER_PASSWORD") or ""
        self.HEADLESS_MODE: bool = True
        self.DOMAIN: str = os.getenv("SOFIA_DOMAIN") or ""