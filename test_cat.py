import pytest
from sandcat_fun.cat import cat_fortune

# unit test for cat_fortune
# these for outputs
def test_cat_fortune_returns_string():
    result = cat_fortune("sunny", 2)
    assert isinstance(result, str)
    assert "Sunny" in result
    assert "nap-friendly" in result


def test_cat_fortune_mid_energy():
    result = cat_fortune("rainy", 5)
    assert "Rainy" in result
    assert "cozy" in result


def test_cat_fortune_high_energy():
    result = cat_fortune("windy", 9)
    assert "Windy" in result
    assert "zoomie-powered" in result


def test_cat_fortune_strips_and_normalizes_weather():
    result = cat_fortune("  snowy  ", 4)
    assert "Snowy" in result
    assert "cozy" in result

# these for inputs
def test_cat_fortune_invalid_empty_weather():
    with pytest.raises(ValueError):
        cat_fortune("", 5)


def test_cat_fortune_invalid_weather_name():
    with pytest.raises(ValueError):
        cat_fortune("stormy", 5)


def test_cat_fortune_invalid_energy_range_low():
    with pytest.raises(ValueError):
        cat_fortune("sunny", 0)


def test_cat_fortune_invalid_energy_range_high():
    with pytest.raises(ValueError):
        cat_fortune("sunny", 11)


def test_cat_fortune_invalid_energy_type():
    with pytest.raises(TypeError):
        cat_fortune("sunny", "high")