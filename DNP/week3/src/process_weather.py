import zmq
import json
import sys
import threading
from datetime import datetime, timedelta

WEATHER_INPUT_PORT = 5555
FASHION_SOCKET_PORT = 5556
IP_ADD = '127.0.0.1'

latest_data = {}


def average_temperature_humidity():
    global latest_data
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    now = datetime.strptime(now_str, "%Y-%m-%d %H:%M:%S")
    threshold = now - timedelta(seconds=30)

    last_30_sec_data = []
    for data in latest_data.values():
        if data['time'] >= str(threshold):
            last_30_sec_data.append(data)

    if last_30_sec_data:
        total_temp = sum(data['temperature'] for data in last_30_sec_data)
        total_hum = sum(data['humidity'] for data in last_30_sec_data)
        num_data_points = len(last_30_sec_data)
        avg_temp = total_temp / num_data_points
        avg_hum = total_hum / num_data_points

        latest_data['average-temp'] = round(avg_temp, 2)
        latest_data['average-hum'] = round(avg_hum, 2)


def recommendation():
    result = ""
    average_temperature_humidity()
    if 'average-temp' in latest_data:
        if latest_data['average-temp'] < 10:
            result = "Today weather is cold. Its better to wear warm clothes"
        elif latest_data['average-temp'] > 10 and latest_data['average-temp'] < 25:
            result = "Feel free to wear spring/autumn clothes"
        else:
            result = "Go for light clothes"
        print(result)
        latest_data.pop('average-temp')
        latest_data.pop('average-hum')
    return result


def report():
    result = ""
    average_temperature_humidity()
    if 'average-temp' in latest_data:
        result = f"The last 30 sec average Temperature is {latest_data['average-temp']} and Humidity {latest_data['average-hum']}"
        print(result)
        latest_data.pop('average-temp')
        latest_data.pop('average-hum')
    return result


def check_weather(data):
    with open("weather_data.log", 'a') as f:
        f.write(json.dumps(data) + '\n')


def receive_weather_data():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(f"tcp://{IP_ADD}:{WEATHER_INPUT_PORT}")
    socket.setsockopt_string(zmq.SUBSCRIBE, "weather")
    while True:
        message = socket.recv_string()
        print("Received weather data:", message)
        topic, data_json = message.split(" ", 1)
        data_json = data_json.replace("'", "\"")
        data = json.loads(data_json)
        check_weather(data)
        latest_data[data['time']] = data


def handle_client():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://{IP_ADD}:{FASHION_SOCKET_PORT}")
    while True:
        request = socket.recv_string()
        if request == "Fashion":
            reply = recommendation()
        elif request == "Weather":
            reply = report()
        else:
            reply = "Query Not Found"
        socket.send_string(reply)


def main():
    try:
        client_thread = threading.Thread(target=handle_client)
        weather_thread = threading.Thread(target=receive_weather_data)
        client_thread.start()
        weather_thread.start()
        client_thread.join()
        weather_thread.join()
    except KeyboardInterrupt:
        print('Terminating data_processor')


if __name__ == "__main__":
    main()
