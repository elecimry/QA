import os

from pathlib import Path
from dotenv import load_dotenv
environment = os.environ.get('test_env', 'test')
env_path = Path('.') / f'.env.{environment}' #C:\Users\LPG-user\page_object_for_habr\.env.
load_dotenv(dotenv_path=env_path)


USER_EMAIL = os.getenv('USER_EMAIL')
USER_PASSWORD = os.getenv('USER_PASSWORD')
#print(USER_EMAIL)