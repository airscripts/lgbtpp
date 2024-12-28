class Questioning:
    def __init__(self) -> None:
        self.name: str = "Questioning"
        self.wiki: str = "https://lgbtqia.fandom.com/wiki/Questioning"

        self.description: str = (
            "Questioning is a term used to describe individuals who are exploring, "
            "learning, or experimenting with their sexual or romantic orientation, "
            "or gender identity. The letter 'Q' in the LGBTQIA+ acronym can sometimes "
            "stand for both 'Queer' and 'Questioning'."
        )

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_wiki_url(self) -> str:
        return self.wiki
