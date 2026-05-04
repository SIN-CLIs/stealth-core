import subprocess, os

def get_secret(key):
    """Holt Secret aus macOS Keychain. Fallback: env var."""
    try:
        r = subprocess.run(["security", "find-generic-password", "-w", "-s", key],
            capture_output=True, text=True, timeout=5)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
    except: pass
    return os.environ.get(key, "")
