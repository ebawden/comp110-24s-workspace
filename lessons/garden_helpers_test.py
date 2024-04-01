"""Test my garden functions."""

__author__ = "730649327"


from lessons.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date

def test_add_by_kind() -> None:
    """Test basic use case for add by kind function."""
    t: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    plant_kind = "flower"
    plant ="daisy"
    assert add_by_kind(t, plant_kind, plant) == {"flower": ["marigold", "zinnia", "daisy"], "vegetable": ["carrots"]}

def test_add_by_kind() -> None:
    """Test basic edge case for add by kind function."""
    t: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    plant_kind = "vegetable"
    plant = "marigold"
    assert add_by_kind(t, plant_kind, plant) ==  {"flower": ["marigold", "zinnia", "daisy"], "vegetable": ["carrots"]}



def test_add_by_date() -> None:
    """Test basic use case for add by date function"""
    t: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots", "zinnias"]}
    month = "April"
    plant = "marigold"
    assert add_by_date(t, month, plant) == {"April", "daisy"}

def test_add_by_date() -> None:
    """Test basic edge case for add by date function"""
    t: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots", "zinnias"]}
    month = "April"
    plant = "marigold"
    assert add_by_date(t, month, plant) == {"April", "June"}



def test_lookup_by_kind_and_date() -> None:
    """Test basic use case for lookup function"""
    t: dict[list[str]] = {"flower", "April"}
    plants_by_date = 
    assert lookup_by_kind_and_date(t) == {"flowers to plant in April: ['marigold']"}

def test_lookup_by_kind_and_date() -> None:
    """Test basic use case for lookup function"""
    t: dict[list[str]] = {"flower", "April", "June" }
    assert lookup_by_kind_and_date(t) == {"flowers to plant in April and June: ['marigold']"}