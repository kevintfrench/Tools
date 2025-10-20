import os, re, shutil, csv, time, pathlib

home = pathlib.Path.home()
# Likely attachment locations
candidate_roots = [
    home / "Library/Group Containers/group.com.apple.calendar/Attachments",
    home / "Library/Group Containers/group.com.apple.calendar/Library/Calendars",
    home / "Library/Calendars"
]

# Extract suspicious names from the ESET CSV if present
eset_csv = home / "20251020_ESET"
patterns = [
    r"Microsoft[_ ]?Billing[_ ]?Portal.*\\.htm[l]?",
    r"MS365[-_ ]?Service[-_ ]?Portal.*\\.htm[l]?",
    r"HTML/Phishing\\.(Agent|Gen)"
]
names = set()
if eset_csv.exists():
    txt = eset_csv.read_text(errors="ignore")
    for m in re.finditer(r"file://(/[^;,]+)", txt):
        names.add(os.path.basename(m.group(1)))
    for m in re.finditer(r"Object URI;([^;]+)", txt):
        base = os.path.basename(m.group(1))
        if base:
            names.add(base)

def suspicious(fname):
    low = fname.lower()
    if low.endswith((".htm", ".html")):
        if any(k in low for k in ["microsoft", "portal", "ms365", "billing", "service"]):
            return True
    return False

quar = home / "Calendar_Attach_Quarantine"
quar.mkdir(exist_ok=True)
hits = []

for root in candidate_roots:
    if not root.exists():
        continue
    for dirpath, _, files in os.walk(root):
        for f in files:
            full = pathlib.Path(dirpath) / f
            low = f.lower()
            if f in names or suspicious(f):
                dst = quar / f"{int(time.time())}_{f}"
                shutil.move(str(full), str(dst))
                hits.append([str(full), str(dst), os.path.getsize(dst)])

with open(home / "calendar_attach_actions.csv", "w", newline="") as fh:
    csv.writer(fh).writerows([["source","destination","bytes"], *hits])
print(f"Quarantined {len(hits)} files to {quar}")