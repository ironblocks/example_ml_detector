## Environment Setup (macOS)

```bash
python3 -m venv venv  
source venv/bin/activate
pip3 install .
```

# Malicious Contracts Detector

__Important note__: You must use exactly the same pre-processing steps that were used in training the model in production/testing. This includes the same vectorization/tokenization and any processing to the opcodes. See at example opcode in `src/opcode_example.txt`.


## Set up

In the main directory run `pip3 install -e .` .

## Training the model

Use `src/model_training/train.ipynb` to train the model and follow the instructions in the notebook. Make sure you save the new model and new vectorizer as `model.pkl` and `vectorizer.pkl` to the `working_model` directory before running it in test/production. Models are saved in the `model_training` directory.

## Using the model

Call `predict([opcode])` from `src/working_model/main.py` with a string of opcode, opcodes and operands separated by spaces like: `PUSH1 0x80 PUSH1 0x40 MSTORE PUSH1 0x04`.

To  test the model save the opcodes in `.txt` files in `working_model/test_opcodes`, and run `src/working_model/test.py`

If you're reading from file, the format of the opcodes should be a string as above, or:

> [1] PUSH1 0x80

> [3] PUSH1 0x40

> [4] MSTORE

> [6] PUSH1 0x04

If your opcode has any other formatting, make sure you pre-process it to fit the expected format (a string of opcodes and operands)
  

