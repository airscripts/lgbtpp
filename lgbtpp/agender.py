class Agender:
    def __init__(self) -> None:
        self.name: str = "Agender"
        self.wiki: str = "https://lgbta.wikia.org/wiki/Agender"

        self.description: str = (
            "Agender, also known as genderless, is a gender identity that has "
            "been defined in several ways. "
            "It can mean having no gender at all (literal meaning) or not feeling a gender. "
            "Some people who identify as agender may experience gender neutrality, "
            "rejecting the gender binary of male/female, man/woman, or masculine/feminine. "
            "Others might not identify with any gender, finding the concept of "
            "gender irrelevant or choosing to reject it entirely. "
            "For some, rejecting the concept of gender is not "
            "just a personal choice, but a broader dismissal of gender as a whole."
        )

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_wiki_url(self) -> str:
        return self.wiki
