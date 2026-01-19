import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo do seaborn
sns.set_style("darkgrid")
sns.set_palette("husl")

print("Carregando dados de petr4a.csv...")
try:
    # Ler dados do arquivo CSV
    dados = pd.read_csv('petr4a.csv', index_col=0, parse_dates=True)
    
    if dados.empty:
        print("Erro: Nenhum dado foi carregado!")
    else:
        print(f"Dados carregados com sucesso: {len(dados)} registros.")
        
        dados['retorno_diario'] = dados['Adj Close'].pct_change()
        dados = dados[['Adj Close', 'retorno_diario']]
        
        # Remover valores NaN
        dados = dados.dropna()
        
        # Visualizando os dados com seaborn
        plt.figure(figsize=(14, 6))
        sns.lineplot(data=dados, x=dados.index, y='retorno_diario', linewidth=2, label='Retorno Diário')
        plt.title('Retorno Diário da Ação PETR4', fontsize=16, fontweight='bold')
        plt.xlabel('Data', fontsize=12)
        plt.ylabel('Retorno Diário (%)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.tight_layout()
        
        # Salvar a figura
        plt.savefig('grafico_retorno_diario_petr4.png', dpi=300, bbox_inches='tight')
        print("Gráfico salvo como 'grafico_retorno_diario_petr4.png'")
        
        plt.show()
    
except Exception as e:
    print(f"Erro ao carregar dados: {e}")