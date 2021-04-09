import sys
def updateDB(port):
    print("THIS IS A TEST, PORT = ", port)
    with open('database.json') as f:
        l = f.readlines()


    again = True
    newl = []
    trueP = 0
    for oldp in ['5001','5002','5003', '5004']:
        for line in l:
            if oldp in line:
                trueP = oldp

    if trueP != 0:
        for line in l:
            line = line.replace(f'http://127.0.0.1:{trueP}/', f'http://127.0.0.1:{port}/')
            newl.append(line)

    if newl:
        with open('database.json', 'w') as f2:
            print(newl)
            f2.writelines(newl)

if __name__ == '__main__':
    updateDB(port=(sys.argv[1]))
