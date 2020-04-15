from parsel import Selector


def selector(text: str, xpath: str) -> str:
    sel = Selector(text=text)
    return sel.xpath(xpath).get()
