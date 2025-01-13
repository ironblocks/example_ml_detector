import re

## Cleans ops codes copied from a etherscan decompiler
def process_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    processed_lines = []

    for line in lines:
        line = re.sub(r'\[.*?\]', '', line)
        
        line = re.sub(r'\b0x\w+\b', '', line)
        
        if 'Unknown' in line:
            continue
        
        processed_lines.append(line.strip())

    return ' '.join(processed_lines)



