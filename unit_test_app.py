import app
import pytest
import requests
import datetime

def test_url_up():
    assert requests.get('http://localhost:5000').status_code == 200, "The website is broken :C"

def test_mean():
    data = requests.get('http://127.0.0.1:5000/mean?liste=10&liste=20&liste=30').text
    print(data)
    assert requests.get('http://127.0.0.1:5000/mean?liste=10&liste=20&liste=30').text == "The mean of the list [10, 20, 30]  is : 20"

def test_time():
    data = requests.get('http://127.0.0.1:5000/mean?liste=10&liste=20&liste=30').elapsed

    for i in range(999):
        data += requests.get('http://127.0.0.1:5000/mean?liste=10&liste=20&liste=30').elapsed

    mean_time = data/1000
    print(mean_time.total_seconds())

    timeout = datetime.timedelta(milliseconds=100)

    assert mean_time < timeout