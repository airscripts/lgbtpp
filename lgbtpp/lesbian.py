class Lesbian:
    def __init__(self) -> None:
        self.name: str = "Lesbian"
        self.wiki: str = "https://lgbtqia.fandom.com/wiki/Lesbian"

        self.description: str = (
            "Lesbian is a sexual orientation or romantic orientation most often defined "
            "as a woman who is attracted to other women, with many variations in definitions."
        )

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_wiki_url(self) -> str:
        return self.wiki
