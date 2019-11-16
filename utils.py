import json


def get_one_data(file_path, key, value):
    dataList = []
    with open(file_path, "r", encoding="utf-8") as f:
        keyList = json.loads(f.read()).get(key)
        for one_data in keyList:
            dataList.append(one_data.get(value))
    return dataList


if __name__ == '__main__':
    print(get_one_data("./data/ipData.json", "iplist", "ip"))
    print(get_one_data("./data/moblieData.json", "moblielist", "moblie"))
