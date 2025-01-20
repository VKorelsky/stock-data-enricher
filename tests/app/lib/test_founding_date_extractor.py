import pytest
from typing import Optional
from src.app.lib.founding_date_extractor import parse_founding_date


@pytest.mark.parametrize(
    "business_summary, expected_founding_date",
    [
        (
            "This company was founded in 2005 and has been in operation since then.",
            2005,
        ),
        (
            "The company was incorporated in 1998 and has been operating since then.",
            1998,
        ),
        ("This company is a leading provider of services.", None),
        (
            "The company was founded in 1980. It has since grown into a global corporation.",
            1980,
        ),
        (
            "The company has been in operation since 1975. It was founded by John Smith.",
            1975,
        ),
        ("The company was founded in the early 20th century.", None),
        ("The company was founded in 1998, but it started operations in 1999.", 1998),
    ],
)
def test_parse_founding_date(
    business_summary: str, expected_founding_date: Optional[int]
):
    assert parse_founding_date(business_summary) == expected_founding_date
