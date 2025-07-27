from selene import browser

def test_search_by_tag():
    browser.element('h1')
    browser.all()

# <div id="main-container">Контент главного контейнера</div>
def test_search_by_id():
    browser.element('#main-container')


# <p class="intro-text other-class-name-1 another-name-3">Это первый параграф с именем классом intro-text. (в том
#     числе)</p>
# <p class="intro-text">Это второй параграф, в котором есть имя класса intro-text</p>
def test_search_by_class_name():
    # поиск по атрибуту class, где селектор состоит из нескольких имен, каждое из которых передается слитно через точку
    browser.element(
        ".intro-text.other-class-name-1.another-name-3")  # -> Это первый параграф с именем классом intro-text.
    # (в том числе)

    # поиск по имени класса
    browser.element(".intro-text")  # Поиск первого элемента с классом "intro-text"

    # В данном случае вернется элемент параграф с текстом 'Это первый параграф с именем классом intro-text.
    # (в том числе)', так как:
    # 1. всегда возвращается первый найденный элемент
    # 2. поиск был по всему DOM.

# <a href="https://example.com" title="Пример ссылки">Пример ссылки</a>
# <button data-action="submit-form">Отправить</button>

def search_by_attr():
    browser.element('[title="Пример ссылки"]')
    # Поиск элемента с title="Пример ссылки"
    browser.element('[data-action="submit-form"]')
    # Поиск элемента с data-action="submit-form"

def test_search_by_attr():
# CSS позволяет выполнять частичный поиск по значению атрибута. Вот основные варианты:
# Используйте ^= для поиска по атрибуту, начинающемуся с определенной строки
    browser.element('[name^="user"]')  # Найдет элемент с name="user_name"
# Используйте $= для поиска по атрибуту, заканчивающемуся на определенную строку
    browser.element('[name$="user"]')  # Найдет элемент с name="contact_email_user"
# Используйте *= для по атрибуту, содержащему подстроку
    browser.all('[name*="user"]')  # Найдет все элементы с подстрокой "user" в name
# Этот запрос найдет и user_name, и phone_user_contact, и contact_email_user.

# Вы также можете использовать сложные селекторы, чтобы находить элементы по их порядку, например:
    browser.element('input:nth-of-type(2)')
# Что вернет следующий элемент, так как он второй по списку. Отсчёт начинается с единицы, а не нуля.
