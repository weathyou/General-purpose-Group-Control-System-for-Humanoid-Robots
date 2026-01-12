# controller.py
import socket
import sys

PORT = 5005
BROADCAST = "255.255.255.255"

if len(sys.argv) < 2:
    print("用法:")
    print("  python3 controller.py ENTER_SYNC")
    print("  python3 controller.py dance_x|dance_y|dance_a|dance_b")
    print("  python3 controller.py EXIT_SYNC")
    print("  python3 controller.py mode_stand_by")
    sys.exit(1)

cmd = sys.argv[1]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(cmd.encode(), (BROADCAST, PORT))

print(f"📤 已发送: {cmd}")
