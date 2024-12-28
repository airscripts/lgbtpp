class TwoSpirit:
    def __init__(self) -> None:
        self.name: str = "Two-Spirit"
        self.wiki: str = "https://lgbtqia.fandom.com/wiki/Two-Spirit"

        self.description: str = (
            "Two-Spirit refers to a strictly Native identity that describes a person "
            "who identifies as having both a masculine and feminine spirit."
        )

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_wiki_url(self) -> str:
        return self.wiki
