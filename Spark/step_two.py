import json
import sys

sys.stdout = open('final_json_for_kibana.json', 'wt',encoding='utf-8')
data1 = open("json_result_processing.json", 'r',encoding='utf-8').read().replace('}{', '}\n{')
print(data1)
