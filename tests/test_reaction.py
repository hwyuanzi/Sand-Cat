import pytest
from sandcat_fun.reaction import cat_reaction

# --- tests for valid outputs ---

def test_cat_reaction_bug_fixed_mild():
    """Mild reaction to a fixed bug should mention nods and squashed."""
    result = cat_reaction("bug_fixed", 1)
    assert isinstance(result, str)
    assert "nods approvingly" in result
    assert "Bug squashed" in result

def test_cat_reaction_bug_fixed_max():
    """Max intensity bug fix should be loud and celebratory."""
    result = cat_reaction("bug_fixed", 3)
    assert "MROW" in result
    assert "CLEAN CODE" in result
    assert "celebration" in result

def test_cat_reaction_code_review_moderate():
    result = cat_reaction("code_review", 2)
    assert "inspects" in result
    assert "comments" in result
    assert isinstance(result, str)

def test_cat_reaction_deploy_max():
    result = cat_reaction("deploy", 3)
    assert "DEPLOYING" in result
    assert "ROLLBACK" in result
    assert "MROW" in result

def test_cat_reaction_merge_conflict_max():
    result = cat_reaction("merge_conflict", 3)
    assert "HISS" in result
    assert "CATASTROPHE" in result
    assert "BRANCH" in result

def test_cat_reaction_friday_moderate():
    result = cat_reaction("friday", 2)
    assert "weekend" in result
    assert "Purrr" in result
    assert isinstance(result, str)

def test_cat_reaction_monday_max():
    result = cat_reaction("monday", 3)
    assert "refuses" in result
    assert "System.exit(0)" in result
    assert "Monday" in result

def test_cat_reaction_normalizes_input():
    """Whitespace and uppercase in event name should still work."""
    result = cat_reaction("  BUG_FIXED  ", 1)
    assert "nods approvingly" in result
    assert isinstance(result, str)
    assert "Bug" in result

def test_cat_reaction_default_intensity():
    """Not passing intensity should default to 1 (mild)."""
    result = cat_reaction("friday")
    assert "yawns" in result
    assert "Almost weekend" in result
    assert isinstance(result, str)

# --- tests for invalid inputs ---

def test_cat_reaction_empty_event():
    with pytest.raises(ValueError):
        cat_reaction("")

def test_cat_reaction_whitespace_event():
    with pytest.raises(ValueError):
        cat_reaction("   ")

def test_cat_reaction_invalid_event():
    with pytest.raises(ValueError) as excinfo:
        cat_reaction("lunch_break", 1)
    assert "event must be one of" in str(excinfo.value)

def test_cat_reaction_intensity_too_low():
    with pytest.raises(ValueError):
        cat_reaction("deploy", 0)

def test_cat_reaction_intensity_too_high():
    with pytest.raises(ValueError):
        cat_reaction("deploy", 4)

def test_cat_reaction_intensity_not_int():
    with pytest.raises(TypeError):
        cat_reaction("deploy", "high")

def test_cat_reaction_intensity_bool():
    with pytest.raises(TypeError):
        cat_reaction("deploy", True)

def test_cat_reaction_event_not_string():
    with pytest.raises(ValueError):
        cat_reaction(123, 1)
