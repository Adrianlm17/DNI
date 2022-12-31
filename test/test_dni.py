from src.dni import Dni

import pytest



@pytest.mark.test_extensionDni
def test_extensionDni():
    assert False == Dni.checkNum(436271815)
    assert True == Dni.checkNum(43627181)
    assert False == Dni.checkNum(4362718)


@pytest.mark.test_resNum
def test_resNum():
    assert 6 == Dni.checkResNum(49481746)
    assert 19 == Dni.checkResNum(54622121)
    assert False == Dni.checkResNum(00000000)


@pytest.mark.test_letraDni
def test_letraDni():
    assert "Y" == Dni.letraDni(6)
    assert "L" == Dni.letraDni(19)
    assert False == Dni.letraDni(23)
