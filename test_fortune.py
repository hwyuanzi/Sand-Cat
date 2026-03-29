import pytest
from sandcat_fun.fortune import get_fortune

def test_get_fortune_default():
    """Test the default fortune when no treats are explicitly provided."""
    result = get_fortune()
    assert isinstance(result, str)
    assert "Meow" in result
    assert "syntax error" in result

def test_get_fortune_medium_treats():
    """Test the fortune given for a medium amount of treats."""
    result = get_fortune(5)
    assert isinstance(result, str)
    assert "Purrr" in result
    assert "bug" in result

def test_get_fortune_high_treats():
    """Test the ultimate fortune given for a large amount of treats."""
    result = get_fortune(15)
    assert isinstance(result, str)
    assert "MROW" in result
    assert "compile flawlessly" in result

def test_get_fortune_zero_treats():
    """Test the sassy response when 0 treats are given."""
    result = get_fortune(0)
    assert isinstance(result, str)
    assert "judges" in result
    assert "No treats" in result

def test_get_fortune_negative_treats():
    """Test the angry response when negative treats are provided."""
    result = get_fortune(-2)
    assert isinstance(result, str)
    assert "HISS" in result
    assert "negative treats" in result

def test_get_fortune_invalid_type():
    """Test that a TypeError is raised when a non-integer is passed."""
    with pytest.raises(TypeError) as excinfo:
        get_fortune("five")  # type: ignore
    assert "integers" in str(excinfo.value)
    assert "treats" in str(excinfo.value)
    assert excinfo.type == TypeError