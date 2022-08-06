def clause1():
    #read input file
    fin = open("introduction.txt", "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace('the Site', 'Youtube')
    # print new template to console
    print(data)
    #close the input file
    fin.close()

clause1()

def clause2():
    #read input file
    fin = open("intellectual property rights.txt", "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace('the Site', 'Youtube').replace('stress', 'sex')
    # print new template to console
    print(data)
    #close the input file
    fin.close()