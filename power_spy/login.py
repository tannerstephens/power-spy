from pathlib import Path

PASSWORD_FILE = Path(__name__).parent.resolve() / "password"


def check_password(password: str):
    with open(PASSWORD_FILE) as f:
        return password == f.readline().strip()


def create_password_file():
    PASSWORD_FILE.touch()
