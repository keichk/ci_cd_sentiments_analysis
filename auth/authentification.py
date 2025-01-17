import os
import requests

# définition de l'adresse de l'API
api_address = 'fastapi'
# port de l'API
api_port = 8000
test_case =[{'username': 'alice', 'password': 'wonderland'},
            {'username': 'bob', 'password': 'builder'},
            {'username': 'alice', 'password': 'clementine'},
            {'username': 'bob', 'password': 'mandarine'}]


for case in test_case:
    # requête
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
        params= case
    )

    output = '''
    ============================
        Authentication test
    ============================

    request done at "/permissions"
    | username="{username}"
    | password="{password}"

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
    print(output.format(username=case['username'], password=case['password'], status_code=status_code, test_status=test_status))

    # impression dans un fichier
    if os.environ.get('LOG') == '1':
        with open('log.txt', 'a') as file:
            file.write(output.format(username=case['username'], password=case['password'], status_code=status_code, test_status=test_status))

