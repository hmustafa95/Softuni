name_company = input()
adult_tickets = int(input())
child_tickets = int(input())
price_adult = float(input())
price_child = price_adult * 0.30
agency_ripoff = float(input())

real_adult = price_adult + agency_ripoff
real_child = price_child + agency_ripoff

ripoff_profit = ((real_adult * adult_tickets) + (real_child * child_tickets)) * 0.20
print(f'The profit of your agency from {name_company} tickets is {ripoff_profit:.2f} lv.')
