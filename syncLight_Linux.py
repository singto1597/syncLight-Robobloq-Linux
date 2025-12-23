import hid
import time
import math

# รหัสอุปกรณ์
VENDOR_ID = 0x1a86
PRODUCT_ID = 0xfe07

def calculate_checksum(data):
    # สูตร: บวกทุกตัว แล้วเอาเศษจากการหาร 256 (Low Byte)
    return sum(data) % 256

def send_rgb(device, r, g, b, sequence_num):
    # --- โครงสร้าง Packet ที่แกะจาก Wireshark ---
    
    # 1. Header (52 42 10) + Sequence Number
    packet = [0x52, 0x42, 0x10, sequence_num]
    
    # 2. Command (86 01)
    packet += [0x86, 0x01]
    
    # 3. ข้อมูลสี RGB (3 Bytes)
    packet += [r, g, b]
    
    # 4. Footer (36 37 00 00 00 FE) - ตัวปิดท้ายก่อน Checksum
    packet += [0x36, 0x37, 0x00, 0x00, 0x00, 0xFE]
    
    # 5. คำนวณ Checksum
    checksum = calculate_checksum(packet)
    packet.append(checksum)
    
    # 6. แพ็คใส่กล่อง USB (Padding ให้ครบ 64 bytes)
    # ต้องมี 0x00 นำหน้าเป็น Report ID
    final_report = [0x00] + packet
    while len(final_report) < 65:
        final_report.append(0x00)
        
    try:
        device.write(final_report)
    except Exception as e:
        print(f"❌ Send Error: {e}")

try:
    print(f"🔌 Connecting to SyncLight...")
    h = hid.device()
    h.open(VENDOR_ID, PRODUCT_ID)
    print("✅ Connected! Protocol Hacked Successfully.")
    print("🌈 Starting Rainbow Effect...")

    seq = 0
    t = 0
    
    while True:
        r = int((math.sin(t) + 1) * 127.5)
        g = int((math.sin(t + 2) + 1) * 127.5)
        b = int((math.sin(t + 4) + 1) * 127.5)

        send_rgb(h, r, g, b, seq)
        
        t += 0.1
        seq += 1
        if seq > 255: seq = 0 
        
        time.sleep(0.02)

except KeyboardInterrupt:
    print("\n👋 Closing...")
    send_rgb(h, 0, 0, 0, 0)
    h.close()
except Exception as e:
    print(f"💥 Error: {e}")