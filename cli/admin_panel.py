import os
import time
from analytics.ai_log_analyzer import analyze_logs
from monitors.tools_monitor import show_netstat, show_lsof, show_iftop
from proctoring.face_capture import capture_snapshots
from threading import Thread

LOG_FILE = os.path.join("logs", "lansentinel.log")

def tail_log(lines=20):
    if not os.path.exists(LOG_FILE):
        print("[!] Log file not found.")
        return
    with open(LOG_FILE, "r") as f:
        all_lines = f.readlines()
        for line in all_lines[-lines:]:
            print(line.strip())

def start_face_monitor():
    t = Thread(target=capture_snapshots, kwargs={'interval': 10})
    t.daemon = True
    t.start()
    print("[🎥] Face monitoring daemon started.")

def print_menu():
    print("\n===== 🧭 LANSentinel++ Admin Panel =====")
    print("1. View Logs")
    print("2. Run AI Log Analyzer")
    print("3. Monitor: netstat")
    print("4. Monitor: lsof")
    print("5. Monitor: iftop")
    print("6. Start Face Monitor")
    print("0. Exit")
    print("========================================")

def run_admin_cli():
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            print("\n[📝 Recent Logs]")
            tail_log()
        elif choice == "2":
            print("\n[🤖 AI Log Analyzer]")
            analyze_logs()
        elif choice == "3":
            print("\n[🌐 netstat]")
            show_netstat()
        elif choice == "4":
            print("\n[📁 lsof]")
            show_lsof()
        elif choice == "5":
            print("\n[📡 iftop]")
            show_iftop()
        elif choice == "6":
            start_face_monitor()
        elif choice == "0":
            print("Exiting Admin Panel...")
            break
        else:
            print("Invalid option. Try again.")
