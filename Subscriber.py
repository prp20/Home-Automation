import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("house/main-light")


def on_message(client, userdata, msg):
    print(msg.payload)


client = mqtt.Client()
client.connect("192.168.0.108", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
