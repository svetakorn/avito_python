Перед запуском нужно установить все зависимости:

`pip install -r requirements.txt`

## Теперь поехали!

Это решения такой домашки по тестам:

https://github.com/siauPatrick/mai-python/blob/master/03-instrumenty-testirovaniya-v-python/issues.md

----

### **issue-01** - файл `test_issue_01.py`

Команда запуска

`python -m doctest -v test_issue_01.py`

Вывод

```
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('MAI-PYTHON-2019') # doctest: +ELLIPSIS
Expecting:
    '-- .- .. ... .---- ----.'
ok
Trying:
    encode(3.14) # doctest: +IGNORE_EXCEPTION_DETAIL
Expecting:
    Traceback (most recent call last):
    TypeError: input must be string
ok
Trying:
    encode('строка для exception') # doctest: +IGNORE_EXCEPTION_DETAIL
Expecting:
    Traceback (most recent call last):
    KeyError: 'с'
ok
1 items had no tests:
    issue-01
1 items passed all tests:
   4 tests in issue-01.encode
4 tests in 2 items.
4 passed and 0 failed.
Test passed.
```

Итог: все тесты пройдены

----

### **issue-02** - файл `test_issue_02.py`

Команда запуска

`pytest test_issue_02.py`

Вывод

```
test_issue_02.py ....                                                                                                              [100%]

======================================================== 4 passed in 0.05 seconds ========================================================
```

Итог: все тесты пройдены

----

### **issue-03** - файл `test_issue_03.py`

Команда запуска

`python -m unittest test_issue_03.py`

Вывод

```
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

Итог: все тесты пройдены

----

### **issue-04** - файл `test_issue_04.py`

Команда запуска

`pytest test_issue_04.py`

Вывод

```
test_issue_04.py ....xx.                                                                                                           [100%]

================================================== 5 passed, 2 xfailed in 0.10 seconds ===================================================
```

Итог: все тесты пройдены

----

### **issue-05** - файл `test_issue_05.py`

Команда запуска

`pytest test_issue_05.py`

Вывод

```
test_issue_05.py ...                                                                                                               [100%]

=========================================================== 3 passed in 0.06s ============================================================
```

Итог: все тесты пройдены

Чтобы увидеть coverage, нужно выполнить команду:

`python -m pytest --cov . --cov-report html`

Результат: `what_is_year_now.py` покрыт полностью тестами, кроме `main` (это можно посмотреть в htmlcov/index.html)

