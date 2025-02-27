import pandas as pd

def analisar_vendas(caminho_ficheiro):
    """
    Carrega um ficheiro CSV de vendas e realiza análises básicas.

    Args:
        caminho_ficheiro (str): Caminho completo para o ficheiro CSV.

    Returns:
        pandas.DataFrame: DataFrame com os dados carregados.
    """

    try:
        df = pd.read_csv(caminho_ficheiro, parse_dates=['date'])

        # Calcular o valor médio do pedido
        valor_medio_pedido = df['total_price'].mean()
        print("O valor médio do pedido é:", valor_medio_pedido)

        # Encontrar a última compra por cliente e formatando a data
        ultima_compra_por_cliente = df.groupby('buyer_name')['date'].max().dt.strftime('%Y-%m-%d')
        print("Última compra por cliente:\n", ultima_compra_por_cliente)

        return df
    except FileNotFoundError:
        print(f"Ficheiro não encontrado: {caminho_ficheiro}")
    except pd.errors.ParserError:
        print(f"Erro ao analisar o ficheiro: {caminho_ficheiro}")

# Como usar o script:
df = analisar_vendas('Meganium_Sales_Data_consolidado.csv')
