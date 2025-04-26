from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# База данных предметов
ITEMS = {
    'ice_coal': {
        'name': '❄️ Ледяной уголь',
        'price': 700,
        'image': 'https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpot621FAR17PLfYQJH5d2zhr-ZkvD8J_WDkjlVvZJ03O3A9I_j3Qew_BY_ZGG1JY-Sd1I_MFjX-lTqk-nq1pO_v8jLn3Jg7HIl5XfDn1a3iBAdPw/360fx360f',
        'desc': 'Эксклюзивный узор для ножей'
    },
    'redline': {
        'name': '🔴 AK-47 | Красная линия',
        'price': 1500,
        'image': 'https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpou-6kejhz2v_Nfz5H_uO1gb-Gm_b5J4Tdn2xZ_Pp9jL2Uod-h3Fbk_RY_YTqhI4-Hcgc9Z1nW-QS6xO3p0Za5vJnNzHJ9-nRztynbl0e2iBodPw/360fx360f',
        'desc': 'Легендарный скин для AK-47'
    }
}

@app.route('/')
def home():
    """Главная страница с предметами"""
    return render_template('index.html', items=ITEMS)

@app.route('/item/<item_id>')
def show_item(item_id):
    """Страница предмета"""
    item = ITEMS.get(item_id)
    if not item:
        return "Предмет не найден", 404
    return render_template('item.html', item=item)

@app.route('/buy', methods=['POST'])
def buy_item():
    """Обработка покупки"""
    item_id = request.form.get('item_id')
    item = ITEMS.get(item_id)
    
    if not item:
        return jsonify({'status': 'error', 'message': 'Предмет не найден'})
    
    # Здесь должна быть логика обработки платежа
    return jsonify({
        'status': 'success',
        'message': f'Вы купили {item["name"]} за {item["price"]} монет!'
    })

if __name__ == '__main__':
    app.run(debug=True)