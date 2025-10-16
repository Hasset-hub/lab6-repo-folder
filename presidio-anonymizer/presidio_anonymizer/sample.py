from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, start: int, end: int):
    """Run the anonymizer with given text and indices, return result."""
    engine = AnonymizerEngine()
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )
    return result

# ✅ Correct __main__ block
if __name__ == "__main__":
    result = sample_run_anonymizer("My name is Bond.", 11, 15)
    print(result)
