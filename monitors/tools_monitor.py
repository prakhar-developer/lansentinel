import subprocess
import platform

def show_netstat():
    print("\n[🔍] Running netstat...")
    if platform.system() == "Windows":
        result = subprocess.run(["netstat", "-ano"], capture_output=True, text=True)
    else:
        result = subprocess.run(["netstat", "-tuln"], capture_output=True, text=True)
    print(result.stdout)

def show_lsof():
    print("\n[🔍] Running lsof...")
    try:
        result = subprocess.run(["lsof", "-i"], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("[⚠️] lsof not found (may not be installed on Windows).")

def show_iftop():
    print("\n[🔍] Running iftop (summary)...")
    print("[⚠️] Cannot run interactive tools like iftop via script.")
    print("👉 Run manually in terminal: `sudo iftop`")

if __name__ == "__main__":
    show_netstat()
    show_lsof()
    show_iftop()
