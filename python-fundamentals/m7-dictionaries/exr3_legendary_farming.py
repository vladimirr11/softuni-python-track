from collections import defaultdict

key_materials_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_dict = defaultdict(int)

winner = ''

while winner == '':
    string_input = input().lower().split(' ')
    for index in range(0, len(string_input), 2):
        item_name = string_input[index + 1]
        item_quantity = int(string_input[index])

        if item_name in key_materials_dict:
            key_materials_dict[item_name] += item_quantity
            if key_materials_dict[item_name] >= 250:
                winner = item_name
                break
        else:
            junk_dict[item_name] += item_quantity


key_materials_dict[winner] -= 250

winner_item_dict = {
    'shards': 'Shadowmourne',
    'fragments': 'Valanyr',
    'motes': 'Dragonwrath'
}

sorted_key_materials = dict(
    sorted(key_materials_dict.items(), key=lambda x: (-x[1], x[0])))
sorted_junk_materials = dict(sorted(junk_dict.items(), key=lambda x: x[0]))


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


print(f'{winner_item_dict[winner]} obtained!')
print_dict(sorted_key_materials, '{}: {}')
print_dict(sorted_junk_materials, '{}: {}')
