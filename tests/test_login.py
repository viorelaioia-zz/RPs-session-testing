import json
import pytest
import requests
import time

from tests import conftest
from pages.rptest import RpTest


class TestLogin:

    @pytest.mark.nondestructive
    def test_login(self, selenium, ldap, token, urls):
        test = RpTest(selenium, urls['testRP'])
        test.login_with_ldap(ldap['email'], ldap['password'], conftest.passcode(ldap['secret_seed']))
        access_token = conftest.access_token(token)
        api = token['api']
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        initial_user_log_date = json.loads(user_logs.content)[0]['date']
        time.sleep(16)
        test.refresh_page()
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        current_user_log_date = json.loads(user_logs.content)[0]['date']
        assert current_user_log_date > initial_user_log_date
        last_user_log_type = json.loads(user_logs.content)[0]['type']
        assert last_user_log_type == "ssa"
