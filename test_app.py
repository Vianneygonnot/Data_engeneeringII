import app
import pytest
import requests
from flask import Flask, request, render_template


def test_url_up():
    assert requests.get('http://localhost:5000').status_code == 200, "The website is broken :C"

def test_pred_neg():
    response = requests.post('http://localhost:5000'+'/analysis', data={'phrase': 'I hate this'}).text
    if 'Negative' in response :
        assert True
    else : assert False

def test_pred_pos():
    response = requests.post('http://localhost:5000'+'/analysis', data={'phrase': 'I love this'}).text
    if 'Positive' in response :
        assert True
    else : assert False

def test_pred_neutral():
    response = requests.post('http://localhost:5000'+'/analysis', data={'phrase': 'It is a dog'}).text
    if 'Neutral' in response :
        assert True
    else : assert False