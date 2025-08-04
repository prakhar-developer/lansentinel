# 🛰️ LANSentinel++

**Secure, Encrypted, AI-Analyzed Peer-to-Peer Communication System for LAN Environments**

> 🔐 Built with: Python, TCP/IP Sockets, AES Encryption, Unix Tools, AI Log Analysis  
> 📡 Designed for: Internal LAN communication (labs, coaching centers, cyber cafes, security-critical nodes)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Platform](https://img.shields.io/badge/Platform-Unix%20%7C%20Windows-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/Encrypted-AES--256-informational)

---

## 🧠 Why LANSentinel++?

A real-world solution to enable **secure, encrypted chat, file sharing, and monitoring** in closed LANs — especially where GUIs or internet access is limited. Useful in:

- 🏫 Coaching centers
- 🧪 Lab networks
- 🛰️ Secure organizations
- 🛠️ Developer teams over LAN

---

## 🚀 Features

| Module | Description |
|--------|-------------|
| 🔌 Peer-to-Peer | Multi-threaded socket server/client with encryption |
| 🔐 AES Encryption | All packets and files are AES-256 encrypted |
| 📁 File Transfer | Share files securely across peers |
| 🧠 AI Analyzer | Log analyzer to detect suspicious activities |
| 🎥 Proctoring | Webcam-based face capture daemon |
| 🧰 Unix Tools | Real-time system monitors (`netstat`, `lsof`, `iftop`) |
| 🔁 Retry + Session | Resume broken sessions with retry logic |
| 🧭 Admin CLI | Full interactive interface to control everything |

---

## 🏗️ Folder Structure

```bash
lansentinel/
├── __main__.py              # Entry point (CLI)
├── requirements.txt
├── core/                    # Core engine
│   ├── peer.py
│   ├── server.py
│   ├── client.py
│   ├── packet.py
│   ├── encryption.py
│   ├── session_manager.py
│   └── retry_manager.py
├── proctoring/              # Webcam snapshot & detection
│   ├── face_capture.py
│   ├── face_detector.py
│   └── snaps/
├── analytics/               # AI log analysis
│   └── ai_log_analyzer.py
├── monitors/                # System monitoring tools
│   └── tools_monitor.py
├── cli/                     # Admin command panel
│   └── admin_panel.py
├── logs/                    # Runtime logs
│   └── lansentinel.log
├── tests/                   # Unit tests
│   ├── test_encryption.py
│   └── test_packets.py
├── Dockerfile
├── README.md

```
⚙️ Setup & Run
🔧 Prerequisites
Python 3.11+

Docker (optional)

Same LAN (WiFi or cable)

Optional: camera for proctoring

📦 Install Dependencies
```bash
pip install -r requirements.txt
```

🧭 Start System
🐳 Docker (Recommended)
```bash
docker build -t lansentinel .
docker run -it lansentinel
```
🐍 Manual (Non-Docker)
```bash
python __main__.py
```
🛠️ CLI Commands
| Command                    | Description              |
| -------------------------- | ------------------------ |
| `start-server`             | Starts local peer server |
| `connect-peer <IP> <PORT>` | Connect to another peer  |
| `send "<message>"`         | Send encrypted message   |
| `sendfile <path>`          | Secure file sharing      |
| `view-log`                 | View recent logs         |
| `scan-lan` *(optional)*    | Detect active peers      |
| `exit`                     | Exit CLI                 |

🧪 Run Tests
```bash
python -m unittest discover -s tests
```

📸 Proctoring Module
```bash
python proctoring/face_capture.py         # Webcam snapshots
python proctoring/face_detector.py        # Face detection
```

🧠 AI Log Analyzer
```bash
python analytics/ai_log_analyzer.py
```
Flags unusual activity, unauthorized IPs, retry storms, etc.

🧰 System Monitoring
```bash
python monitors/tools_monitor.py
```
Wraps Unix tools like netstat, lsof, and iftop.

💡 Use Cases
Coaching centers using LAN messaging with file sharing

Secure internal messaging (offline)

Peer-to-peer file exchange in college labs

Monitoring network behavior + proctoring during internal exams

🤖 Tech Stack
Python (Sockets, AES, threading, logging)

TCP/IP protocols

Unix/Linux command tools

AI Log pattern detection

Docker packaging
Wraps Unix tools like netstat, lsof, and iftop.

💡 Use Cases
Coaching centers using LAN messaging with file sharing

Secure internal messaging (offline)

Peer-to-peer file exchange in college labs

Monitoring network behavior + proctoring during internal exams

🤖 Tech Stack
Python (Sockets, AES, threading, logging)

TCP/IP protocols

Unix/Linux command tools

AI Log pattern detection

Docker packaging

📜 License
This project is licensed under the MIT License — feel free to use, modify, and extend!

💌 Author
Prakhar Srivastava
System Programmer & AI Backend Developer
📧 Email: [prakhar_developer@outlook.com]
🔗 GitHub: [github.com/prakhar-developer]
🔗 LinkedIn: [https://www.linkedin.com/in/prakhar--developer/]