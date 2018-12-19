import os

os.system('spark-submit filter.py')
os.system('python3 convert_to_json.py')
os.system('python3 step_one.py')
os.system('python3 step_two.py')
os.system('sudo scp /home/cloudera/Documents/final_json_for_kibana.json yong@10.20.25.5:/Users/yong/elasticsearch-6.5.2/bin/test.json')
