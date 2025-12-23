import hid

class SyncLightDriver:
    VENDOR_ID = 0x1a86
    PRODUCT_ID = 0xfe07

    def __init__(self):
        self.device = None
        self.sequence_num = 0
        self.connect()

    def connect(self):
        """เชื่อมต่อกับอุปกรณ์"""
        try:
            self.device = hid.device()
            self.device.open(self.VENDOR_ID, self.PRODUCT_ID)
            print(f"✅ Driver: Connected to {hex(self.VENDOR_ID)}:{hex(self.PRODUCT_ID)}")
        except Exception as e:
            print(f"❌ Driver Error: Could not connect - {e}")
            raise e

    def _calculate_checksum(self, data):
        """บวกทุกตัว Modulo 256"""
        return sum(data) % 256

    def set_color(self, r, g, b):
        """ส่งคำสั่งเปลี่ยนสี"""
        if not self.device:
            return

        # 1. Header (52 42 10) + Sequence Number (ใช้ค่าของตัวเอง)
        packet = [0x52, 0x42, 0x10, self.sequence_num]
        
        # 2. Command (86 01) + RGB Data
        packet += [0x86, 0x01, r, g, b]
        
        # 3. Footer (Fixed bytes)
        packet += [0x36, 0x37, 0x00, 0x00, 0x00, 0xFE]
        
        # 4. Checksum
        packet.append(self._calculate_checksum(packet))
        
        # 5. Padding (HID Report 64 bytes)
        # เติม 0x00 นำหน้าเป็น Report ID
        final_report = [0x00] + packet
        while len(final_report) < 65:
            final_report.append(0x00)
            
        try:
            self.device.write(final_report)

            self.sequence_num = (self.sequence_num + 1) % 256
            
        except Exception as e:
            print(f"❌ Send Error: {e}")

    def close(self):
        """ปิดไฟและตัดการเชื่อมต่อ"""
        if self.device:
            print("👋 Driver: Closing connection...")
            try:
                self.set_color(0, 0, 0)
                self.device.close()
            except:
                pass