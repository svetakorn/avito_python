import requests
from parsel import Selector
import re
from scraper.decorators.decorators import timer, memoize
from typing import Iterable, Dict

BASE_URL = 'https://175g.ru'
START_URL = BASE_URL + '/players/'

METRICS = {'tournaments': 'турнир',
           'countries': 'стран',
           'finals': 'финал',
           'first places': 'мест',
           'spirit of the game': 'ДИ',
           'MVP': 'MVP',
           'tournaments organized': 'рганизовал'}

STAT_LABELS = ('tournaments',
               'countries',
               'finals',
               'first places',
               'spirit of the game',
               'MVP',
               'tournaments organized')


@timer
def parse(resp: requests.Response) -> Iterable:
    """Собирает ссылки на страницы игроков"""
    sel = Selector(resp.text)

    player_css = '.pl-player > .pl-player-name > a::attr(href)'
    tasks = [(BASE_URL + url, parse_player) for url in sel.css(player_css).getall()]

    return tasks


@timer
@memoize
def parse_player(resp: requests.Response) -> Iterable:
    """
    Собирает информацию о каждом игроке.
    Мемоизация здесь нужна, чтобы при повторении одно и того же url
    на стартовой странице, не собирать информацию по нему 2 раза
    """
    sel = Selector(resp.text)

    name = sel.css('h1::text').get().strip()
    teams = sel.css('.player-teams a::text').getall()

    player_info = {
        'url': resp.url,
        'name': name,
        'teams': teams,
        'teams_cnt': len(teams)
    }

    player_stats = stats_to_dict(get_player_stats(sel))

    player = {**player_info, **player_stats}
    return [player]


@timer
def get_player_stats(sel: Selector) -> Iterable:
    """Обрабатывает информацию об игроке"""
    raw_values = sel.xpath('//div[@class="player-stat-cell"]//text()') \
        .getall()
    processed_values = [r.strip() for r in raw_values if r.strip() != '']
    concat = [i + ' ' + j for i, j in zip(processed_values[::2], processed_values[1::2])]
    return concat


@timer
def stats_to_dict(stats: Iterable) -> Dict:
    """Создает словарь с данными каждого игрока"""

    stats_dict = dict.fromkeys(STAT_LABELS, '')

    for k, v in METRICS.items():
        for st in stats:
            if v in st:
                stats_dict[k] = re.findall('\d+', st)[0]

    return stats_dict
