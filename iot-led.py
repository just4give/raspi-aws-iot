from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import logging
import time
import json
import RPi.GPIO as GPIO

class shadowCallbackContainer:
    def __init__(self, deviceShadowInstance):
        self.deviceShadowInstance = deviceShadowInstance

    # Custom Shadow callback
    def customShadowCallback_Delta(self, payload, responseStatus, token):
        # payload is a JSON string ready to be parsed using json.loads(...)
        # in both Py2.x and Py3.x
        global LEDPIN
        payloadDict = json.loads(payload)
        isLEDOn=payloadDict["state"]["isLEDOn"]
        deltaMessage = json.dumps(payloadDict["state"])
        #print(deltaMessage)
        if isLEDOn == "true":
            print("Turn on LED")
            GPIO.output(LEDPIN, GPIO.HIGH) # Turn on
        else:
            print("Turn off LED")
            GPIO.output(LEDPIN, GPIO.LOW) # Turn on    
        #print("Request to update the reported state...")
        newPayload = '{"state":{"reported":' + deltaMessage + '}}'
        self.deviceShadowInstance.shadowUpdate(newPayload, None, 5)
        
LEDPIN=14
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setup(LEDPIN, GPIO.OUT, initial=GPIO.LOW)

clientId="mypythoncodeled"
thingName="LED"
myAWSIoTMQTTShadowClient = AWSIoTMQTTShadowClient(clientId)
myAWSIoTMQTTShadowClient.configureEndpoint("a2c6vtfn7g8m57-ats.iot.us-east-1.amazonaws.com", 8883)
myAWSIoTMQTTShadowClient.configureCredentials("root-CA.pem", "LED-private.pem.key", "LED.pem.crt")

# Connect to AWS IoT
myAWSIoTMQTTShadowClient.connect()

deviceShadowHandler = myAWSIoTMQTTShadowClient.createShadowHandlerWithName(thingName, True)
shadowCallbackContainer_Bot = shadowCallbackContainer(deviceShadowHandler)

# Listen on deltas
deviceShadowHandler.shadowRegisterDeltaCallback(shadowCallbackContainer_Bot.customShadowCallback_Delta)

# Loop forever
while True:
    time.sleep(1)

