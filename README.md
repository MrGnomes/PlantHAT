# PlantHAT
![PlantHAT](https://raw.githubusercontent.com/mrgnomes/readme_images/master/plantHAT_Readme.png)

Python library and design files for a modular plant monitoring and watering system based on the Raspberry Pi.

It is powered by a 12V power supply an it backpowers the Pi so that everything can be run from a single supply.
The 12V can be used to power up to 5 additional 12V inductive loads, like water pumps or magnetic valves that can be controlled over 
the GPIO Pins of the Pi.

# Sensors

Connect a 3 Wire temperature/humidity sensor (e.g. DHT22) and up to 4 I2C sensors to monitor your plants.

# Hardware

You can find the schematic design file in the "hardware" section of this repo.

## Maximum Ratings
The HAT is designed to work with a single power supply, that backpowers the raspberry pi with 5V/2A.

Input Voltage: 12V 

# Python3 Web-APP (Flask)

## Windows
The App was written using the current Python Tool for Visual Studio included in the community edition of Visual Studio 2017 and as an extension for Visual Studio 2015.
If you have the GitHub extension for Visual Studio and the python tools installed you can clone the git and start right away by using the solution file.

By using the Visual Studio as the IDE, the flask based WebApp can be compiled and debugged on the windows development PC.
When the code is working, the app can be run inside the Pi and by using the PTVSD package one can remotely debug the flask app directly from the VS-IDE by attaching to the running process using the IP-Address of the Pi.
Python 3.4 (32-bit) was used, because this was the current python version supported by the Pi, when I started the project.

## Linux

If you are using linux, just clone the repo, install the required packages and run the app by typing:
>> python3 run.py

inside the app folder.

(requirements.txt file is coming soon)

## Screenshot

This is what the current working App looks like:

![Dashboard](https://raw.githubusercontent.com/mrgnomes/readme_images/master/plantHAT_dashboard.png)

# Coming Soon - Sensor data charts and GPIO control




 
