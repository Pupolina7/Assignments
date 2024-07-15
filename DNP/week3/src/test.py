# import json
#
# data = 'weather {"time": "2024-04-02 03:24:40", "temperature": 23.3, "humidity": 74.2}'
# message = json.dumps(data)
# print(message)
# topic, data_json = message.split(" ", 1)
# print(topic)
# print(data_json)
# # data1 = json.loads(data_json)
# # print(data1)
from datetime import datetime, timedelta

latest_data = {
    1: {'temperature': 25, 'humidity': 50, 'time': '2024-04-02 10:00:00'},
    2: {'temperature': 30, 'humidity': 60, 'time': '2024-04-02 10:01:00'},
    3: {'temperature': 28, 'humidity': 55, 'time': '2024-04-02 10:02:00'}
}
now = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")

    # Calculate the time threshold for the last 30 seconds
threshold = now - timedelta(seconds=30)
print(threshold, type(threshold))
# Accessing values using latest_data.values()
values = latest_data.values()
for value in values:
    if value['time'] <= str(threshold):
        print(value['time'])
