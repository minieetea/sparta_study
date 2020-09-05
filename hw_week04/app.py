from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기 
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 주문자이름, 수량, 주소, 전화번호을 받아온다.
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    print("받아온 값:", name_receive, quantity_receive, address_receive, phone_receive)

    # 2. mongoDB에 데이터 넣기
    order = {
        'name': name_receive,
        'quantity': quantity_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    db.myshops.insert_one(order)
    return jsonify({'result': 'success'})
  

# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
    orders = list(db.alonememo.find({}, {'_id': False}))

    # 2. orders라는 키 값으로 주문정보 보내주기
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
