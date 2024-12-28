class Gay:
    def __init__(self) -> None:
        self.name: str = "Gay"
        self.wiki: str = "https://lgbtqia.fandom.com/wiki/Gay"

        self.description: str = (
            "Gay is an adjective referring to those with an enduring physical, romantic, "
            "and/or emotional attraction to people of the same gender."
        )

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_wiki_url(self) -> str:
        return self.wiki
