### Exercício 1:
    
Criar uma classe para converter formatos de dados que receba o caminho completo de um arquivo json no construtor, faça a leitura deste conteúdo transformando-o para dicionário e que tenha 2 métodos: 
    
- O primeiro salva os dados em formato csv
- O segundo sava os dados em formato xlsx
    
`O nome do arquivo precisa ser o mesmo, porém os formatos de arquivo serão diferentes`
    
    
### Exemplo:
    
```python
conversor = ConversorDados(caminho_arquivo="alunos.json")

# Salvar em formato csv
conversor.salvar_em_formato_csv()

# Salvar em formato xlsx
conversor.salvar_em_formato_xlsx()

# Imprimir os dados na tela
conversor.imprimir_dados_na_tela()
```
    
    
### Tratamento de dados
- O campo data_nascimento está com formato 2006-07-25 ( yyyy-mm-dd ). Precisamos converter para o formato 25/07/2006 ( `dd-mm-yyyy` )
      
- Existem alunos sem CPF ( `000.000.000-00` ). Nesses casos precisamos trocar o valor `000.000.000-00` por uma mensagem: Sem CPF.