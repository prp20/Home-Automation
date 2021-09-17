import paho.mqtt.client as mqtt
import time
import sys


def on_log(client, level, buf):
    print("Log: ", buf)


def on_disconnect(client, rc=0):
    print("Disconnected flags" + "result code" + str(rc) + "client_id")
    client.connected_flag = False


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        print("connected OK")
    else:
        print("bad Connection Returned code =", rc)


mqtt.Client.connected_flag = False
broker = "192.168.0.108"
client = mqtt.Client("python1")
client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_connect = on_connect
print("Connecting to broker", broker)
client.loop_start()
try:
    client.connect(broker)
    while not client.connected_flag:
        print("In wait Loop")
        time.sleep(1)
except:
    print("Connection Failed")
    sys.exit("Quitting")

run_flag = True
count = 1
while run_flag:
    print("In Main Loop")
    msg = "Test Message"+str(count)
    ret = client.publish("house/main-light", msg)
    print("Publish", ret)
    count += 1
    time.sleep(4)

client.loop_stop()
client.disconnect()
