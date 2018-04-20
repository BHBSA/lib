import json
with open('city.json','r+') as f:
    standard_city_dict = json.loads(f.read())
with open('region.json','r+') as f:
    standard_block_dict = json.loads(f.read())

def standard_city(city_name):
    for i in standard_city_dict.items():
        for city in i[1]:
            if city in city_name:
                return i[0]
            else:
                continue
    print("无法标准化")
    return city_name

def standard_block(region_name):
    for i in standard_block_dict.items():
        for block in i[1]:
            if block in region_name:
                # print(i[0])
                return i[0]
            else:
                continue
    print('无法标准化')
    return region_name

if __name__ == '__main__':
    standard_city('   珠海市  ' )