import requests

base_url = "https://ru.yougile.com"
#получить список компаний
def test_get_list_company(login = 'Ladi1993@mail.ru', password = '19932009q94374218'):
    creds = {
        'login': login,
        'password': password
        }
    resp = requests.post(base_url + '/api-v2/auth/companies',json=creds)
    return resp.json()["content"],["id"]
    assert resp.status_code == 200


def test_auth():
    creds_2 = {
        'login': 'Ladi1993@mail.ru',
        'password': '19932009q94374218',
        'companyId': '1b457e57-9bda-4612-890d-789a8d7fc59c'
        }
    resp= requests.post(base_url + '/api-v2/auth/keys',json=creds_2)
    return resp.json()["key"]
    assert resp.status_code == 200

#создание проекта(внутри компании)

def test_get_company_pozitiv(key = 'wu-X3SHwd0IxDGP-zpkR+q8ptJhdD5BvhH-BHuRuCYq6+z9mrLo6jwdF7wJz3sNc',
                             base_url="https://ru.yougile.com"):
    resp = requests.get(base_url + '/api-v2/projects')
    return resp.json()


def test_get_company_negative(key = 'wu-X3SHwd0IxDGP-zpkR+q8ptJhdD5BvhH-BHuRuCYq6+z9mrLo6jwdF7wJz3sNc',
                              base_url="https://ru.yougile.com"):
    resp = requests.get( + '/api-v2/projects')
    return resp.json()

def test_create_new_project_poz():
    headers = {
        'key': 'wu-X3SHwd0IxDGP-zpkR+q8ptJhdD5BvhH-BHuRuCYq6+z9mrLo6jwdF7wJz3sNc'
    }
    company = {
        'title': 'python'
    }
    return requests.post(base_url + '/api-v2/projects', headers=headers,
                         json=company)
    assert resp.status_code == 201



def test_create_new_project_neg():
    headers = {
        'key' : 'wu-X3SHwd0IxDGP-zpkR+q8ptJhdD5BvhH-BHuRuCYq6+z9mrLo6jwdF7wJz3sNc'
    }
    company = {
        'title': 'python'
    }
    return requests.post( + '/api-v2/projects',headers=headers,
                         json=company)
    assert resp.status_code == 201

def test_change_prodject_poz():
    headers = {
        'key': 'wu-X3SHwd0IxDGP-zpkR+q8ptJhdD5BvhH-BHuRuCYq6+z9mrLo6jwdF7wJz3sNc'
    }
    project = {
        'deleted' : 'False',
        'title':'python_1'
    }
    return requests.put(base_url + '/api-v2/projects/{cdad9022-0ad7-40ed-8afd-c1924e117071}', headers=headers,
                         json=project)
    assert resp.status_code == 201

def test_change_prodject_neg():
    headers = {
        'key': 'wu-X3SHwd0IxDGP-zpkR+q8ptJhdD5BvhH-BHuRuCYq6+z9mrLo6jwdF7wJz3sNc'
    }
    project = {
        'deleted' : 'True',
        'title':'python_1'
    }
    return requests.put( + '/api-v2/projects/{cdad9022-0ad7-40ed-8afd-c1924e117071}', headers=headers,
                         json=project)
    assert resp.status_code == 201



