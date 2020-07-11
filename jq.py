# from jqdatasdk import *
from pandas import *

# auth('13521722086', 'Quant2020')
stocks = read_csv('data/stocks.csv')
pan = read_csv('data/prices.csv')
names = dict(zip(stocks.values[:, 0], stocks.values[:, 1]))

prices = pan.values
number = len(stocks)

res = DataFrame(columns=('代码', '名称', '收盘价', '5日均线', '10日均线',
                         '20日均线', '30日交易量', '30日交易额'))

for i in range(0, number*30, 30):
    code = prices[i, 2]
    display_name = names[code]
    close, k5, k10, k20 = 0, 0, 0, 0
    volume, money = 0, 0
    for j in range(i + 10, i + 29):
        close = prices[j, 4]
        volume += prices[j, 7]
        money += prices[j, 8]
        if j - i >= 10:
            k20 += close
        if j - i >= 20:
            k10 += close
        if j - i >= 25:
            k5 += close
    k20 /= 20.
    k10 /= 10.
    k5 /= 5.
    # res.append(code, display_name, close, k5, k10, k20, volume, money)
    res.loc[res.shape[0] + 1] = {'代码': code, '名称': display_name, '收盘价': close,
                                 '5日均线': k5, '10日均线': k10, '20日均线': k20,
                                 '30日交易量': volume, '30日交易额': money}

res.to_csv('data/summary.csv', encoding='utf-8-sig')
# logout()
