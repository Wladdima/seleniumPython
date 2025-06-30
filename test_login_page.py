from models.users import LOGIN_USER


def test_existing_user_can_login(login_page):
    login_page.open()
    login_page.log_in_user(LOGIN_USER)
    login_page.user_should_be_logged_in()
