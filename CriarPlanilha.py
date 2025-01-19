import pandas as pd

dados_vendas = {
    'Vendedor': ['Ana', 'Carlos', 'Bianca', 'João', 'Marcos', 'Larissa', 'Pedro', 'Fernanda', 'Lucas', 'Juliana',
                 'Roberta', 'Gustavo', 'Patrícia', 'Rafael', 'Vanessa'],
    'Produto': ['Notebook', 'Smartphone', 'Tablet', 'Monitor', 'Teclado', 'Mouse', 'Impressora', 'HD Externo',
                'Câmera', 'Fone de Ouvido', 'Smartwatch', 'Projetor', 'Carregador', 'Microfone', 'Placa de Vídeo'],
    'Quantidade': [5, 10, 8, 4, 15, 12, 3, 6, 7, 9, 11, 2, 20, 5, 3],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'Salvador', 'Brasília',
               'Recife', 'Fortaleza', 'Manaus', 'Florianópolis', 'Vitória', 'Belém', 'Campinas', 'Goiânia'],
    'Valor Total (R$)': [25000, 8000, 6400, 4800, 3000, 2400, 1500, 3600, 4900, 2700, 5500, 12000, 2000, 4500, 6000],
    'Data da Venda': ['2025-01-10', '2025-01-12', '2025-01-15', '2025-01-18', '2025-01-20', '2025-01-22',
                       '2025-01-25', '2025-01-28', '2025-01-30', '2025-02-01', '2025-02-03', '2025-02-05',
                       '2025-02-07', '2025-02-09', '2025-02-11'],
    'Categoria': ['Eletrônicos', 'Eletrônicos', 'Eletrônicos', 'Periféricos', 'Periféricos', 'Periféricos',
                  'Impressoras', 'Armazenamento', 'Câmeras', 'Periféricos', 'Vestíveis', 'Apresentação',
                  'Acessórios', 'Audio', 'Hardware']
}

df = pd.DataFrame(dados_vendas)
