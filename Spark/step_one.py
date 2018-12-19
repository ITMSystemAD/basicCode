import sys
import json

sys.stdout = open('json_result_processing.json', 'wt',encoding='utf-8')
data1 = open("json_result.json", 'r',encoding='utf-8').read().replace('}}{', '}}\n{')
print(data1)