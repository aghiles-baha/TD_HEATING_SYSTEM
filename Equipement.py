VALID_TYPES = {"Chaudiere", "Radiateur", "Pompe a chaleur", "Chauffe-eau"}


class Equipement:
    def __init__(self, type_equipement: str, annee_installation: int, puissance: int):
        self.type_equipement = type_equipement
        self.annee_installation = annee_installation
        self.puissance = puissance

    def is_valid(self) -> bool:
        if self.type_equipement not in VALID_TYPES:
            return False
        if not isinstance(self.annee_installation, int):
            return False
        if self.annee_installation <= 1995 or self.annee_installation == 2019:
            return False
        if not isinstance(self.puissance, int):
            return False
        if not (1 <= self.puissance <= 50):
            return False
        return True

    def __repr__(self):
        return (
            f"Equipement(type={self.type_equipement!r}, "
            f"annee={self.annee_installation}, "
            f"puissance={self.puissance} kW)"
        )
