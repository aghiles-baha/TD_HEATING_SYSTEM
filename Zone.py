VALID_TYPES = {"Chaudiere", "Radiateur", "Pompe a chaleur", "Chauffe-eau"}



class Zone:
    def __init__(self, nom: str, surface: float, equipement: Equipement):
        self.nom = nom
        self.surface = surface
        self.equipement = equipement

    def __repr__(self):
        return f"Zone(nom={self.nom!r}, surface={self.surface} m²)"
