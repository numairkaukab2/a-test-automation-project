import requests

def test_api():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    r_body = response.json()

    
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"
    assert r_body["name"] == "Leanne Graham"
    assert r_body["company"]["bs"] == "harness real-time e-markets"
    
    