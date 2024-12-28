class Queer:
    def __init__(self) -> None:
        self.name: str = "Queer"
        self.wiki: str = "https://lgbtqia.fandom.com/wiki/Queer"

        self.description: str = (
            "Queer is an identifier for individuals who are not exclusively heterosexual "
            "in their sexual orientation, who use it in reference to their gender identity "
            "and/or gender expression (as a standalone term or part of another like genderqueer), "
            "or who are fluid in their identities, as well as an umbrella term "
            "for the entire community."
        )

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_wiki_url(self) -> str:
        return self.wiki
