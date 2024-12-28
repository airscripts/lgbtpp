class Aromantic:
    def __init__(self) -> None:
        self.name: str = "Aromantic"
        self.wiki: str = "https://lgbta.wikia.org/wiki/Aromantic"

        self.description: str = (
            "Aromantic, often shortened to aro, describes people who do not experience romantic "
            "attraction, or experience little-to-no romantic attraction."
        )

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_wiki_url(self) -> str:
        return self.wiki
