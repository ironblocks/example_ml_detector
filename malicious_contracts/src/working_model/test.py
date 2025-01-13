import os
from malicious_contracts.src.utils.clean_opcode_from_file import process_file
from malicious_contracts.src.working_model.main import predict


dir = os.path.dirname(__file__)

def run():

    malicious_directory_path = os.path.join(dir, 'test_opcodes/malicious')
    not_malicious_directory_path = os.path.join(dir, 'test_opcodes/not_malicious')
    
    print ("Should print True for detecting malicious contracts")

    for filename in os.listdir(malicious_directory_path):
        clean_opcode = process_file(os.path.join(malicious_directory_path, filename))

        print("File name: ", filename, "Result:", predict([clean_opcode])[0])
        

    print ("Should print False for detecting malicious contracts")

    for filename in os.listdir(not_malicious_directory_path):
        clean_opcode = process_file(os.path.join(not_malicious_directory_path,filename))

        print("File name:", filename, "Result:", predict([clean_opcode])[0])

# Run reads from the test_opcodes directory, pro
if __name__ == '__main__':
    run()
