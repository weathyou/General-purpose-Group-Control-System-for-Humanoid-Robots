# vgamepad.py
import uinput
import time
from config import VIRTUAL_CREATE_DELAY, COMBO_HOLD, COMBO_PRESS

class VirtualGamepad:
    def __init__(self):
        self.device = uinput.Device([
            uinput.BTN_TL,    # LB
            uinput.BTN_TR,    # RB
            uinput.BTN_SOUTH, # A
            uinput.BTN_EAST,  # B
            uinput.BTN_NORTH, # X
            uinput.BTN_WEST   # Y
        ])
        time.sleep(VIRTUAL_CREATE_DELAY)
        print("🎮 虚拟手柄已创建")

    def trigger_combo(self, btn):
        # LB + RB
        self.device.emit(uinput.BTN_TL, 1)
        self.device.emit(uinput.BTN_TR, 1)
        time.sleep(COMBO_HOLD)
        # 再补一次肩键电平，防止丢帧
        self.device.emit(uinput.BTN_TL, 1)
        self.device.emit(uinput.BTN_TR, 1)
        time.sleep(0.05)
	
        # X / Y / A / B
        self.device.emit(btn, 1)
        time.sleep(COMBO_PRESS)
        self.device.emit(btn, 0)

        # release
        self.device.emit(uinput.BTN_TR, 0)
        self.device.emit(uinput.BTN_TL, 0)
        
    def trigger_combo_mode(self, btn):
        # LB
        self.device.emit(uinput.BTN_TL, 1)
        time.sleep(COMBO_HOLD)
        # 再补一次肩键电平，防止丢帧
        self.device.emit(uinput.BTN_TL, 1)
        time.sleep(0.05)
        # + X
        self.device.emit(btn, 1)
        time.sleep(COMBO_PRESS)
        self.device.emit(btn, 0)

        # release
        self.device.emit(uinput.BTN_TL, 0)
        
    def close(self):
        print("🧹 销毁虚拟手柄")
        self.device = None
