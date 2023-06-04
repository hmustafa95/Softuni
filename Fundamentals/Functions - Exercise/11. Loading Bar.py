def percentage(a):
    any_list = []
    if a < 100:
        bar_percent = '%' * (a // 10)
        dot_percent = '.' * (10 - a // 10)
        any_list.append(bar_percent)
        any_list.append(dot_percent)
        return f'{a}% [{"".join(any_list)}] \nStill loading...'
    else:
        return f'100% Complete! \n[%%%%%%%%%%]'

percent = int(input())
print(percentage(percent))
