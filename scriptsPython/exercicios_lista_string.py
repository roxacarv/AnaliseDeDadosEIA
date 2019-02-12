def ExibirImpares(lista):
	return [i for i in lista if i%2 != 0]

def InverterVetor(lista):
	return lista[::-1]

def Media(*args):
	print("Media Geral: %.02f" % (sum(args)/len(args)))
	for arg in range(len(args)):
		print("Nota %d: %.02f" % (arg, args[arg]))

def MediaAlunos(alunos):
	mediasMaioresQueSete = 0
	for aluno in alunos:
		mediaDoAluno = sum(aluno)/len(aluno)
		if mediaDoAluno >= 7.0:
			mediasMaioresQueSete += 1
	print(mediasMaioresQueSete)

def CriarAlunos():
	from random import randint, uniform
	randAlunos = randint(0, 30)
	listaDeAlunos = []
	for aluno in range(randAlunos):
		listaDeAlunos.append([uniform(0.0, 10.0), uniform(0.0, 10.0), uniform(0.0, 10.0), uniform(0.0, 10.0)])
	return listaDeAlunos

def Middle(lista):
	return lista[1:-1]

def TamanhoStrings(primeiraString, segundaString):
	tamanhoStrings = True if len(primeiraString) - len(segundaString) == 0 else False
	conteudoStrings = True if primeiraString == segundaString else False
	print("Primeira String tem o tamanho de %d e o valor de %s \nSegunda String tem o tamanho de %d e o valor de %s" 
		% (len(primeiraString), primeiraString, len(segundaString), segundaString))
	if tamanhoStrings:
		print("As strings possuem o mesmo comprimento")
	if conteudoStrings:
		print("As strings possuem o mesmo conteúdo")

def ReverterNome():
	nomeOriginal = input("Digite seu nome: ")
	nomeRevertido = nomeOriginal[::-1]
	print(nomeRevertido.upper())

def DataPorExtenso(data):
	dataFinal = data.split("/")
	meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	print("%d de %s de %d" % (int(dataFinal[0]), meses[int(dataFinal[1])], int(dataFinal[2])))

def Palindromo(palavra):
	palavra = palavra.split()
	possivelPalindromo = "".join(palavra)
	ePalindromo = True if possivelPalindromo.lower() == possivelPalindromo[::-1].lower() else False
	if ePalindromo:
		print("É um palindromo")
	else:
		print("Não é um palindromo")

print(ExibirImpares(list(range(10))))
print(InverterVetor(list(range(10))))
Media(8.0, 8.0, 9.0, 9.0)
alunos = CriarAlunos()
MediaAlunos(alunos)
print(Middle([10, 20, 30, 40, 12, 34]))
TamanhoStrings("Rodrigo", "Jeferson")
#ReverterNome()
DataPorExtenso("30/03/1991")
Palindromo("Ovo")
