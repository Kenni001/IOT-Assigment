"""
MicroPython IoT Weather Station Example for Wokwi.com

To view the data:

1. Go to http://www.hivemq.com/demos/websocket-client/
2. Click "Connect"
3. Under Subscriptions, click "Add New Topic Subscription"
4. In the Topic field, type "wokwi-weather" then click "Subscribe"

Now click on the DHT22 sensor in the simulation,
change the temperature/humidity, and you should see
the message appear on the MQTT Broker, in the "Messages" pane.

Copyright (C) 2022, Uri Shaked

https://wokwi.com/arduino/projects/322577683855704658
"""

import network
import time
import urandom
from umqtt.simple import MQTTClient

# MQTT broker details of Thingspeak
mqtt_client_id = "CjUUOhQ6OAgCKRcSFwwsMxI"
mqtt_username = "CjUUOhQ6OAgCKRcSFwwsMxI"
mqtt_password = "uPSFaSCSDZYrEJZU4geB8T4Q"
mqtt_server = "mqtt3.thingspeak.com"
mqtt_port = 1883
channel_id = "2488649"
write_api_key = "AWZHG47CSBNZNMHU"

wifi_ssid = "Wokwi-GUEST"
wifi_password = ""

# MQTT Topics for different sensor fields
mqtt_topic_temperature = "channels/{}/publish/fields/field1".format(channel_id)
mqtt_topic_humidity = "channels/{}/publish/fields/field2".format(channel_id)
mqtt_topic_co2 = "channels/{}/publish/fields/field3".format(channel_id)

def sensor_values():
    temperature = urandom.uniform(-50, 50)
    humidity = urandom.uniform(0, 100)
    co2 = urandom.uniform(300, 2000)
    return temperature, humidity, co2

def data_upload(client, topic, data):
    try:
        client.publish(topic, str(data))
        print("Uploaded to {}: {}".format(topic, data))
    except Exception as e:
        print("Failed to upload data to {}: {}".format(topic, e))

def connect_wifi(ssid, password):
    print("Connecting to Wi-Fi...")
    wifi_interface = network.WLAN(network.STA_IF)
    wifi_interface.active(True)
    wifi_interface.connect(ssid, password)
    
    # Display loading animation while waiting for connection
    animation = "|/-\\"
    animation_index = 0
    
    while not wifi_interface.isconnected():
        print("Connecting... " + animation[animation_index % len(animation)], end="\r")
        animation_index += 1
        time.sleep(0.5)
    
    print("\nWi-Fi connection established")

def main():
    connect_wifi(wifi_ssid, wifi_password)
    client = MQTTClient(mqtt_client_id, mqtt_server, user=mqtt_username, password=mqtt_password)
    client.connect()
    
    while True:
        temperature, humidity, co2 = sensor_values()
        data_upload(client, mqtt_topic_temperature, temperature)
        data_upload(client, mqtt_topic_humidity, humidity)
        data_upload(client, mqtt_topic_co2, co2)
        time.sleep(5)  # Adjust delay as needed

if __name__ == "__main__":
    main()