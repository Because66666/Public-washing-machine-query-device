from flask import Flask,render_template
import requests
from datetime import datetime


req_session = requests.Session()
headers = {
    'User-Agent': 'okhttp/4.3.1',
    # 'Accept-Encoding': 'gzip',
    'authorization': '*************',
    'x-mobile-brand': 'OPPO',
    'x-app-code': 'BA',
    'weex-version': '1.1.43',
    'x-app-version': '2.4.8',
    'x-mobile-model': 'PGJM10',
    'content-type': 'application/json; charset=utf-8',
    'Cookie': '*********',
}

req_session.headers=headers
app = Flask(__name__)

@app.route('/')
def index():
    right = False
    left = False
    right_4 = False
    left_4 = False
    info = None
    try:
        json_data = {
            'qrCode': 'https://q.ujing.com.cn/ucqrc/index.html?cd=755501240130321074',
        }
        url='https://phoenix.ujing.online/api/v1/devices/scanWasherCode'
        # 左边洗衣机
        ans_left = req_session.post(url,json=json_data)
        if ans_left.status_code == 200:
            left = ans_left.json()['data']['result']['createOrderEnabled']
        else:
            left = ans_left.text
        # 右边洗衣机
        json_data = {
            'qrCode': 'https://q.ujing.com.cn/ucqrc/index.html?cd=755501240412324394',
        }
        ans_rignt = req_session.post(url,json=json_data)
        if ans_rignt.status_code == 200:
            right = ans_rignt.json()['data']['result']['createOrderEnabled']
        else:
            right = ans_rignt.text
        # 四层洗衣机左边
        json_data = {
            'qrCode': 'https://q.ujing.com.cn/ucqrc/index.html?cd=755501240412324394',
        }
        ans_rignt = req_session.post(url,json=json_data)
        if ans_rignt.status_code == 200:
            left_4 = ans_rignt.json()['data']['result']['createOrderEnabled']
        else:
            left_4 = ans_rignt.text
        # 四层洗衣机右边
        json_data = {
            'qrCode': 'https://q.ujing.com.cn/ucqrc/index.html?cd=755501240412325203',
        }
        ans_rignt = req_session.post(url,json=json_data)
        if ans_rignt.status_code == 200:
            right_4 = ans_rignt.json()['data']['result']['createOrderEnabled']
        else:
            right_4 = ans_rignt.text


        data = {
            'left': left,
            'right': right,
            'left_4': left_4,
            'right_4': right_4,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    except Exception as e:
        info = str(e)
        data = {
            'left': None,
            'right': None,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'info': info
        }
    return render_template('main.html', data=data)



if __name__ == '__main__':
    app.run(port=2111,debug=True)