import os
required_env_vars = ["SOFIA_USER_EMAIL", "SOFIA_USER_PASSWORD"]

for var in required_env_vars:
    if not os.getenv(var):
        raise ValueError(f"Environment variable {var} is not set")

class Constants:
    def __init__(self):
        self.SOFIA_USER_EMAIL = os.getenv("SOFIA_USER_EMAIL") or ""
        self.SOFIA_USER_PASSWORD = os.getenv("SOFIA_USER_PASSWORD") or ""
        self.HEADLESS_MODE = False