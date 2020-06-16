from enum import Enum

from gethtml import get_soup

class History():
    """
    コンテスト成績表
    """
    Item = Enum("Item", "date contest rank perf rating diff")

    def __init__(self, name):
        soup = get_soup(f"https://atcoder.jp/users/{name}/history")
        trs = soup.table.tbody.find_all("tr")
        trs = [tr for tr in trs if tr != "\n"]
        def to_text():
            for tr in trs:
                yield [td.text.strip() for td in tr.contents if td != "\n"][:-1]
        self.rows = tuple(to_text())
        self.columns = tuple(zip(*self.rows))

    def column(self, item):
        if isinstance(item, int):
            i = item
        else:
            i = History.Item[item].value - 1
        return self.columns[i]

    def row(self, i):
        return self.rows[i]

    __getattr__ = column


def check():
    history = History("AgeashiParrot")
    print(*history.column(4))
    print(*history.perf)


if __name__ == "__main__":
    check()