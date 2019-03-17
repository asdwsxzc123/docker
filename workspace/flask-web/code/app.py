# coding:utf-8
import time
import redis
from flask import Flask
app = Flask(__name__)
# 此处host是docker-compose.yaml配置文件中redis服务的名称
cache = redis.Redis(host='127.0.0.1', port=6379, password='geesunn')
def get_hit_commit():
  """ 利用redis统计访问次数 """
  retries = 5
  while True:
    try:
      return cache.incr('hits')
    except redis.exceptions.ConnectionError as e:
      if retries == 0:
        raise e
      retries -= 1
      time.sleep(0.5)
@app.route('/')
def main():
  count = get_hit_commit()
  return '欢迎访问!网站已经累计访问{}次\n'.format(count)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)