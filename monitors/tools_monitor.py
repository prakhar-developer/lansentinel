import subprocess
import platform

def run_netstat():
    print("\n[🔍] Running netstat...")
    if platform.system() == "Windows":
        result = subprocess.run(["netstat", "-ano"], capture_output=True, text=True)
    else:
        result = subprocess.run(["netstat", "-tuln"], capture_output=True, text=True)
    print(result.stdout)

def run_lsof():
    print("\n[🔍] Running lsof...")
    try:
        result = subprocess.run(["lsof", "-i"], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("[⚠️] lsof not found (may not be installed on Windows).")

def run_iftop():
    print("\n[🔍] Running iftop (summary)...")
    print("[⚠️] Cannot run interactive tools like iftop via script.")
    print("👉 Run manually in terminal: `sudo iftop`")

if __name__ == "__main__":
    run_netstat()
    run_lsof()
    run_iftop()
