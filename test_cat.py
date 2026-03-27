import pytest
from sandcat_fun.cat import cat_fortune, cat_comfort

# unit test for cat_fortune
# tests for outputs
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

# tests for inputs
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

# unit test for cat_fortune
# tests for outputs
def test_cat_comfort_returns_string():
    result = cat_comfort(1)
    assert isinstance(result, str)

def test_cat_comfort_default_level():
    result = cat_comfort()
    assert isinstance(result, str)
    assert "Purrr" in result

def test_cat_comfort_level_3():
    result = cat_comfort(3)
    assert "everything will be okay" in result

def test_cat_comfort_level_5():
    result = cat_comfort(5)
    assert "This sand cat strongly recommends water" in result
    assert "<3" in result

def test_cat_comfort_invalid_level_low():
    with pytest.raises(ValueError):
        cat_comfort(0)

# tests for inputs
def test_cat_comfort_invalid_level_high():
    with pytest.raises(ValueError):
        cat_comfort(6)

def test_cat_comfort_invalid_level_type():
    with pytest.raises(TypeError):
        cat_comfort("high")