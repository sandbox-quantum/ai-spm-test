# This model is a test model for the detection of malicious behavior.
# See https://huggingface.co/ScanMe/test-models

import keras

model = keras.saving.load_model("hf://ScanMe/test-models")
