from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

stores=[
    {
        'name':'my wonderful store',
        'items': [
            {
                'name':'my item',
                'price':15.99
            }
            ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
    reques_data=request.get_json()
    new_store={
        'name':request_data['name'],
        'items':[]}
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:names>')
def get_store(name):
    for store in stores:
        if store ['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

@app.route('/store/<string:name>/items', methods=['POST'])
def create_item_in_store(name):
    reques_data=request.get_json()
    for store in stores:
        if store ['name'] == names:
            new_items={
                'name':request_data['name'],
                'price':request_data['price']}
            store['items'].append(new_items)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/items')
def get_items_in_store():
    for store in stores:
        if store ['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message': 'store not found'})

app.run(port=5000)
