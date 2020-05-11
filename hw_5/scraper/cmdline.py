import argparse
from scraper.commands import crawl

SIGN_STDOUT = 'stdout'

FORMAT_CSV = 'csv'
FORMAT_JL = 'jl'
MONGO_DB = 'mongodb'

PROGRESS_ON = 'on'
PROGRESS_OFF = 'off'


def parse():
    parser = argparse.ArgumentParser(prog='scraper')
    subparsers = parser.add_subparsers()

    parser_crawl = subparsers.add_parser('crawl')
    parser_crawl.add_argument('-o', '--outfile', metavar='FILE', default=SIGN_STDOUT)
    parser_crawl.add_argument('-p', '--progress', default=PROGRESS_ON, choices=[PROGRESS_ON, PROGRESS_OFF])
    parser_crawl.add_argument('-f', '--format', default=MONGO_DB, choices=[FORMAT_CSV, FORMAT_JL, MONGO_DB, SIGN_STDOUT])
    parser_crawl.set_defaults(func=crawl.execute)

    args = parser.parse_args()
    args.func(args)
