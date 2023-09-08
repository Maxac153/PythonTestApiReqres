# PythonTestApiReqres

## Описание

Цель проекта: получения навыков в написании API авто тестов на Python<br>
Сайт для тестирования (<a href="https://reqres.in/">REQRES</a>).

## Окружение

Перед тем как запускать тесты нужно установить необходимые зависемости<br>
Введите следующую команду (нужно находиться внутри папки проекта):<br>
<b>pip install -r requirements.txt</b>

## Запуск тестов

Для запуска тестов нужно ввести следующую команду</br>
<b>py.test --alluredir=allure_report tests/</b>

Для просмотра результатов тестов</br>
<b>allure serve allure_report/</b>

## Технологии

- Python 3.11.2
- Pytest
- csv
- Allure
- Requests
- Jenkins

## Пример запуска тестов

<img src="img/allure_start.png" width="800" height="250">

## Пример Allure отчёта

<img src="img/allure_report.png" width="800" height="400">

## Пример Allure отчёта в Jenkins

<img src="img/allure_report_jenkins.png" width="800" height="400">
