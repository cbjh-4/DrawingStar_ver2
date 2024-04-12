from drawing_stars.star_drawer import StarDrawer
from flask import Flask, render_template, request

app = Flask(__name__)

#http://localhost:5050/

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/star', methods=['GET'])
def start():
    return render_template('star01.html')

@app.route('/star_draw', methods=['POST'])
def start_draw():
    #star01.html에서 submit으로 보낸 name alias, num_lines를 request.form으로 반환받는다.
    alais = request.form['alias']
    drawing_char = request.form['drawing_char']
    drawing_shape = request.form['drawing_shape']
    num_lines = int(request.form['num_lines'])

    stardrawer = StarDrawer(alias = alais, num_lines = num_lines, drawing_char = drawing_char, drawing_shape = drawing_shape)
    #drawing_str = 별 찍은 것을 문자열로 반환한 값
    drawing_str = stardrawer.draw_stars()

    return render_template('star02.html', drawing=drawing_str)

if __name__ == '__main__':
    # 0.0.0.0은 모든 포트에서 접근을 허용한다는 뜻, port 번호는 5050
    app.run(host='0.0.0.0', port='5050', debug=True)