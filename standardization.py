"""
格式化城市区域
"""

import json
from lib.region_block import block_region

with open('lib/city.json', 'r+') as f:
    standard_city_dict = json.loads(f.read())
# with open('region.json', 'r+') as f:
#     standard_block_dict = json.loads(f.read())
#     print(standard_block_dict)
standard_block_dict  = block_region()
def standard_city(city_name):
    """

    :param city_name: 城市名称
    :return: 城市名称
    """
    for i in standard_city_dict.items():
        for city in i[1]:
            if city and i[0] in city_name:
                # print(i[0])
                return i[0]
            else:
                continue
    print("无法标准化")
    return city_name


def standard_block(city_name,region_name):
    """

    :param region_name: 区域
    :return: 区域
    """
    city = standard_city(city_name)
    for i in standard_block_dict.items():
        if city == i[1][0]:
            for block in i[1][1]:
                if block in region_name:
                    print(i[0])
                    return i[0]
                else:
                    continue
    print('无法标准化')
    # print(region_name)
    return region_name


if __name__ == '__main__':
    # standard_city('   珠海市  ')
    standard_block('上海','浦东惠南')
