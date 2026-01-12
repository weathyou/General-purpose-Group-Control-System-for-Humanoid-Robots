# General-purpose-Group-Control-System-for-Humanoid-Robots 🎶🤖

[English](README.md) | [简体中文](README_zh.md)

A PC-based synchronization controller for triggering **simultaneous dance actions**
across multiple humanoid robots using **virtual gamepads** over LAN.

## ✨ Features

- 🎮 Virtual gamepad injection (uinput)
- 🤖 Control multiple identical robots simultaneously
- 🌐 LAN-based synchronization (Wi-Fi)
- 🔁 ENTER_SYNC / EXIT_SYNC mode switching
- 🧩 Compatible with original 2.4GHz physical gamepad
- ⚙️ systemd service support

## 🧠 Architecture

PC Controller
  ├── Virtual Gamepad (js10)
  ├── Sync Manager
  └── Network Broadcaster
          ↓
   Robot A / B / C
      dance_agent.py
          ↓
     Vendor Controller (js0)


https://github.com/user-attachments/assets/ee95c134-4661-4301-bfda-dadd3123de61


## 🚀 Quick Start

### 1. Clone
```bash
git clone https://github.com/weathyou/General-purpose-Group-Control-System-for-Humanoid-Robots.git
cd General-purpose-Group-Control-System-for-Humanoid-Robots
