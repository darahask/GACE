import re

def changecode():
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')

    loop = f1.read()
    a = re.search(r"for", loop).start()
    f2.write(loop[:a] + "\n")
    loop = loop[a:-1]
    b = re.search(r'\}', loop).start()

    if re.search(r"for", loop):
        x = re.findall(r'(\(.*\))', loop)
        y = x[0].split(';')
        f2.write(y[0][1:] + ';' + '\n')
        f2.write('while(' + y[1][1:] + ')' + '\n')
        z = re.search(r'\{', loop).start()
        f2.write(loop[z:b] + '\n\t' + y[2][1:-1] + ';\n' + '}' + '\n')

    f2.write(loop[b+1:] + '\n}')

    f1.close()
    f2.close()
