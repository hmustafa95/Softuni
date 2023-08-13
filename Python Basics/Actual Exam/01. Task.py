processor_dollar = float(input())
videocard_dollar = float(input())
ram_dollar = float(input())
amount_ram = int(input())
discount = float(input())

discounted_processor = processor_dollar - (processor_dollar * discount)
discounted_videocard = videocard_dollar - (videocard_dollar * discount)
total_ram = ram_dollar * amount_ram

processor_lv = discounted_processor * 1.57
videocard_lv = discounted_videocard * 1.57
ram_lv = total_ram * 1.57

total_price = processor_lv + videocard_lv + ram_lv

print(f'Money needed - {total_price:.2f} leva.')
