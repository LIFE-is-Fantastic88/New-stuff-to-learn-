import paho.mqtt.client as mqttclient
import time

##### pc as subscriber ? app as publisher

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("client is connected")
        global connected
        connected = True
    else:
        print("client is not connected")

def on_message(client, userdata, message):
    messagereceived=True
    print("message received", str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)

connected = False
messagereceived = False

broker_address = "xxx.cloudmqtt.com"
port = 12551
user = "xxxxxx"
password = "xxxxxx"

client = mqttclient.Client("MQTT")
client.username_pw_set(user,password=password)
client.on_connect=on_connect
client.connect(broker_address,port=port)
client.loop_start()
client.subscribe("mqtt/secondcode")
while connected!=True:
    time.sleep(0.2)
while messagereceived!=True:
    time.sleep(0.2)
