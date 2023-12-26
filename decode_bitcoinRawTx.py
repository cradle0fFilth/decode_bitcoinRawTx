from bitcoinlib.transactions import Transaction,transaction_deserialize
import requests
from dotenv import load_dotenv
import os
# 加载 .env 文件
load_dotenv()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
txid = os.environ.get("txid")
print("txid:",txid)
url = 'https://mempool.space/api/tx/{}/hex'.format(txid)

res = requests.get(url,headers=headers)
rawTx = res.text
tx = transaction_deserialize(rawTx)
print(tx.as_json())