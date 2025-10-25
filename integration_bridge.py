import os, subprocess

def run_command(command):
    print(f"→ Executing: {command}")
    os.system(command)

def run_python(code):
    with open("temp_exec.py", "w", encoding="utf-8") as f:
        f.write(code)
    subprocess.run(["python", "temp_exec.py"])

def open_app(app):
    apps = {
        "chrome": "start chrome",
        "vscode": "start code",
        "cmd": "start cmd",
        "explorer": "start explorer",
    }
    cmd = apps.get(app.lower(), f"start {app}")
    os.system(cmd)
