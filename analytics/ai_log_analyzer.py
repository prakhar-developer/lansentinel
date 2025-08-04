import re
import os
from datetime import datetime

LOG_FILE = os.path.join("logs", "lansentinel.log")
SUSPICIOUS_PATTERNS = [
    r"unauthorized access",
    r"multiple failed login attempts",
    r"packet drop",
    r"peer timeout",
    r"missing handshake",
    r"encryption failure",
    r"face not detected",
    r"disconnected unexpectedly",
    r"high packet loss",
]

def highlight(text, keyword):
    return text.replace(keyword, f"\033[91m{keyword}\033[0m")

def analyze_logs():
    if not os.path.exists(LOG_FILE):
        print("[!] Log file not found.")
        return

    with open(LOG_FILE, "r") as log:
        lines = log.readlines()

    suspicious_entries = []
    for line in lines:
        for pattern in SUSPICIOUS_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                suspicious_entries.append(line.strip())

    if suspicious_entries:
        print("\n[⚠️ Suspicious Events Detected]")
        for entry in suspicious_entries:
            for pattern in SUSPICIOUS_PATTERNS:
                if pattern.lower() in entry.lower():
                    entry = highlight(entry, pattern)
            print(entry)
    else:
        print("[✔️ No suspicious patterns found.]")

if __name__ == "__main__":
    analyze_logs()
