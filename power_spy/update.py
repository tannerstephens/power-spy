import subprocess
import threading
from pathlib import Path

app_dir = Path(__file__).parent.parent.resolve()


def update():
    threading.Thread(target=_update).start()


def check_for_update():
    subprocess.call(["git", "remote", "update"])
    git_status = subprocess.Popen(
        ["git", "status", "-uno"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = git_status.communicate()

    return "Your branch is behind" in out.decode()


def _update():
    subprocess.call(["/bin/bash", app_dir / "maintainence" / "update.sh"])
    subprocess.call(["/bin/bash", app_dir / "maintainence" / "install.sh"], cwd=app_dir)
