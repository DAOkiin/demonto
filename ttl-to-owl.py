import os
import rdflib

# Define the directory you want to start from
rootDir = '.'

for dirName, subdirList, fileList in os.walk(rootDir):
    # Ignore directories that start with "."
    if os.path.basename(dirName).startswith('.'):
        continue
    # Look only one level deep
    if dirName.count(os.sep) - rootDir.count(os.sep) <= 1:
        for fname in fileList:
            # Check if the file is a .ttl file
            if fname.endswith('.ttl'):
                print('Converting', fname, 'to .owl')
                ttl_file_path = os.path.join(dirName, fname)
                owl_file_path = os.path.join(dirName, fname.replace('.ttl', '.owl'))

                # Load the .ttl file
                g = rdflib.Graph()
                g.parse(ttl_file_path, format="turtle")

                # Save as .owl file
                g.serialize(destination=owl_file_path, format='xml')