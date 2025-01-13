import pickle, os
from src.utils.pre_process import pre_process_opcode

dir = os.path.dirname(__file__)

with open(os.path.join(dir,'model.pkl' ), 'rb') as f:
    model = pickle.load(f)

## Call with [opcode]
def predict(opcode):

    pre_processed_opcode = pre_process_opcode(opcode)

    res =  model.predict(pre_processed_opcode)
    
    return res


