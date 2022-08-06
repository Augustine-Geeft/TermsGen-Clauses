# Import the required libraries
import os

# Define the location of the directory
path =r"C:\Users\GOAT\Documents\TermsGen Clause"


def customMessage():
    #read input file
    fin = open("story.txt", "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace('psychology professor', 'education student').replace('stress', 'mood')
    # print new template to console
    print(data)
    #close the input file
    fin.close()



# Change the directory
os.chdir(path)

def read_files(file_path):
   with open(file_path, 'r') as file:
      print(file.read())

# Iterate over all the files in the directory
for file in os.listdir():
   if file.endswith('.txt'):
      # Create the filepath of particular file
      file_path =f"{path}/{file}"

read_files(file_path)
