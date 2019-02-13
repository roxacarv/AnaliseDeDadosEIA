import string
import json

class NPL:

	def __init__(self, texto):
		self.textoOriginal = texto
		self.textoModificado = None
		self.stopWords = self.OpenJSON("stopwords")
		self.numbers = None

	def GetTexto(self):
		return self.textoOriginal

	def SetTexto(self, texto):
		self.textoOriginal = texto

	def OpenJSON(self, fileName):
		data = None
		with open(fileName + ".json") as file:
			data = json.load(file)
		return data

	def Tokenizar(self):
		novoTexto = []
		tempPalavra = ""
		for palavra in self.textoOriginal:
			if not palavra or palavra.isspace():
				novoTexto.append(tempPalavra.lower())
				tempPalavra = ""
			elif palavra in string.punctuation:
				novoTexto.append(tempPalavra.lower())
				novoTexto.append(palavra.lower())
				tempPalavra = ""
			else:
				tempPalavra = self.InserirChar(palavra, tempPalavra)
		self.textoModificado = novoTexto

	def RemoverStopwords(self):
		palavrasParaRemover = []
		for palavra in self.textoModificado:
			if palavra in self.stopWords:
				palavrasParaRemover.append(palavra)
		self.RemoverElementos(palavrasParaRemover)

	def RemoverNumeros(self):
		numerosParaRemover = []
		for palavra in self.textoModificado:
			if palavra.isdigit():
				numerosParaRemover.append(palavra)
		self.RemoverElementos(numerosParaRemover)

	def RemoverPalavrasGrandes(self):
		palavrasGrandes = []
		for palavra in self.textoModificado:
			if len(palavra) > 2:
				palavrasGrandes.append(palavra)
		self.RemoverElementos(palavrasGrandes)

	def RemoverPontuacao(self):
		pontuacao = []
		for palavra in self.textoModificado:
			if palavra in string.punctuation:
				pontuacao.append(palavra)
		self.RemoverElementos(pontuacao)

	def RemoverElementos(self, listaDeElementos):
		for elemento in listaDeElementos:
			self.textoModificado.remove(elemento)

	def InserirChar(self, charParaInserir, string):
		novaString = string
		string = novaString + charParaInserir
		return string
