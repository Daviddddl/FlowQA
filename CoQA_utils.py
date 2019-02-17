import json
import PERQAInstance
import prepare

# raw_data_f = open('data/zh_session_ano.json', 'r')
# raw_data_json = json.load(raw_data_f)


def gen_split_id_list():
    for each_data_type in ['train', 'dev', 'test']:
        each_data_base_path = 'data/' + each_data_type
        with open(each_data_base_path + '_ids.txt', 'w+') as res_f:
            for each_ins in prepare.load_instances(each_data_base_path + '.pkl'):
                res_f.write(each_ins.get_qa_id() + '\n')


# for each_split in ['train', 'dev', 'test']:
#     with open('data/perqa_' + each_split + '.json', 'w+') as perqa_raw_qa_json:
#         raw_qa_json = {"version": "1.0"}
#         raw_qa_json_data_list = []
#         each_data_json = {"source": "douban"}
#         for each_ins in prepare.load_instances('data/' + each_split + '.pkl'):
#             each_data_json['id'] = each_ins.get_qa_id()
#             each_data_json['filename'] = "null"
#             each_data_json['story'] = str(each_ins.session)
#             each_data_json['questions'] = []
#             for each_qa in raw_data_json[each_ins.name][]
#
#
#
#
# with open('CoQA/train.json', 'r') as f:
#     json_data = json.load(f)
#     data_1 = json_data['data'][0]
#     print(data_1.keys())


if __name__ == '__main__':
    gen_split_id_list()
