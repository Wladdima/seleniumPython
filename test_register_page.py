import allure
from models.users import generate_user


@allure.story("Product")
@allure.feature("Product list")
@allure.title("New user can register")
def test_new_user_can_register(register_page):
    new_user = generate_user()

    register_page.open()
    register_page.register_new_user(new_user)
    register_page.user_should_be_registered()
