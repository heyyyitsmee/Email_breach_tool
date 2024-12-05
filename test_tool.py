import pytest
from tool import validating_email, identifying_breaches, displaying_breaches
import requests
from unittest.mock import patch
from io import StringIO
import sys

def test_validating_email():
    assert validating_email("zainabfatima0058963@gmail.com") == True
    assert validating_email("@") == False

@patch("requests.get")
def test_identifying_breaches(mock_get):
    mock_response = {
        "success" : True,
        "found" : 3,
        "fields" : ["username", "first_name", "address"],
        "sources" : [
            {"name" : "Evony.com", "date" : "2016-07"},
            {"name" : "Wattpad.com", "date" : "2020-11"},
            {"name" : "Zynga.com", "date" : "2023-09"}
        ]
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    email = "zainabfatima0058963@gmail.com"
    api_key = "333e6ffff7e97ae22dc91c2ebaa2d9379c96bf10"
    result = identifying_breaches(email, api_key)

    assert result["success"] == True
    assert result["found"] == 3
    assert "Evony.com" in [source["name"] for source in result["sources"]]
    assert result["fields"] == ["username", "first_name", "address"]

def test_displaying_breaches():
    info = {
        "success": True,
        "found": 3,
        "fields": ["username", "first_name", "address"],
        "sources": [
            {"name": "Evony.com", "date": "2016-07"},
            {"name": "Wattpad.com", "date": "2016-08"},
            {"name": "Zynga.com", "date": "2019-09"}
        ]
    }


    captured_output = StringIO()
    sys.stdout = captured_output

    displaying_breaches(info, "zainabfatima0058963@gmail.com")
    output = captured_output.getvalue()
    assert "The email has been found in 3 breaches." in output
    assert "Evony.com" in captured_output.getvalue()
    assert "Zynga.com" in captured_output.getvalue()

    sys.stdout = sys.__stdout__