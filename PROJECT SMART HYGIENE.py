from machine import Pin, ADC, time_pulse_us
import network
import urequests
import time


SSID ="vivo T4 Lite 5G"

PASSWORD = "Mahitha@123"


API_KEY = "R4PL2EFAQ8IY7W07"


ir_left = Pin(14, Pin.IN)
ir_right = Pin(15, Pin.IN)

ldr = ADC(26)

trig = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

pir = Pin(12, Pin.IN)

buzzer = Pin(5, Pin.OUT)
led = Pin(6, Pin.OUT)


count = 0


wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

print("Connecting WiFi...")

while not wifi.isconnected():
    time.sleep(1)

print("WiFi Connected")
print(wifi.ifconfig())


def get_distance():

    trig.low()
    time.sleep_us(2)

    trig.high()
    time.sleep_us(10)

    trig.low()

    duration = time_pulse_us(echo, 1)

    distance = (duration * 0.0343) / 2

    return distance


def send_data(left, right, light, distance, motion, count):

    url = "https://api.thingspeak.com/update?api_key={}".format(API_KEY)

    url += "&field1={}".format(left)
    url += "&field2={}".format(right)
    url += "&field3={}".format(light)
    url += "&field4={}".format(distance)
    url += "&field5={}".format(motion)
    url += "&field6={}".format(count)

    try:
        response = urequests.get(url)
        response.close()
        print("Data Uploaded")

    except:
        print("Upload Failed")


while True:

    left = ir_left.value()

    right = ir_right.value()

    light = ldr.read_u16()

    distance = get_distance()

    motion = pir.value()

    alert = False
    message = "Normal"

    
    if left == 0:
        count += 1
        message = "Looking Left"
        alert = True

    
    elif right == 0:
        count += 1
        message = "Looking Right"
        alert = True

    
    elif light > 50000:
        count += 1
        message = "Mobile Use"
        alert = True


    elif distance < 20:
        count += 1
        message = "Student Moving"
        alert = True

    elif motion == 1:
        count += 1
        message = "Motion Detected"
        alert = True

    
    if alert:
        buzzer.value(1)
        led.value(1)
    else:
        buzzer.value(0)
        led.value(0)

    
    print("========== SENSOR VALUES ==========")

    print("Left IR:", left)

    print("Right IR:", right)

    print("LDR:", light)

    print("Distance:", round(distance, 2), "cm")

    print("PIR Motion:", motion)

    print("Status:", message)

    print("Suspicion Count:", count)

    print("===================================")

    
    send_data(
        left,
        right,
        light,
        round(distance, 2),
        motion,
        count
    )

    time.sleep(2)ws