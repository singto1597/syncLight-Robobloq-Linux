import time
import math
from driver import SyncLightDriver

# เรียกใช้ Driver
try:
    light = SyncLightDriver()
    print("🌈 Main: Starting Rainbow Loop...")

    t = 0
    while True:
        # คำนวณสีรุ้งสวยๆ
        r = int((math.sin(t) + 1) * 127.5)
        g = int((math.sin(t + 2) + 1) * 127.5)
        b = int((math.sin(t + 4) + 1) * 127.5)

        # สั่งสีได้เลย! ไม่ต้องสน seq หรือ checksum
        light.set_color(r, g, b)
        
        t += 0.1
        time.sleep(0.02)

except KeyboardInterrupt:
    # กด Ctrl+C เพื่อออก
    light.close()
except Exception as e:
    print(f"💥 Critical Error: {e}")