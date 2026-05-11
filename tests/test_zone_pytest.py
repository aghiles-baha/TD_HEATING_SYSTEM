import pytest
 import Equipement, Zone


class TestZone:

    def _make_equipement(self):
        return Equipement("Chaudiere", 2000, 20)

    def test_zone_creation(self):
        e = self._make_equipement()
        z = Zone("Salon", 50, e)
        assert z.nom == "Salon"
        assert z.surface == 50
        assert z.equipement is e

    def test_zone_surface_positive(self):
        e = self._make_equipement()
        z = Zone("Chambre", 30, e)
        assert z.surface > 0

    def test_zone_surface_zero(self):
        e = self._make_equipement()
        z = Zone("Salle de bain", 0, e)
        assert z.surface == 0

    def test_zone_equipement_associe(self):
        e = self._make_equipement()
        z = Zone("Salon", 50, e)
        assert z.equipement is e

    def test_zone_repr(self):
        e = self._make_equipement()
        z = Zone("Salon", 50, e)
        assert "Salon" in repr(z)
        assert "50" in repr(z)
