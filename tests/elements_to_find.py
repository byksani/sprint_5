from selenium.webdriver.common.by import By


class TestLocators:
    NAME_INPUT_FIELD = By.XPATH, '//label[ text()="Имя" ]/parent::div/input' # Поле ввода имени для авторизации
    EMAIL_INPUT_FIELD = By.XPATH, '//label[ text()="Email" ]/parent::div/input' # Поле ввода email для авторизации
    PASSWORD_INPUT_FIELD = By.XPATH, '//label[ text()="Пароль" ]/parent::div/input' # Поле ввода пароля для авторизации
    REGISTRATION_BUTTON = By.XPATH, '//button[ text()="Зарегистрироваться" ]' # Кнопка "Зарегистрироваться" на странице регистрации
    INPUT_ERROR_TEXT = By.CSS_SELECTOR, ".input__error.text_type_main-default" # Ошибка при невалидных данных при регистрации
    GO_TO_LOGIN_BUTTON = By.XPATH, '//button[ text()="Войти в аккаунт" ]' # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = By.XPATH, '//button[ text()="Войти" ]' # Кнопка "Войти" на странице авторизации
    MAKE_AN_ORDER_BUTTON = By.XPATH, '//button[ text()="Оформить заказ" ]' # Кнопка "Оформить заказ" на главной странице после авторизации
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//a/p[ text()="Личный Кабинет" ]' # Кнопка "Личный кабинет" на главной странице
    LINK_TO_LOGIN_PAGE = By.XPATH, '//p/a[@class="Auth_link__1fOlj"]' # Ссылка на страницу авторизации на странице регистрации
    CONSTRUCTOR_BUTTON = By.XPATH, '//a/p[ text()="Конструктор" ]' # Кнопка "Конструктор" в хедере
    LOGO_BUTTON = By.XPATH, '//div[ @class="AppHeader_header__logo__2D0X2" ]' # Логотип в хедере
    LOGOUT_BUTTON = By.XPATH, '//button[ text()="Выход" ]' # Кнопка "Выход" на странице Личного кабинета
    PUNS_CONSTRUCTOR_BUTTON = By.XPATH, '//span[text()="Булки"]' # Кнопка секции "Булки"
    SAUCES_CONSTRUCTION_BUTTON = By.XPATH, '//span[text()="Соусы"]' # Кнопка секции "Соусы"
    TOPPINGS_CONSTRUCTION_BUTTON = By.XPATH, '//span[text()="Начинки"]' # Кнопка секции "Начинки"
