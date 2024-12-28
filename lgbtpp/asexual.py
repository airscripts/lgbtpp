class Asexual:
    def __init__(self) -> None:
        self.name: str = "Asexual"
        self.wiki: str = "ttps://lgbtqia.fandom.com/wiki/Asexuality"

        self.description: str = (
            "Asexual refers to people who do not experience sexual attraction toward others, "
            "as well as people who experience limited or conditional sexual attraction and relate "
            "to the label asexual more than other sexual identity terms."
        )

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_wiki_url(self) -> str:
        return self.wiki
