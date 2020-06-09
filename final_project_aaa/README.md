Перед запуском нужно установить все зависимости:

`pip install -r requirements.txt`

Это решение задачки на экзамене:

## Fibonacci 

- написать функцию `fibonacci_iter()` возвращающую последовательность Фибоначчи
- написать функцию `fibonacci(n: int)` возвращающую число по индексу из последовательности
- использовать кеш для ответа `fibonacci_iter()` по ключу индекса
- например: `fibonacci(6) == 8`
----

Команда запуска тестов

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

`pytest`

Вывод

```
....
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

Итог: все тесты пройдены

----

Можно посмотреть покрытие

`coverage report -m `

Вывод - (2 непокрытые строки - это из main)

```
Name                                                          Stmts   Miss  Cover   Missing
-------------------------------------------------------------------------------------------
fibonacci.py           25      2    92%   47-48
test_fibonacci.py      47      0   100%
-------------------------------------------------------------------------------------------
TOTAL                                                            72      2    97%

```