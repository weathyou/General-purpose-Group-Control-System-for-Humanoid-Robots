#!/usr/bin/env python3
import socket
import os
import time
import uinput

from vgamepad import VirtualGamepad
from config import UDP_PORT, JS0_PATH

def js0_exists():
    return os.path.exists(JS0_PATH)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", UDP_PORT))

vgamepad = None
mode = "MANUAL"

print("🧠 dance_agent 已启动")
print("📡 等待 PC 指令...")

while True:
    data, addr = sock.recvfrom(1024)
    cmd = data.decode().strip()

    print(f"📩 {cmd} from {addr}")

    # ---------- ENTER SYNC ----------
    if cmd == "ENTER_SYNC":
        if vgamepad:
            print("⚠️ 已在 SYNC 模式")
            continue

        if js0_exists():
            print("❌ js0 仍存在（请先关闭物理手柄）")
            continue

        vgamepad = VirtualGamepad()
        mode = "SYNC"
        print("🔁 已进入 SYNC 模式")

    # ---------- EXIT SYNC ----------
    elif cmd == "EXIT_SYNC":
        if not vgamepad:
            print("⚠️ 当前不在 SYNC 模式")
            continue

        vgamepad.close()
        vgamepad = None
        mode = "MANUAL"
        print("↩️ 已退出 SYNC 模式，请打开物理手柄")

    # ---------- DANCE COMMAND ----------
    elif cmd.startswith("dance_") and vgamepad:
        if cmd == "dance_x":
            vgamepad.trigger_combo(uinput.BTN_NORTH)
        elif cmd == "dance_y":
            vgamepad.trigger_combo(uinput.BTN_WEST)
        elif cmd == "dance_a":
            vgamepad.trigger_combo(uinput.BTN_SOUTH)
        elif cmd == "dance_b":
            vgamepad.trigger_combo(uinput.BTN_EAST)
        else:
            print("❓ 未知 dance 指令")
            
    elif cmd.startswith("mode_") and vgamepad:
        if cmd == "mode_stand_by":
            vgamepad.trigger_combo_mode(uinput.BTN_NORTH)
        else:
            print("❓ 未知 mode 指令")

    # ---------- HEARTBEAT ----------
    elif cmd == "PING":
        sock.sendto(b"PONG", addr)

    else:
        print("⚠️ 忽略指令（模式/状态不匹配）")
