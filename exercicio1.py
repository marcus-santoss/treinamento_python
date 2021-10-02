class ConversorDados:
    def __init__(self, caminho_arquivo) -> None:        
        self.caminho_arquivo = self._validar_nome_de_arquivo(caminho_arquivo)
        
    def _validar_nome_de_arquivo(self, caminho_arquivo):
        # Só aceita arquivo json
        partes_do_arquivo = caminho_arquivo.split(".")
        tipo_arquivo = partes_do_arquivo[1]
        
        if tipo_arquivo != "json":
            raise Exception(f"O tipo de arquivo {tipo_arquivo} é inválido. Só aceitamos aquivos json")
        return caminho_arquivo
        
    def converter_para_csv(self):
        # Converter para objto json
        # Converte para objeto csv
        # Sava em arquivo csv
        print(f"Convertendo arquivo {self.caminho_arquivo} para csv")

    def converter_para_xlsx(self):
        # Converter para objto json
        # Sava em arquivo csv
        print(f"Convertendo arquivo {self.caminho_arquivo} para xlsx")

    def imprimir_na_tela(self):
        print(f"Imprimindo arquivo {self.caminho_arquivo} na tela")

if __name__ == "__main__":
    conv = ConversorDados("alunos.json")
    conv.converter_para_csv()
    conv.converter_para_xlsx()
    conv.imprimir_na_tela()