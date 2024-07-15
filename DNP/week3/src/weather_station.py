import sys
import zmq
import time
import json
import random
from datetime import datetime

IP_ADD = '127.0.0.1'
DATA_PROCESSES_INPUT_PORT = 5555


def generate_weather_data():
    humidity = round(random.uniform(40, 100), 1)
    temperature = round(random.uniform(5, 40), 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    weather_data = {"time": timestamp, "temperature": temperature, "humidity": humidity}
    return weather_data


def generate_co2_level():
    co2 = round(random.uniform(300, 500), 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    co2_level = {"time": timestamp, "co2": co2}
    return co2_level


def main():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(f"tcp://{IP_ADD}:{DATA_PROCESSES_INPUT_PORT}")
    time.sleep(2)
    try:
        while True:
            time.sleep(2)
            weather_data = generate_weather_data()
            socket.send_string(f"weather {weather_data}")
            print("Weather is sent from WS1", weather_data)
            time.sleep(2)
            co2_level = generate_co2_level()
            socket.send_string(f"co2 {co2_level}")
            print("CO2 is sent from WS1", co2_level)
    except KeyboardInterrupt:
        print("Terminating weather station")
    finally:
        socket.close()
        context.term()


if __name__ == '__main__':
    main()
