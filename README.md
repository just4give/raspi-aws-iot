# raspi-aws-iot
Communicate between two Raspberry Pi through AWS IoT


### Install GPIO library 
```
sudo apt-get update
sudo apt-get -y install python-dev python3-rpi.gpio
```

### Install AWS Python SDK on Raspberry Pi

```
pip3 install AWSIoTPythonSDK
```

### Run LED code on First Raspberry Pi
```
python3 iot-led.py
```
### Run LED code on Second Raspberry Pi
```
python3 iot-button.py
```
