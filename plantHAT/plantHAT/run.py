""" 
    PlantHAT - the modular plant monitoring and growth automation system based on the RaspberryPi

        This RaspberryPi HAT that allows you to turn your RaspberryPi into an plant growth automation system.
        It allows you to control watering pumps, magnetic valves, sensors and light.
        It is build with the flask microframework and provides a Admin Dashboard (sb-admin v2) with charts
        that plot your sensor data to monitor plants.
        In the strategy tab you can set up growth strategies for your plants.

        TODO:
        If you connect a RaspberryPi camera you can use the Plantix API developed by PEAT (PEAT GmbH, Hannover)
        to provide you with high class, state of the art plant disease and pests detection.
        Go and check out their website at wwww.peat.ai or test their App Plantix.

        PlantHAT on GitHub: https://github.com/MrGnomes/plantHAT

        :copyright: (c) 2017 Patrick Laza.
        :license: MIT, see LICENSE for more details.
"""

from app import db, create_app


if __name__ == '__main__':
    app = create_app('default')
    app.run(host='0.0.0.0', port=5000, debug=False)