# raspi-aws-iot
Communicate between two Raspberry Pi through AWS IoT

![iot copy](https://user-images.githubusercontent.com/9275193/51081892-86f5bd00-16c9-11e9-99e5-fe9e4a72f5e5.jpg)

![ezgif com-add-text](https://user-images.githubusercontent.com/9275193/51079601-dde29e80-1697-11e9-99a1-a1aa05d2c7f6.gif)


### Configure AWS IoT Thing
Watch my youtube video for step by step instruction to create IoT thing and connect to it from Raspberry Pi

https://youtu.be/MCXXoyV_j4w



### Thing Policy
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:*"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
```

### Install GPIO library 
```
sudo apt-get update
sudo apt-get -y install python-dev python3-rpi.gpio
```

### Install AWS Python SDK on Raspberry Pi

```
pip3 install AWSIoTPythonSDK
```

### Diagram of First Raspberry Pi
![image](https://github.com/just4give/raspi-aws-iot/blob/master/led.png)


### Diagram of Second Raspberry Pi
![image](https://github.com/just4give/raspi-aws-iot/blob/master/button.png)

### Run LED code on First Raspberry Pi
```
python3 iot-led.py
```
### Run Button code on Second Raspberry Pi
```
python3 iot-button.py
```
