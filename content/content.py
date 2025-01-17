import os
import requests

# définition de l'adresse de l'API
api_address = 'fastapi'
# port de l'API
api_port = 8000
se = '/v1/sentiment'
test_case = [
    {'username': 'alice', 'password': 'wonderland', 'sentence': 'life is beautiful', 'endpoint': '/v1/sentiment'},
    {'username': 'alice', 'password': 'wonderland', 'sentence': 'that sucks', 'endpoint': '/v2/sentiment'},
]


for case in test_case:
    # requête
    r = requests.get(
        url='http://{address}:{port}{endpoint}'.format(address=api_address, port=api_port, endpoint=case["endpoint"]),
        params=case,
    )
  
    try:
        response_json = r.json() if r.status_code == 200 else {}
    except ValueError:
        response_json = {}
    username = case['username']
    sentence = response_json.get('sentence', case['sentence'])
    version = response_json.get('version')
    score = response_json.get('score')
    output = '''
    ============================
        Content test
    ============================

    request done at "{endpoint}"
    | username="{username}"
    | version="{version}"
    | sentence="{sentence}"
    | score= {score}

    expected result = 200
    actual result = {status_code}
    ==>  {test_status}

    '''

    # statut de la requête
    status_code = response_json.get('status_code', r.status_code)
    # affichage des résultats
    if status_code == 200 and score is not None:
        score = float(score)
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(
        username=case['username'],
        status_code=status_code,
        test_status=test_status,
        version=version,
        score=score,
        password=case['password'],
        sentence=case['sentence'],
        endpoint=case['endpoint']
    ))

    # impression dans un fichier
    if os.environ.get('LOG') == '1':
        file_path = os.path.join(os.path.dirname(__file__), '/test/log.txt')
        with open('log.txt', 'a') as file:
            file.write(output.format(username=case['username'], 
                                     status_code=status_code,
                                     test_status= test_status, 
                                     version=version,
                                     score = score, 
                                     password=case['password'], 
                                     sentence=case['sentence'], 
                                     endpoint=case['endpoint']))