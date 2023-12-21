import os
directory = "test"

for filename in os.listdir(directory):
    if filename.startswith("test"):
        filepath = os.path.join(directory, filename)
        # Execute the file here
        exec(open(filepath).read())

