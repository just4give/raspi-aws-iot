from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import logging
import time
import json
import RPi.GPIO as GPIO


        
BUTTONPIN=18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setup(BUTTONPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

clientId="mypythoncodebutton"
thingName="LED"
isOn=False
myAWSIoTMQTTShadowClient = AWSIoTMQTTShadowClient(clientId)
myAWSIoTMQTTShadowClient.configureEndpoint("a2c6vtfn7g8m57-ats.iot.us-east-1.amazonaws.com", 8883)
myAWSIoTMQTTShadowClient.configureCredentials("root-CA.pem", "LED-private.pem.key", "LED.pem.crt")

# Connect to AWS IoT
myAWSIoTMQTTShadowClient.connect()

deviceShadowHandler = myAWSIoTMQTTShadowClient.createShadowHandlerWithName(thingName, True)

# Loop forever
while True: # Run forever
  input_state = GPIO.input(BUTTONPIN)
  if input_state == False:
   if isOn == False:
    print("Button pressed to turn on led")
    newPayload = '{"state":{"desired":{"isLEDOn":"true"}}}'
    deviceShadowHandler.shadowUpdate(newPayload, None, 5)
    isOn=True
   else:
    print("Button pressed to turn off led")
    newPayload = '{"state":{"desired":{"isLEDOn":"false"}}}'
    deviceShadowHandler.shadowUpdate(newPayload, None, 5)
    isOn=False
  time.sleep(0.2) # Sleep for 0.2 second

