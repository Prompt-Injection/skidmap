# SkidMap
SkidMap short for "script kiddy" and "Nmap," automating tedious reconnaissance with a sophisticated &amp; methodical approach. Starting with a Ping Sweep to identify live hosts, ensuring targeted scans only, and optionally followed by a stealth scan to minimize detection, this tool effectively reduces unnecessary time and noise.

![skidmap](https://github.com/user-attachments/assets/6250a155-52f9-44a3-befc-4cb5bc730c2a)


## Features
- **Methodical Approach**: SkidMap starts with a **Ping Sweep** to identify live hosts, minimizing unnecessary noise and resource usage.
- **Stealthy Scanning**: The tool offers optional stealth scanning methods to reduce detection by firewalls.
- **Built-in Guidance**: Users can access explanations of various Nmap flags and options, making it suitable for both beginners and experienced users.

## How to Use
To run SkidMap, simply execute the following command in your terminal (Make sure to use sudo):

```bash
sudo python3 skidmap.py
```
## Installation

Before running the tool, ensure your system is updated and that `nmap` is installed. You can do this by following these steps:

1. **Update your system and install nmap** (if not already installed):
   ```bash
   sudo apt update && sudo apt upgrade -y && sudo apt install nmap -y
   ```
2. **Clone the repository and run the tool**:
```bash
git clone https://github.com/Prompt-Injection/skidmap.git && cd skidmap && sudo python3 skidmap.py
```

**Disclaimer:** This tool was developed with the assistance of AI and is intended strictly for educational purposes. The author is not responsible for any misuse or illegal activities that may arise from using this tool. Happy Hacking!
