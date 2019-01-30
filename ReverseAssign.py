fileIn = open('d:\Python\ReverseAssign\ReverseIn.txt', 'r')
fileOut = open('d:\Python\ReverseAssign\ReverseOut.txt', 'w')
  
for line in fileIn:
  elem = line.split(' = ')
  firstelem = elem[0]
  lastelem = elem[1].rstrip('\n')
  numspaces = len(firstelem) - len(firstelem.lstrip(' '))
  firstelem = firstelem.lstrip(' ')
  firstelem = firstelem.lstrip('\t')
  fileOut.write((' ' * numspaces) + lastelem + ' = ' + firstelem + '\n')
  
fileIn.close()
fileOut.close()

