import pytest
from models import Equipement, Installation, Zone


class TestInstallation:

    def _make_valid_installation(self):
        e = Equipement("Chaudiere", 2000, 20)
        z1 = Zone("Salon", 60, e)
        z2 = Zone("Chambre", 40, e)
        return Installation(100, [e], [z1, z2])

    def test_valid_installation(self):
        inst = self._make_valid_installation()
        assert inst.is_valid() is True

    def test_surface_non_multiple_de_10(self):
        e = Equipement("Chaudiere", 2000, 20)
        z = Zone("Salon", 105, e)
        inst = Installation(105, [e], [z])
        assert inst.is_valid() is False

    def test_surface_300_invalide(self):
        e = Equipement("Chaudiere", 2000, 20)
        z = Zone("Salon", 300, e)
        inst = Installation(300, [e], [z])
        assert inst.is_valid() is False

    def test_surface_290_valide(self):
        e = Equipement("Chaudiere", 2000, 20)
        z = Zone("Salon", 290, e)
        inst = Installation(290, [e], [z])
        assert inst.is_valid() is True

    def test_zones_ne_couvrent_pas_surface(self):
        e = Equipement("Chaudiere", 2000, 20)
        z = Zone("Salon", 50, e)
        inst = Installation(100, [e], [z])
        assert inst.is_valid() is False

    def test_zone_surface_zero(self):
        e = Equipement("Chaudiere", 2000, 20)
        z1 = Zone("Salon", 0, e)
        z2 = Zone("Chambre", 100, e)
        inst = Installation(100, [e], [z1, z2])
        assert inst.is_valid() is False

    def test_zone_equipement_absent(self):
        e1 = Equipement("Chaudiere", 2000, 20)
        e2 = Equipement("Radiateur", 2005, 10)
        z = Zone("Salon", 100, e2)  # e2 absent de la liste
        inst = Installation(100, [e1], [z])
        assert inst.is_valid() is False

    def test_equipement_partage_entre_zones(self):
        """Un équipement peut être utilisé dans plusieurs zones."""
        e = Equipement("Chaudiere", 2000, 20)
        z1 = Zone("Salon", 60, e)
        z2 = Zone("Chambre", 40, e)
        inst = Installation(100, [e], [z1, z2])
        assert inst.is_valid() is True
