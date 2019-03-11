import json


def main():
    with open('dev.json', 'r') as in_f:
        json_data = json.load(in_f)

    print(json_data.keys())  # data
    print(len(json_data['data']))  # 1000
    print(json_data['data'][0].keys())  # dict_keys(['title', 'paragraphs'])
    print(json_data['data'][0]['title'])
    print(len(json_data['data'][0]['paragraphs']))  # 1
    print(json_data['data'][0]['paragraphs'][0].keys())  # dict_keys(['context', 'qas', 'id'])
    print(json_data['data'][0]['paragraphs'][0]['context'])
    print(json_data['data'][0]['paragraphs'][0]['qas'])


if __name__ == '__main__':
    main()
