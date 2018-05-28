"""
格式化城市区域
"""

import json
from lib.region_block import region_block
from lib.log import LogHandler

log = LogHandler(__name__)
with open('lib/city.json', 'r+') as f:
    standard_city_dict = json.loads(f.read())

standard_block_dict = region_block()


def standard_city(city_name):
    """

    :param city_name: 城市名称
    :return: 城市名称
    """
    for i in standard_city_dict.items():
        for city in i[1]:
            if city and i[0] in city_name:
                return True, i[0]
            else:
                continue
    log.error("城市无法标准化：{}".format(city_name))
    return False, city_name


def standard_block(city_name, region_name):
    """

    :param city_name: 城市名称
    :param region_name: 区域
    :return: 区域
    """
    city = standard_city(city_name)[1]
    for i in standard_block_dict.items():
        if city == i[0]:
            for block in i[1].items():
                for n in block[1]:
                    if n in region_name:
                        return True, block[0]
    log.error('区域无法标准化，城市：{}，区域：{}'.format(city_name, region_name))
    return False, region_name


if __name__ == '__main__':
    # standard_city('   珠海市  ')
    standard_block('北京', '[朝阳]百子湾')
