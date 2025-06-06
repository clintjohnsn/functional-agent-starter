"""Test server."""

import server


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(server.__name__, str)
