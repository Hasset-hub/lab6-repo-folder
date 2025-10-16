import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

@pytest.mark.parametrize(
    # fmt: off
    "text, start, end, expected_text, expected_items",
    [
        (
            "My name is Bond.", 
            11, 
            15, 
            "My name is BIP.",
            [{'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}]
        ),
    ],
    # fmt: on
)
def test_sample_run_anonymizer(text, start, end, expected_text, expected_items):
    result = sample_run_anonymizer(text, start, end)

    # Check that the text is correctly anonymized
    assert result.text == expected_text

    # Check that the items list is correct
    assert result.items == expected_items
