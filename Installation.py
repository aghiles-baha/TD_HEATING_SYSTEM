VALID_TYPES = {"Chaudiere", "Radiateur", "Pompe a chaleur", "Chauffe-eau"}



class Installation:
    def __init__(self, surface: float, equipements: list, zones: list):
        self.surface = surface
        self.equipements = equipements  # list[Equipement]
        self.zones = zones              # list[Zone]

    def is_valid(self) -> bool:
        # Surface multiple de 10 et < 300 m²
        if self.surface % 10 != 0 or self.surface >= 300:
            return False

        # Zones couvrent toute la surface
        total_zones = sum(z.surface for z in self.zones)
        if total_zones != self.surface:
            return False

        for zone in self.zones:
            # Chaque zone a une surface > 0
            if zone.surface <= 0:
                return False
            # Chaque zone est associée à un équipement existant dans la liste
            if zone.equipement not in self.equipements:
                return False

        return True

    def __repr__(self):
        return (
            f"Installation(surface={self.surface} m², "
            f"{len(self.equipements)} équipements, "
            f"{len(self.zones)} zones)"
        )