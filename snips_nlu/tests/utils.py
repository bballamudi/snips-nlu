import io
import json
import os

from snips_nlu.dataset import validate_and_format_dataset

TEST_PATH = os.path.dirname(os.path.abspath(__file__))
SAMPLE_DATASET_PATH = os.path.join(TEST_PATH, "resources",
                                   "sample_dataset.json")


def empty_dataset(language):
    return validate_and_format_dataset(
        {"intents": {}, "entities": {}, "language": language.iso_code})


with io.open(SAMPLE_DATASET_PATH) as dataset_file:
    SAMPLE_DATASET = json.load(dataset_file)

SAMPLE_DATASET = validate_and_format_dataset(SAMPLE_DATASET)
