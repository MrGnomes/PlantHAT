# PlantHAT
![PlantHAT](https://raw.githubusercontent.com/mrgnomes/readme_images/master/plantHAT_Readme.png)

Python library and design files for a modular greenhouse system based on the RaspberryPi.

It is powered by a 12V/2A power supply an it backpowers the raspberry pi so everything can be run from a single supply.
The 12V can be used to power up to 5 additional 12V inductive loads, like water pumps or magnetic valves that can be controlled over 
the GPIO Pins of the Pi.

# Sensors

Connect a 3 Wire temperature/humidity sensor and up to 4 I2C sensors to monitor your plants.

# Hardware

You can find the schematic design file in the "hardware" section of this repo.

## Maximum Ratings
The HAT is designed to work with a single power supply, that backpowers the raspberry pi.
The power ratings for the supply are: 12V/2A 

# Coming Soon - PlantHAT Web-APP

I am working on a python web app based on flask to monitor the plants and provide a admin panel to control water pumps and different inductive loads needed for a garden/greenhouse.
Here is a screenshot of the current app:

![Dashboard](https://raw.githubusercontent.com/mrgnomes/readme_images/master/plantHAT_dashboard.png)


 