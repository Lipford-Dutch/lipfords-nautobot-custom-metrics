"""Unit tests for task helpers."""
import pytest
from hypothesis import given, strategies as st

from tasks import is_truthy

@pytest.mark.parametrize(
    "value,expected",
    [
        ("y", True),
        ("yes", True),
        ("1", True),
        ("no", False),
        ("0", False),
        (True, True),
        (False, False),
    ],
)
def test_is_truthy(value, expected):
    assert is_truthy(value) is expected


@given(st.booleans())
def test_is_truthy_idempotent(b):
    assert is_truthy(b) is b


@given(
    st.text().filter(
        lambda s: s.lower() not in {"y","yes","t","true","on","1","n","no","f","false","off","0"}
    )
)
def test_is_truthy_invalid(s):
    with pytest.raises(ValueError):
        is_truthy(s)
