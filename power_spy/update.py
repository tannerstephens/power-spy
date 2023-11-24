import subprocess
import threading
from pathlib import Path

app_dir = Path(__file__).parent.parent.resolve()

UPDATING_FILE_PATH = Path("/tmp/updating")


def update():
    threading.Thread(target=_update).start()


def is_updating():
    return UPDATING_FILE_PATH.exists()


def update_available():
    subprocess.call(["git", "remote", "update"])
    git_status = subprocess.Popen(
        ["git", "status", "-uno"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = git_status.communicate()

    return "Your branch is behind" in out.decode()


def _update():
    UPDATING_FILE_PATH.touch()

    subprocess.call(["/bin/bash", app_dir / "maintainence" / "update.sh"])
    subprocess.call(["/bin/bash", app_dir / "maintainence" / "install.sh"], cwd=app_dir)

    UPDATING_FILE_PATH.unlink()
