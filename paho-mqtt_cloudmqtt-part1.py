from paho import paho.mqtt.client as mqttclient
import time

##### app as subscriber ? pc as publisher

def on_connect(client,usedata,flags,rc):
    if rc==0:
        print("Client is connected")
        global connected
        connected = True
    else:
        print("Connection failed gai gai")
connected = False
broker_addressses="xxxxx.cloudmqtt.com"
port=12551
user="xxxxxxxxx"
password="xxxxxxxxx"

client=mqttclient.Client("MQTT")
client.username_pw_set(user,password)
client.on_connect=on_connect
client.connect(broker_address, port=port)
client.loop_start()
while connected!=True:
    time.sleep(0.2)
client.publish("mqtt/firstcode","Hi sam")
client.loop_stop()
