# raspi-aws-iot
Communicate between two Raspberry Pi through AWS IoT

![ezgif com-add-text](https://user-images.githubusercontent.com/9275193/51079601-dde29e80-1697-11e9-99a1-a1aa05d2c7f6.gif)


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
