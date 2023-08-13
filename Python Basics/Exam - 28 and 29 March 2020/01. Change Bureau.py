bitcoin_amount = int(input())
chinese_yuan_amount = float(input())
commission = float(input())
actual_commission = commission / 100

bitcoin = bitcoin_amount * 1168
euro_bitcoin = bitcoin / 1.95
coin_commission = euro_bitcoin - (euro_bitcoin * actual_commission)

chinese_yuan = chinese_yuan_amount * 0.15
bgn_chinese = chinese_yuan * 1.76
euro_chinese = bgn_chinese / 1.95
chinese_commission = euro_chinese - (euro_chinese * actual_commission)

total_euro = coin_commission + chinese_commission
print(f'{total_euro:.2f}')
