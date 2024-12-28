class Intersex:
    def __init__(self) -> None:
        self.name: str = "Intersex"
        self.wiki: str = "ttps://lgbtqia.fandom.com/wiki/Intersex"

        self.description: str = (
            "Intersex is an umbrella term for people who are born with or develop sex "
            "characteristics that differ from the binary notions of a 'male' or 'female' body."
        )

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_wiki_url(self) -> str:
        return self.wiki
