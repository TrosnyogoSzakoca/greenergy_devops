import pytest
import requests

BASE_URL = 'http://localhost:5000'

def test_successful_case():
    payload = {'string': 'abcDEF'}
    response = requests.post(f"{BASE_URL}/", data=payload)
    assert response.status_code == 200
    assert response.json() == {'result': 'ABCdef'}

def test_missing_parameter():
    payload = {}
    response = requests.post(f"{BASE_URL}/", data=payload)
    assert response.status_code == 400
    assert response.json() == {'error': "Missing 'string' parameter in the request."}

def test_empty_string():
    payload = {'string': ''}
    response = requests.post(f"{BASE_URL}/", data=payload)
    assert response.status_code == 400
    assert response.json() == {'error': "Missing 'string' parameter in the request."}

def test_non_string_value():
    payload = {'string': 1234}
    response = requests.post(f"{BASE_URL}/", data=payload)
    assert response.status_code == 400
    assert response.json() == {'error': "Invalid input type. Expecting a string."}

def test_server_error():
    payload = {'string': 'abcDEF'}
    response = requests.post(f"{BASE_URL}/nonexistent", data=payload)
    assert response.status_code == 404
