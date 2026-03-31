from sandcat_fun.draw import draw_cat

def test_draw_cat_default_sleeping():
    """Test that the default style returns the sleeping cat."""
    art = draw_cat()
    assert "zZz..." in art
    assert "v_v" in art
    assert r"|\___/|" in art

def test_draw_cat_stretching():
    """Test that the 'stretching' style returns the correct ASCII art."""
    art = draw_cat("stretching")
    assert "o.o" in art
    assert "____/" in art
    assert "stretching" not in art

def test_draw_cat_case_insensitivity_and_whitespace():
    """Test that the function gracefully handles messy inputs."""
    art = draw_cat("  PLAYING  ")
    assert "✧ω✧" in art
    assert "o" in art
    assert "> ^ <" in art

def test_draw_cat_coding():
    """Test that the 'coding' style returns the coding cat with a bug."""
    art = draw_cat("coding")
    assert "@.@" in art
    assert "[Bug]" in art
    assert "[___]" in art

def test_draw_cat_ninja():
    """Test that the 'ninja' style returns the stealthy ninja cat throwing a star."""
    art = draw_cat("ninja")
    assert "-_-" in art
    assert "---*" in art
    assert "ninja" not in art

def test_draw_cat_loaf():
    """Test that the 'loaf' style returns the classic cat loaf."""
    art = draw_cat("loaf")
    assert "-.-" in art
    assert "(_____)" in art
    assert "loaf" not in art

def test_draw_cat_invalid_style():
    """Test that an invalid style returns the confused cat with the style name."""
    art = draw_cat("flying")
    assert "?.?" in art
    assert "Unknown style 'flying'" in art
    assert "flying" in art