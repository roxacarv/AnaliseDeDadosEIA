#textManipulation
from NPL import NPL

file = open("tm.txt", "r")
textFile = file.readline()
file.close()
print("Texto antes das modificações: ")
print("".join(textFile))
npl = NPL(textFile)
npl.Tokenizar()
npl.RemoverStopwords()
npl.RemoverPontuacao()
npl.RemoverNumeros()
npl.RemoverPalavrasGrandes()
print("Texto após as modificações: ")
print(" ".join(npl.textoModificado))