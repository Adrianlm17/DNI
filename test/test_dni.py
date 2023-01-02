from src.dni import *

import pytest



@pytest.mark.test_extensionDni
def test_extensionDni():
    assert False == Dni.checkNum(436271815)
    assert True == Dni.checkNum(43627181)
    assert False == Dni.checkNum(4362718)
    assert False == Dni.checkCaracter("aaaaaa")


@pytest.mark.test_checkCaracter
def test_checkCaracter():
    assert True == Dni.checkCaracter(49481746)
    assert False == Dni.checkCaracter(-4948174)
    assert False == Dni.checkCaracter(494-1746)
    assert False == Dni.checkCaracter("aaaaaa")


@pytest.mark.test_resNum
def test_resNum():
    assert 6 == Dni.checkResNum(49481746)
    assert 19 == Dni.checkResNum(54622121)
    assert False == Dni.checkResNum(00000000)


@pytest.mark.test_letraDni
def test_letraDni():
    assert "Y" == Letra.letraDni(6)
    assert "L" == Letra.letraDni(19)
    assert False == Letra.letraDni(23)
