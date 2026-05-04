import pytest
import subprocess, json, time

@pytest.fixture
def chrome_fixture():
    """Startet Chrome mit --force-renderer-accessibility für Tests."""
    proc = subprocess.Popen(
        ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
         "--force-renderer-accessibility", "--remote-debugging-port=0",
         "--no-first-run", "--headless=new"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)
    yield proc.pid
    proc.terminate()
