from scraper import engine
from scraper.spiders import ultimate


def execute(args):
    engine.start(ultimate.START_URL, ultimate.parse, args.outfile, args.format, args.progress)
