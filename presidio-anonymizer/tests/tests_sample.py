from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # Run the anonymizer
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Check the anonymized text
    assert result.text == "My name is BIP."

    # Ensure one item was anonymized
    assert len(result.items) == 1

    # Verify the first item details
    item = result.items[0]
    assert item["start"] == 11
    assert item["end"] == 14
    assert item["entity_type"] == "PERSON"
    assert item["text"] == "BIP"
    assert item["operator"] == "replace"
