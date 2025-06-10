import requests

def test_api_get():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    r_body = response.json()

    
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"
    assert r_body["name"] == "Leanne Graham"
    assert r_body["company"]["bs"] == "harness real-time e-markets"
    
def test_api_post():
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data={
    "userId": 1,
    "title": "My blog post title",
    "body": "This is the text of my latest blog post."
    })
    
    assert response.status_code == 201
    assert type(response.json()["id"]) == int