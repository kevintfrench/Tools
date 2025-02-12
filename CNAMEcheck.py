import subprocess

# Dictionary of CNAMEs and their expected values
cname_records = {
    "laybslxevaukiwsdmgomoitnldo4ver4._domainkey.amherstlibrary.org": "laybslxevaukiwsdmgomoitnldo4ver4.dkim.amazonses.com.",
    "w6jwxr2fk4urdqqxgvfavwu5jutyu45u._domainkey.amherstlibrary.org": "w6jwxr2fk4urdqqxgvfavwu5jutyu45u.dkim.amazonses.com.",
    "zxo55xsmcx2xqhv6octqak6vn7ohe45h._domainkey.amherstlibrary.org": "zxo55xsmcx2xqhv6octqak6vn7ohe45h.dkim.amazonses.com.",
    "3qo6eil6d7c3ejdjjduhhbhw3sizqaio._domainkey.hooksettlibrary.org": "3qo6eil6d7c3ejdjjduhhbhw3sizqaio.dkim.amazonses.com.",
    "dpuz33dmu46omwx26rzi7quselppnnrt._domainkey.hooksettlibrary.org": "dpuz33dmu46omwx26rzi7quselppnnrt.dkim.amazonses.com.",
    "pgzztsirgy37ggyy7xlvz77xdazjzjzt._domainkey.hooksettlibrary.org": "pgzztsirgy37ggyy7xlvz77xdazjzjzt.dkim.amazonses.com.",
    "bvm4a2nv6hassqg7d2uhler5pobip46v._domainkey.merrimacklibrary.org": "bvm4a2nv6hassqg7d2uhler5pobip46v.dkim.amazonses.com.",
    "ggofcpxgotursr7hqeebq5yyrzh33j4y._domainkey.merrimacklibrary.org": "ggofcpxgotursr7hqeebq5yyrzh33j4y.dkim.amazonses.com.",
    "ba45ueuc3lt4dilmn3h4qswy3ard7dc6._domainkey.merrimacklibrary.org": "ba45ueuc3lt4dilmn3h4qswy3ard7dc6.dkim.amazonses.com.",
    "7unuyp3mh6yrzf74ofkdw7pv2s5tag4c._domainkey.nesmithlibrary.org": "7unuyp3mh6yrzf74ofkdw7pv2s5tag4c.dkim.amazonses.com.",
    "we27nhv46mez3fqtingpooju5aidxoms._domainkey.nesmithlibrary.org": "we27nhv46mez3fqtingpooju5aidxoms.dkim.amazonses.com.",
    "yfilfjdgv7q3kl2utdfuyc4z2q3zap7n._domainkey.nesmithlibrary.org": "yfilfjdgv7q3kl2utdfuyc4z2q3zap7n.dkim.amazonses.com."
}

# Function to check CNAME using dig
def check_cname(cname, expected_value):
    try:
        result = subprocess.check_output(["dig", cname, "CNAME", "+short"], universal_newlines=True).strip()
        if result == expected_value:
            return "SUCCESS"
        else:
            return f"FAILED (Expected: {expected_value}, Found: {result if result else 'None'})"
    except subprocess.CalledProcessError:
        return "ERROR"

# Verify each CNAME and print the result
for cname, expected_value in cname_records.items():
    status = check_cname(cname, expected_value)
    print(f"{cname}: {status}")