import pickle, os

directory = 'malicious_contracts/src'

print (__file__, "file")

def clean_tokens(tokens):
    clean_tokens = []

    for token in tokens:
        if token.startswith('0x') or token == '' or token == ' ' or ('Unknown' in token):
            continue
        clean_tokens.append(token)
    return clean_tokens


def pre_process_opcode(opcode, training=False):

    if training:
        with open(os.path.join(directory,'model_training','vectorizer.pkl'), 'rb') as f:
            loaded_vectorizer = pickle.load(f)
    else:
        with open(os.path.join(directory, 'working_model','vectorizer.pkl'), 'rb') as f:
            loaded_vectorizer = pickle.load(f)
    tokens = clean_tokens(opcode)
    return(loaded_vectorizer.transform(tokens))

