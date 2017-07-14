import json
import pyotp
import pytest
import requests


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


@pytest.fixture
def passcode(secret_seed):
    totp = pyotp.TOTP(secret_seed)
    return totp.now()


@pytest.fixture
def ldap(variables):
    return variables['ldap_user']


@pytest.fixture
def token(variables):
    return variables['token']


@pytest.fixture
def urls(variables):
    return variables['RPs_urls']


@pytest.fixture
def access_token(token):
    headers = {'content-type': 'application/json'}
    data = {
        "client_id": token['client_id'],
        "client_secret": token['client_secret'],
        "audience": token['audience'],
        "grant_type": "client_credentials"
    }
    response = requests.post(token['url'], data=json.dumps(data), headers=headers)
    return json.loads(response.content)['access_token']


@pytest.fixture
def file_content(filename):
    return open(filename, 'r').read()


@pytest.fixture
def write_in_file(filename, content):
    f = open(filename, 'w')
    f.write(content)  # python will convert \n to os.linesep
    f.close()
