import os, shutil, csv, time, pathlib
home = pathlib.Path.home()
root = home / "Library/Group Containers/group.com.apple.calendar/Library/Calendars"
quar = home / "Calendar_Attach_Quarantine"
quar.mkdir(exist_ok=True)
hits = []
for dirpath, _, files in os.walk(root):
    for f in files:
        name = f.lower()
        if name.endswith((".htm", ".html")) and any(s in name for s in [
            "microsoft_billing_portal".lower(), "ms365-service-portal".lower()
        ]):
            src = pathlib.Path(dirpath) / f
            dst = quar / f"{int(time.time())}_{f}"
            shutil.move(src, dst)
            hits.append([str(src), str(dst), os.path.getsize(dst)])
with open(home / "calendar_attach_actions.csv", "w", newline="") as fh:
    csv.writer(fh).writerows([["source","destination","bytes"], *hits])
print(f"Quarantined {len(hits)} files to {quar}")