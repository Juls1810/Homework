import requests

base_url = "https://ru.yougile.com"
id_company = "1b457e57-9bda-4612-890d-789a8d7fc59c"
api_key = ""
user_id = "a441852e-de85-4c7f-8731-2ede92ada79b"


def test_create_new_project_poz():
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    body = {
        'title': 'python',
        "users": {
            user_id: "admin"
        }
    }
    resp = requests.post(base_url + '/api-v2/projects', headers=headers,
                         json=body)
    print(resp.json()["id"])
    assert resp.status_code == 201
    assert resp.json()["id"] != ""


def test_create_new_project_neg():
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    body = {
        'title': 'python',
        "id": "123",
        "users": {
            user_id: "admin"
        }
    }
    resp = requests.post(base_url + '/api-v2/projects', headers=headers,
                         json=body)
    assert resp.status_code == 400


def test_change_project_poz():
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    body = {
        "deleted": False,
        'title': 'python',
        "users": {
            user_id: "admin"
        }
    }
    resp = requests.put(base_url + '/api-v2/projects/ab44b773-c768-40cc-b662-54c21f3ef9c0',
                        headers=headers, json=body)

    assert resp.status_code == 200
    assert resp.json()["id"] != ""


def test_change_project_neg():
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    body = {
        "deleted": False,
        'title': 'python',
        "users": {
            user_id: "admin"
        }
    }
    resp = requests.put(base_url + '/api-v2/projects/ab44b773-c768-40cc-b6',
                   headers=headers, json=body)
    assert resp.status_code == 404


def test_project_list_poz():
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    resp = requests.get(base_url + '/api-v2/projects/ab44b773-c768-40cc-b662-54c21f3ef9c0', headers=headers)
    assert resp.status_code == 200
    assert resp.json()["id"] == "ab44b773-c768-40cc-b662-54c21f3ef9c0"
    assert resp.json()["title"] == "python"


def test_project_list_neg():
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    resp = requests.get(base_url + '/api-v2/projects/ab44b77', headers=headers)
    assert resp.status_code == 404
