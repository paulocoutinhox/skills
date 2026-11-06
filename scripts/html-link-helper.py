from html.parser import HTMLParser


class HtmlLinkHelper(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name in {"src", "href"} and value is not None:
                self.targets.append(value)

    @classmethod
    def links(cls, content: str) -> list[str]:
        parser = cls()
        parser.feed(content)
        parser.close()
        return parser.targets
