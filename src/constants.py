import os
required_env_vars = ["SOFIA_USER_EMAIL", "SOFIA_USER_PASSWORD"]

for var in required_env_vars:
    if not os.getenv(var):
        raise ValueError(f"Environment variable {var} is not set")

class Constants:
    SOFIA_USER_EMAIL:str = os.getenv("SOFIA_USER_EMAIL") or ""
    SOFIA_USER_PASSWORD:str = os.getenv("SOFIA_USER_PASSWORD") or ""