
# 🧼 Connectionless Smart Hygiene System

## 📖 Overview
The **Connectionless Smart Hygiene System** is an IoT-based automation project designed to promote hygiene compliance in public and private spaces. Using **Raspberry Pi Pico** and **MicroPython**, the system integrates multiple sensors to enable **touch-free interaction** for sanitation and monitoring.

---

## ⚙️ Features
- 🚰 **Ultrasonic Sensor** – Detects hand presence for automatic sanitizer/tap activation  
- 👀 **IR/PIR Sensor** – Enables touchless user interaction and motion detection  
- 💡 **LDR Sensor** – Controls lighting/water flow based on ambient conditions  
- 🌱 **Moisture Sensor** – Monitors cleaning/waste management hygiene  
- 🛡️ **Gas Sensor (MQ series)** – Detects harmful gases for safety monitoring  
- 🌡️ **Temperature & Humidity (DHT11/DHT22)** – Tracks environmental conditions  

---

## 🛠️ Tech Stack
- **Hardware:** Raspberry Pi Pico, sensors (Ultrasonic, PIR, LDR, MQ, DHT11/DHT22), actuators (DC motor, pump)  
- **Software:** MicroPython, event-driven programming  
- **Protocols (Future Scope):** MQTT/HTTP for IoT cloud integration  

---

## 🚀 Outcomes
- Built a **prototype hygiene automation system** with multiple sensor integrations  
- Reduced **false triggers** through sensor calibration and event-driven logic  
- Demonstrated scalability for **smart city applications** (schools, hospitals, offices)  

---

## 🔧 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Mahithashiva/connectionless-smart-hygiene.git
   cd connectionless-smart-hygiene
