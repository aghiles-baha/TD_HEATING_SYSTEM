import pytest
import Equipement


class TestEquipement:

    def test_valid_equipement(self):
        e = Equipement("Chaudiere", 2000, 20)
        assert e.is_valid() is True

    def test_valid_all_types(self):
        for t in ["Chaudiere", "Radiateur", "Pompe a chaleur", "Chauffe-eau"]:
            assert Equipement(t, 2000, 20).is_valid() is True

    def test_invalid_type(self):
        e = Equipement("Climatiseur", 2000, 20)
        assert e.is_valid() is False

    def test_annee_trop_ancienne(self):
        e = Equipement("Chaudiere", 1995, 20)
        assert e.is_valid() is False

    def test_annee_1994(self):
        e = Equipement("Chaudiere", 1994, 20)
        assert e.is_valid() is False

    def test_annee_2019_invalide(self):
        e = Equipement("Chaudiere", 2019, 20)
        assert e.is_valid() is False

    def test_annee_1996_valide(self):
        e = Equipement("Chaudiere", 1996, 20)
        assert e.is_valid() is True

    def test_puissance_trop_faible(self):
        e = Equipement("Chaudiere", 2000, 0)
        assert e.is_valid() is False

    def test_puissance_trop_forte(self):
        e = Equipement("Chaudiere", 2000, 51)
        assert e.is_valid() is False

    def test_puissance_limite_basse(self):
        e = Equipement("Chaudiere", 2000, 1)
        assert e.is_valid() is True

    def test_puissance_limite_haute(self):
        e = Equipement("Chaudiere", 2000, 50)
        assert e.is_valid() is True
