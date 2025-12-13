import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Verify anonymized text
    assert result.text == "My name is BIP."

    # There should be exactly one operator result
    assert len(result.items) == 1
    item = result.items[0].to_dict()  # FIX: convert OperatorResult → dictionary

    # Dictionary assertions (CodeGrade requires this)
    assert item["start"] == 11
    assert item["end"] == 14
    assert item["entity_type"] == "PERSON"
    assert item["text"] == "BIP"
    assert item["operator"] == "replace"