import subprocess

# List of CNAME records to verify
cnames = [
    "laybslxevaukiwsdmgomoitnldo4ver4._domainkey.amherstlibrary.org",
    "w6jwxr2fk4urdqqxgvfavwu5jutyu45u._domainkey.amherstlibrary.org",
    "zxo55xsmcx2xqhv6octqak6vn7ohe45h._domainkey.amherstlibrary.org"
]

# Function to check CNAME using dig
def check_cname(cname):
    try:
        result = subprocess.check_output(["dig", cname, "CNAME", "+short"], universal_newlines=True)
        return result.strip() if result else "Not Found"
    except subprocess.CalledProcessError:
        return "Error"

# Verify each CNAME and print the result
for cname in cnames:
    result = check_cname(cname)
    print(f"{cname}: {result}")