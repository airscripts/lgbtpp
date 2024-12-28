class Plus:
    def __init__(self) -> None:
        self.name: str = "Plus"
        self.wiki: str = "https://lgbtqia.fandom.com/"

        self.description: str = (
            "The + stands for all other members of the community."
        )

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_wiki_url(self) -> str:
        return self.wiki
