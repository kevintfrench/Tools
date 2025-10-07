import subprocess, pathlib
gitdir = subprocess.check_output(["git","rev-parse","--git-dir"], text=True).strip()
removed = []
for p in pathlib.Path(gitdir).rglob("*.lock"):
    p.unlink(missing_ok=True)
    removed.append(str(p))
print("Removed" if removed else "No locks found", removed)