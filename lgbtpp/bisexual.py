class Bisexual:
    def __init__(self) -> None:
        self.name: str = "Bisexual"
        self.wiki: str = "https://lgbtqia.fandom.com/wiki/Bisexual"

        self.description: str = (
            "Bisexual, also abbreviated as bi, is a sexual orientation encompassing attraction "
            "to multiple genders and/or sexes, with the attraction being sexual, romantic, "
            "and/or emotional."
        )

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_wiki_url(self) -> str:
        return self.wiki
