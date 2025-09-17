import json
import requests
from jsonschema import validate
from schemas import create_user, update_user, list_users, single_user, error_schema
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE = "https://reqres.in/api"
headers = {"x-api-key": "reqres-free-v1"}

def test_get_users_list():
    r = requests.get(f"{BASE}/users", verify=False, params={"page": 2})
    assert r.status_code == 200
    validate(r.json(), list_users)

def test_get_single_user():
    r = requests.get(f"{BASE}/users/2", verify=False, headers=headers)
    assert r.status_code == 200
    validate(r.json(), single_user)

def test_get_single_user_404():
    r = requests.get(f"{BASE}/users/13", verify=False, headers=headers)
    assert r.status_code == 404
    assert r.json() == {}

def test_post_create_user_schema_from_file():
    payload = {"name": "morpheus", "job": "leader"}
    r = requests.post(f"{BASE}/users", verify=False, json=payload, headers=headers)
    assert r.status_code == 201
    with open("post_users.json", encoding="utf-8") as f:
        validate(r.json(), create_user)

def test_post_register_missing_password():
    payload = {"email": "sydney@fife"}
    r = requests.post(f"{BASE}/register", verify=False, json=payload, headers=headers)
    assert r.status_code == 400
    validate(r.json(), error_schema)

def test_put_update_user():
    payload = {"name": "neo", "job": "the one"}
    r = requests.put(f"{BASE}/users/2", verify=False, json=payload, headers=headers)
    assert r.status_code == 200
    validate(r.json(), update_user)

def test_delete_user():
    r = requests.delete(f"{BASE}/users/2", verify=False, headers=headers)
    assert r.status_code == 204
    assert r.text == ""