import json
import collections

def tree():
		return collections.defaultdict(tree)

dict_tree = tree()

info_dict = { "gu": 'gu', "name": 'name', "date": 'date', "category": 'category'}

indexx = input("put index name")
with open('result.txt') as f:
		with open('json_result.json', 'w', encoding='utf-8') as output:
				for line in f:
						_list = line.split(',')
						if '\n' not in _list:
								dict_tree["index"]["_index"] = indexx
								dict_tree["index"]["_type"] = "restrecord"
								dict_tree["index"]["_id"] = _list[0]
								info_dict["gu"] = _list[1]
								info_dict["name"] = _list[2]
								info_dict["date"] = _list[3]
								info_dict["category"] =_list[4].rstrip()
								json.dump(dict_tree, output, ensure_ascii=False, indent=None)
								json.dump(info_dict, output, ensure_ascii=False, indent=None)
