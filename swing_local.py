"""data_local.py — utilitário para baixar OHLCV (open, high, low, close, volume)
com yfinance. Para ações da B3, inclua sufixo .SA (ex.: 'PETR4.SA')."""

import yfinance as yf
import pandas as pd

def get_ohlcv(ticker: str, period: str = '2y', interval: str = '1d') -> pd.DataFrame:
    """Baixa dados do yfinance e padroniza colunas.
    - ticker: símbolo (ex.: 'BBAS3.SA')
    - period: janela (ex.: '1y', '2y')
    - interval: granularidade (ex.: '1d', '1h')
    """
    df = yf.download(ticker, period=period, interval=interval, auto_adjust=False, progress=False)
    df = df.rename(columns={
        'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close',
        'Adj Close': 'adj_close', 'Volume': 'volume'
    }).dropna()
    return df
