import json
import pytest
import requests
import time

from pages.moderator import Moderator
from pages.mozillians import Mozillians
from pages.reps import Reps
from pages.standups import Standups
from pages.rptest import RpTest
from tests import conftest

TIME_TO_WAIT_FOR = 900


class TestLogin:

    @pytest.mark.nondestructive
    def test_login_testrp(self, selenium, ldap, token, urls):
        test = RpTest(selenium, urls['testRP'])
        passcode = conftest.passcode(ldap['secret_seed'])
        conftest.write_in_file("passcodes", passcode)
        test.login_with_ldap(ldap['email'], ldap['password'])
        test.enter_passcode(passcode)
        access_token = conftest.access_token(token)
        api = token['api']
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        initial_user_log_date = json.loads(user_logs.content)[0]['date']
        time.sleep(TIME_TO_WAIT_FOR)
        test.refresh_page()
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        last_user_log_type = json.loads(user_logs.content)[0]['type']
        assert last_user_log_type == "ssa"
        current_user_log_date = json.loads(user_logs.content)[0]['date']
        assert current_user_log_date > initial_user_log_date
        test.click_logout()

    @pytest.mark.nondestructive
    def test_login_mozillians(self, selenium, ldap, token, urls):
        test = Mozillians(selenium, urls['mozillians'])
        test.login_with_ldap(ldap['email'], ldap['password'])
        current_passcode = conftest.passcode(ldap['secret_seed'])
        passcode_from_file = conftest.file_content("passcodes")
        while passcode_from_file == current_passcode:
            test.wait_for_passcode_to_change(ldap['secret_seed'], current_passcode)
            current_passcode = conftest.passcode(ldap['secret_seed'])
            passcode_from_file = conftest.file_content("passcodes")
        passcode = conftest.passcode(ldap['secret_seed'])
        conftest.write_in_file("passcodes", passcode)
        test.enter_passcode(passcode)
        access_token = conftest.access_token(token)
        api = token['api']
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        initial_user_log_date = json.loads(user_logs.content)[0]['date']
        time.sleep(TIME_TO_WAIT_FOR)
        test.refresh_page()
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        current_user_log_date = json.loads(user_logs.content)[0]['date']
        assert current_user_log_date > initial_user_log_date
        test.click_logout()

    @pytest.mark.nondestructive
    def test_login_moderator(self, selenium, ldap, token, urls):
        test = Moderator(selenium, urls['moderator'])
        test.login_with_ldap(ldap['email'], ldap['password'])
        current_passcode = conftest.passcode(ldap['secret_seed'])
        passcode_from_file = conftest.file_content("passcodes")
        while passcode_from_file == current_passcode:
            test.wait_for_passcode_to_change(ldap['secret_seed'], current_passcode)
            current_passcode = conftest.passcode(ldap['secret_seed'])
            passcode_from_file = conftest.file_content("passcodes")
        passcode = conftest.passcode(ldap['secret_seed'])
        conftest.write_in_file("passcodes", passcode)
        test.enter_passcode(passcode)
        access_token = conftest.access_token(token)
        api = token['api']
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        initial_user_log_date = json.loads(user_logs.content)[0]['date']
        time.sleep(TIME_TO_WAIT_FOR)
        test.refresh_page()
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        current_user_log_date = json.loads(user_logs.content)[0]['date']
        assert current_user_log_date > initial_user_log_date
        test.logout()

    def test_login_reps(self, selenium, ldap, token, urls):
        test = Reps(selenium, urls['reps'])
        test.login_with_ldap(ldap['email'], ldap['password'])
        current_passcode = conftest.passcode(ldap['secret_seed'])
        passcode_from_file = conftest.file_content("passcodes")
        while passcode_from_file == current_passcode:
            test.wait_for_passcode_to_change(ldap['secret_seed'], current_passcode)
            current_passcode = conftest.passcode(ldap['secret_seed'])
            passcode_from_file = conftest.file_content("passcodes")
        passcode = conftest.passcode(ldap['secret_seed'])
        conftest.write_in_file("passcodes", passcode)
        test.enter_passcode(passcode)
        access_token = conftest.access_token(token)
        api = token['api']
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        initial_user_log_date = json.loads(user_logs.content)[0]['date']
        time.sleep(TIME_TO_WAIT_FOR)
        test.refresh_page()
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        current_user_log_date = json.loads(user_logs.content)[0]['date']
        assert current_user_log_date > initial_user_log_date
        test.click_logout()

    def test_login_standups(self, selenium, ldap, token, urls):
        test = Standups(selenium, urls['standups'])
        test.login_with_ldap(ldap['email'], ldap['password'])
        current_passcode = conftest.passcode(ldap['secret_seed'])
        passcode_from_file = conftest.file_content("passcodes")
        while passcode_from_file == current_passcode:
            test.wait_for_passcode_to_change(ldap['secret_seed'], current_passcode)
            current_passcode = conftest.passcode(ldap['secret_seed'])
            passcode_from_file = conftest.file_content("passcodes")
        passcode = conftest.passcode(ldap['secret_seed'])
        conftest.write_in_file("passcodes", passcode)
        test.enter_passcode(passcode)
        access_token = conftest.access_token(token)
        api = token['api']
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        initial_user_log_date = json.loads(user_logs.content)[0]['date']
        time.sleep(TIME_TO_WAIT_FOR)
        test.refresh_page()
        user_logs = requests.get(api, headers={'Authorization': 'Bearer {0}'.format(access_token)})
        current_user_log_date = json.loads(user_logs.content)[0]['date']
        assert current_user_log_date > initial_user_log_date
        test.click_logout()
