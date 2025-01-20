from typing import Optional

FOUNDING_DATE_GREP_PATTERNS = [
    "was founded in",
    "was incorporated in",
    "been in operation since",
]


def parse_founding_date(business_summary: str) -> Optional[int]:
    for pattern in FOUNDING_DATE_GREP_PATTERNS:
        index = business_summary.find(pattern)
        if index != -1:
            start_index, end_index = index + len(pattern), index + len(pattern) + 5
            extracted_date = business_summary[start_index:end_index].strip()
            if extracted_date.isdigit():
                return int(extracted_date)

    return None
