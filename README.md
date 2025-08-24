# Demographic Data Analyzer

Projeto da trilha **Data Analysis with Python** (freeCodeCamp).

## Objetivo
Analisar o dataset `adult.data.csv` (Census Bureau data) e gerar estatísticas demográficas como:
- Distribuição por raça
- Média de idade dos homens
- Percentual de bacharéis
- Percentuais de pessoas com/sem educação avançada que ganham >50K
- Horas mínimas trabalhadas e % de ricos nesse grupo
- País com maior percentual de pessoas que ganham >50K
- Ocupação mais comum na Índia entre pessoas >50K

## Estrutura
- `adult.data.csv` — dataset original
- `demographic_data_analyzer.py` — implementação principal
- `test_module.py` — testes unitários
- `README.md` — descrição do projeto

## Como rodar
```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
pip install pandas

# executar análise
python demographic_data_analyzer.py

# rodar testes
python test_module.py
