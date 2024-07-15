import zmq
import json
import sys

WEATHER_INPUT_PORT = 5555
IP_ADD = '127.0.0.1'


def check_co2(data):
    with open("co2_data.log", 'a') as f:
        f.write(json.dumps(data) + '\n')
    if data["co2"] > 400:
        print("Danger Zone! Please do not leave home")


def main():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(f"tcp://{IP_ADD}:{WEATHER_INPUT_PORT}")
    socket.setsockopt_string(zmq.SUBSCRIBE, "co2")
    try:
        while True:
            message = socket.recv_string()
            print("Received weather data:", message)
            topic, data_json = message.split(" ", 1)
            data_json = data_json.replace("'", "\"")
            data = json.loads(data_json)
            check_co2(data)
    except KeyboardInterrupt:
        print("Terminating data_processor")
    finally:
        socket.close()
        context.term()


if __name__ == "__main__":
    main()
