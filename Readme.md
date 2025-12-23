# SyncLight Robobloq Linux Driver 🐧

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux-orange?style=flat&logo=linux)
![License](https://img.shields.io/badge/License-MIT-green)

[🇺🇸 English Version](#-english-version) | [🇹🇭 ภาษาไทย](#-thai-version-for-thai-users)

---

## 🇺🇸 English Version

**Unofficial Linux driver for Robobloq SyncLight (and compatible devices).** Since the manufacturer only provides Windows/macOS software, I reverse-engineered the USB HID protocol to make it work on Linux!

### 🚀 Features
- [x] **Full RGB Color Control:** Set any custom color.
- [x] **Rainbow/Cycle Modes:** Built-in loop effects.
- [x] **Keep-Alive:** Prevents the device from reverting to demo mode.
- [ ] **Screen Sync (Ambilight):** Real-time screen capture synchronization *(Coming Soon)*.

### 🛠️ Requirements
* Python 3.x
* `hidapi` library

### 📦 Installation

1. **Install dependencies:**
   ```bash
   sudo apt install libhidapi-hidraw0
   pip install hidapi

```

2. **Clone this repository:**
```bash
git clone [https://github.com/singto1597/syncLight-Robobloq-Linux.git](https://github.com/singto1597/syncLight-Robobloq-Linux.git)
cd syncLight-Robobloq-Linux

```


3. **Setup udev rules:** To control the device without `sudo`, create a rule file:
```bash
echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="fe07", MODE="0666"' | sudo tee /etc/udev/rules.d/99-synclight.rules

```


Then reload:
```bash
sudo udevadm control --reload-rules && sudo udevadm trigger

```



### 🎮 Usage

Run the script directly:

```bash
python3 synclight.py

```

### 🕵️‍♂️ How it works?

I analyzed the USB packets using **Wireshark** (with USBPcap) and replicated the HID protocol in Python.

* **Vendor ID:** `0x1a86` (WCH)
* **Product ID:** `0xfe07`
* **Protocol:** 64-byte HID report with Checksum validation.

---

## 🇹🇭 Thai Version (For Thai Users)

### "ซื้อไฟมาใช้ แต่ซอฟต์แวร์ไม่มีของ Linux... ก็เขียนเองแม่งเลย!"

คือ ผมซื้อไฟ LED ของ Robobloq มา แต่ว่า ผมใช้ Linux ไงง แต่ทาง Robobloq เขาไม่ได้ทำมาเพื่อรองรับระบบ Linux ผมก็เลยลองใช้ Wireshark เพื่อดูว่ามันส่งข้อมูล คำสั่ง ไปให้กับตัวไฟของผมยังไง แล้วก็ลองแกะๆ สั่งๆคำสั่งมันไปดู **ได้เฉยเว้ยเห้ยย!** 🎉

ก็เลยทำโปรเจกต์นี้ขึ้นมาแจก เผื่อใครใช้ Linux แล้วเจอปัญหาเดียวกัน เอาไปใช้ได้เลยครับ!

### 🚀 ทำอะไรได้บ้าง?

* [x] สั่งเปลี่ยนสี RGB ได้ตามใจชอบ
* [x] มีโหมดรุ้ง (Rainbow) วนลูปสวยๆ
* [x] แก้ปัญหาไฟตัด (Keep-Alive) คือถ้าไม่ส่งข้อมูลนานๆ ไฟมันจะดีดกลับไปโหมด Demo อันนี้แก้ให้แล้ว
* [ ] **Screen Sync:** เดี๋ยวจะทำเวอร์ชันดูดสีหน้าจอตามมาทีหลัง (เร็วๆ นี้)

### 📦 ติดตั้งยังไง (ฉบับรวบรัด)

1. **ลงของที่ต้องใช้ก่อน:**
```bash
sudo apt install libhidapi-hidraw0
pip install hidapi

```


2. **ดึงโค้ดไปลงเครื่อง:**
```bash
git clone [https://github.com/singto1597/syncLight-Robobloq-Linux.git](https://github.com/singto1597/syncLight-Robobloq-Linux.git)
cd syncLight-Robobloq-Linux

```


3. **ตั้งค่าให้มันมองเห็น USB (สำคัญมาก!):**
ปกติ Linux มันจะบล็อคไม่ให้เรายุ่งกับ USB ตรงๆ ถ้าขี้เกียจพิมพ์ `sudo` ทุกรอบ ให้ก๊อปคำสั่งนี้ไปรันทีเดียวจบ:
```bash
echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="fe07", MODE="0666"' | sudo tee /etc/udev/rules.d/99-synclight.rules

```


เสร็จแล้วรีโหลดระบบ 1 ที:
```bash
sudo udevadm control --reload-rules && sudo udevadm trigger

```



### 🎮 วิธีเล่น

รันไฟล์ Python ได้เลย:

```bash
python3 synclight.py

```

*(ถ้าไฟติดแล้วเปลี่ยนสีได้ ก็คือจบงานครับ!)*

---

## ❤️ Credits

Created by [singto1597](https://www.google.com/search?q=https://github.com/singto1597)

```
