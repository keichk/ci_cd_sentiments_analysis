import os
import requests

# définition de l'adresse de l'API
api_address = 'fastapi'
# port de l'API
api_port = 8000
test_case = [
    {'username': 'alice', 'password': 'wonderland', 'sentence': 'hello world', 'endpoint': '/v1/sentiment'},
    {'username': 'bob', 'password': 'builder', 'sentence': 'hello world', 'endpoint': '/v1/sentiment'},
    {'username': 'alice', 'password': 'wonderland', 'sentence': 'hello world', 'endpoint': '/v2/sentiment'},
    {'username': 'bob', 'password': 'builder', 'sentence': 'hello world', 'endpoint': '/v2/sentiment'},
]


for case in test_case:
    # requête
    r = requests.get(
        url='http://{address}:{port}{endpoint}'.format(address=api_address, port=api_port, endpoint=case["endpoint"]),
        params=case
    )
    response_json = r.json()
    username = case['username']
    sentence = response_json.get('sentence', case['sentence'])

    output = '''
    ============================
        Authorization test
    ============================

    request done at "{endpoint}"
    | username="{username}"
    | password="{password}"
    | sentence="{sentence}"

    expected result = 200
    actual result = {status_code}
    ==>  {test_status}

    '''

    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(
        username=case['username'],
        status_code=status_code,
        test_status=test_status,
        password=case['password'],
        sentence=case['sentence'],
        endpoint=case['endpoint']
    ))

    # impression dans un fichier
    if os.environ.get('LOG') == 1:
        with open('log.txt', 'a') as file:
            file.write(output.format(username=case['username'], 
                                     status_code=status_code,
                                     test_status= test_status,
                                     password=case['password'], sentence=case['sentence'], 
                                     endpoint=case['endpoint']))
