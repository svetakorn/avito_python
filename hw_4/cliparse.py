import html
from parsel_selector import selector
import argparse


def create_cliparse(html_text):
    parser = argparse.ArgumentParser()
    parser.add_argument('--xpath',
                        help='xpath to navigate through html',
                        type=str,
                        default='//*')
    args = parser.parse_args()
    print(selector(html_text, args.xpath))


if __name__ == '__main__':
    create_cliparse(html.text)
