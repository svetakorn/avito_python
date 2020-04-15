import requests
from parsel import Selector
import re


BASE_URL = 'https://175g.ru'
START_URL = BASE_URL + '/players/'


def parse(resp: requests.Response):
    """Собирает ссылки на страницы игроков"""
    sel = Selector(resp.text)

    player_css = '.pl-player > .pl-player-name > a::attr(href)'
    tasks = [(BASE_URL + url, parse_player) for url in sel.css(player_css).getall()]

    return tasks


def parse_player(resp: requests.Response):
    """Собирает информацию о каждом игроке"""
    sel = Selector(resp.text)

    name = sel.css('h1::text').get().strip()
    teams = sel.css('.player-teams a::text').getall()

    player_info = {
        'name': name,
        'teams': teams,
        'teams_cnt': len(teams)
              }

    player_stats = stats_to_dict(get_player_stats(sel))

    player = {**player_info, **player_stats}
    print(player)
    return [player]


def get_player_stats(sel: Selector) -> list:
    """Обрабатывает информацию об игроке"""
    raw_values = sel.xpath('//div[@class="player-stat-cell"]//text()')\
        .getall()
    processed_values = [r.strip() for r in raw_values if r.strip() != '']
    concat = [i + ' ' + j for i, j in zip(processed_values[::2], processed_values[1::2])]
    return concat


def stats_to_dict(stats: list) -> dict:
    """Создает словарь с данными каждого игрока"""
    metrics = {'tournaments': 'турнир',
               'countries': 'стран',
               'finals': 'финал',
               'first places': 'мест',
               'spirit of the game': 'ДИ',
               'MVP': 'MVP',
               'tournaments organized': 'рганизовал'}

    stats_dict = {'tournaments': '',
                  'countries': '',
                  'finals': '',
                  'first places': '',
                  'spirit of the game': '',
                  'MVP': '',
                  'tournaments organized': ''}

    for k, v in metrics.items():
        for st in stats:
            if v in st:
                stats_dict[k] = re.findall('\d+', st)[0]

    return stats_dict

