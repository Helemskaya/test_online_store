Проект по автоматизации тестирования интернет-магазина: vasko.ru

Цель: 
Провести тестирование маршрута пользователя: Авторизация и прохождение всего бизнес пути интернет-магазина на примере покупки товара с установленными фильтровыми значениями.

Описание проекта: 
Проект по Автоматизации Тестирования выполнен на языке Python 3.12.9 в интегрированной среде разработки PyCharm 2023.3.5 (Community Edition), оперционная систем Windows 10.0, на Firefox Browser Версия 136.0.2 (64-разрядный), 23 марта 2025 г. Проект построен по модели POM (Page Object Model), что позволяет в дальнейшем использовать его как базис для построения новых тестов.

Директории: 
1)	base - содержит различные базовые методы: 
  получение текущего URL: get_current_url,
  валидация по URL: assert_url,
  валидация по строчному значению: assert_word,
  создания скриншотов окна браузера: get_screenshot.
2)  logs - место хранения текстовых логов прохождения тестов
3)  pages - хранит POM классы страниц c используемыми на странице: 
  Locators – локаторы элементов, которые находятся на странице,
  Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска
  Actions - методы, которые будут принимать результат поиска от Getters и производить требуемой действие, например кликать или вводить требуемую информацию,
  Methods - метод, содержащий список Actions, представленных в виде действий.
4)	screen - создаваемые скриншоты, методом get_screenshot, 
5)  tests - хранит тест или группу тестов в пределах одного или нескольких файла(-ов). Содержит в себе методы непосредственно выполняющие тестирование. Также в данной папке находится файл conftest.py, который содержит параметры pytest для запуска параметризированных тестов.
6)  utilities - содержит код с помощью которого производится логгирование действий и записываются логи теста(-ов)

Файлы:
README.md - содержит описание данного проекта

Шаги теста - test_buy_product.py:
1.	Тестирование Авторизации на Веб-сайте:
Получение текущего URL: get_current_url
Введение логина и пароля, 
Нажатие на кнопку "Авторизироваться", 
Нажатие на иконку пользователя 
Проверка подтверждения входа в аккаунт, с помощью assert_word сравнения по
ключевой фразе на странице.

2.	Выбор продукта и прохождение всего бизнес пути (Выбор продукта - Добавление в Корзину - Покупка):
Получение текущего URL: get_current_url
Переход на страницу "Для дома", 
Выбор категории искомого продукта: "Стиральные машины", 
Установка "Фильтров": 
минимальная цена - 30000, 
максимальная цена - 35000, 
производитель - "Candy", 
наличие функции "сушка" - есть, 
получение скриншота страницы для подтверждения установки фильтров, 
проверка с помощью assert_word названия и цены выбранной модели, 
нажатие кнопки выбрать товар, 
нажатие кнопки перехода на страницу корзины пользователя, 
проверка url для подтверждения перехода на страницу корзины пользователя,
Получение текущего URL: get_current_url,
проверка с помощью assert_word названия и цены выбранной модели в корзине пользователя, 
проверка с помощью assert_word общей стоимости товаров в корзине пользователя,
получение скриншота страницы корзины пользователя, 
нажатие кнопки "Оформить заказ", 
проверки url для подтверждения перехода на страницу оформления заказа,
Получение текущего URL: get_current_url,
заполнение данных на странице способа получения товара с помощью библиотеки Faker, 
нажатие кнопки "Продолжить", 
проверка url для подтверждения перехода на страницу контактной информации,
Получение текущего URL: get_current_url,
заполнение данных на странице контактной информации с помощью библиотеки Faker, 
нажатие кнопки "Продолжить", 
проверка url для подтверждения перехода на страницу подтверждения оформления заказа,
Получение текущего URL: get_current_url,
получение скриншота страницы подтверждения оформления заказа,
(Условно)Успешное завершение теста

3. В тесте имеется собственная система логгирования и подключен allure-pytest для вывода отчётов и удобства для работы с итоговыми результатами.

Запуск теста через терминал:

py.test --alluredir=%allure_result_folder% ./tests

allure serve %allure_result_folder%
