legendary_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_items = {}
built_legendary = False

while built_legendary is False:
    rcvd_list = input().split(' ')
    for index in range(0, len(rcvd_list), 2):
        item = rcvd_list[index + 1].lower()
        quantity = int(rcvd_list[index])
        if item in legendary_items:
            legendary_items[item] += quantity
        else:
            if item not in junk_items:
                junk_items[item] = 0
            junk_items[item] += quantity
        if legendary_items['shards'] >= 250:
            print('Shadowmourne obtained!')
            legendary_items['shards'] -= 250
            for key, value in legendary_items.items():
                print(f"{key}: {value}")
            for key, value in junk_items.items():
                print(f"{key}: {value}")
            built_legendary = True
            if built_legendary:
                break
        elif legendary_items['fragments'] >= 250:
            print('Valanyr obtained!')
            legendary_items['fragments'] -= 250
            for key, value in legendary_items.items():
                print(f"{key}: {value}")
            for key, value in junk_items.items():
                print(f"{key}: {value}")
            built_legendary = True
            if built_legendary:
                break
        elif legendary_items['motes'] >= 250:
            print('Dragonwrath obtained!')
            legendary_items['motes'] -= 250
            for key, value in legendary_items.items():
                print(f"{key}: {value}")
            for key, value in junk_items.items():
                print(f"{key}: {value}")
            built_legendary = True
            if built_legendary:
                break
