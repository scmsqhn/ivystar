#!encoding=utf-8

# 将路径配置入环境变量

import os

PROJECT_PATH = os.getenv("PROJECT_PATH")
SIGNATURE_FILE_PATH = os.getenv("SIGNATURE_FILE_PATH")
BERT_MODEL_PATH = os.getenv("BERT_MODEL_PATH")
MONGO_IP= os.getenv("MONGO_IP")
MONGO_PORT= os.getenv("MONGO_PORT")

print(PROJECT_PATH, SIGNATURE_FILE_PATH, BERT_MODEL_PATH, MONGO_IP, MONGO_PORT)

# 'bert/chinese_L-12_H-768_A-12/bert_config.json'
