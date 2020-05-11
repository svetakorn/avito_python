# Scraper
-----
**UPD от 11.05.2020:**
- добавлена возможность записи в MongoDB
- добавлена возможность вывода в stdout
- для каждого спрасенного элемента указан его URL
- добавлен агрумент для возможности вывода прогресса парсинга в консоль
- добавлено логирование времени выполнения некоторых функций и мемоизация (с помощью декораторов `@timer` и `@memoize`)
- для декораторов `@timer` и `@memoize` написаны unit-тесты
-----

### Overview
Scraper - простой, синхронный веб-краулер и веб-скрейпер, созданный в обущающих целях  
Собирает данные об игроках, играющих в алтимат-фрисби в России с сайта https://175g.ru/players

### Install
Устанавливаем зависимости
```shell script
pip install -r requirements/dev.txt
```

### Commands
Запуск краулера
```shell script
python -m scraper crawl [options]
```
&nbsp;&nbsp;&nbsp;&nbsp;Supported options:
  - ```--outfile=FILE``` or ```-o FILE```: файл, в который будут сохранены собранные данные `(по умолчанию stdout)`
  - ```--progress=PROGRESS``` or ```-f PROGRESS```: нужен ли вывод прогресса в консоль {on, off} `(по умолчанию on)`
  - ```--format=FORMAT``` or ```-f FORMAT```: формат файла с собранными данными {csv, jl, mongodb} `(по умолчанию mongodb)`
  
### Особенности использования

Если указать название файла, то вывод в формате csv/jl будет в файл:
```
python -m scraper crawl -f csv -o test
```

Если не указывать название файла, то вывод в формате csv/jl будет в stdout (без дополнительных действий - в консоль):
```
python -m scraper crawl -f csv
```

Для MondoDB вывода в stdout/файл происходить не будет, только запись в базу:
```
python -m scraper crawl -f mongodb
```

БД MongoDB поднята с помощью докера:
```
mongodb://localhost:32769 -> scraper_db -> rus_ultimate_players
```

### Аналитика

* Спарсенные данные в файле **_rus_ultimate_players.csv_**.
* В файле **_some_analytics.ipynb_** находится визуализация собранного датасета.

### Запуск тестов
Тесты для декораторов - все пройдены:
```
python -m unittest scraper/decorators/test_decorators.py
```
