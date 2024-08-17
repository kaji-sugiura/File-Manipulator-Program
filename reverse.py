import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
contents = ""

with open(input_file) as f:
    contents = f.read()
    
with open(output_file, "w") as f:
    f.write(contents[::-1])