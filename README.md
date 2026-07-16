# python-multithreaded-portscanner
# Multithreaded TCP Port Scanner in Python

An asynchronous, highly-efficient TCP Port Scanner developed in Python using the `socket` and `threading` libraries. This tool is designed for network administrators and security enthusiasts to quickly map open ports on target hosts.

## Features
* **Multithreaded Performance:** Uses Python's `threading` and `queue` libraries to scan ports concurrently, scanning 1000+ ports in seconds.
* **DNS Resolution:** Automatically converts domain names (e.g., `scanme.nmap.org`) to IPv4 addresses.
* **Error Handling:** Gracefully handles keyboard interrupts (`Ctrl+C`) and host-unreachable errors.
* **No External Dependencies:** Built entirely with Python's standard library.

## How It Works
The scanner utilizes a **TCP Connect Scan** approach. It attempts to complete a 3-way handshake with each specified port on the target IP. 
* If `socket.connect_ex()` returns `0`, the port is **OPEN**.
* If it returns an error code, the port is closed or filtered.

## Usage
1. Clone this repository:
   ```bash
   git clone [https://github.com/qethlx/python-multithreaded-portscanner.git](https://github.com/qethlx/python-multithreaded-portscanner.git)
   cd python-multithreaded-portscanner


Run the scanner:

Bash
python scanner.py

Enter the target IP or domain when prompted (e.g., scanme.nmap.org).
