class Transgender:
    def __init__(self) -> None:
        self.name: str = "Transgender"
        self.wiki: str = "https://lgbtqia.fandom.com/wiki/Transgender"

        self.description: str = (
            "Transgender, often shortened to trans, is an umbrella term that describes "
            "an individual whose gender identity differs from their assigned "
            "gender at birth (AGAB)."
        )

    def get_description(self) -> str:
        return self.description

    def get_wiki_url(self) -> str:
        return self.wiki

    def get_name(self) -> str:
        return self.name
