from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import color_test
import logging
import json
import loging


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/' # Путь к месту хранения сохранённого файла
app.secret_key = "my_secret key" # Секретный ключ
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif']) # Доступные форматы картинок


def allowed_file(filename): # Проверка файла на правильность формата
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    loging.addLogging({'level': 'debug', 'message': 'Вход на сайт'})
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    loging.addLogging({'level': 'debug', 'message': 'Передача POST'})
    if 'file' not in request.files:
        flash('Фаил не выбран')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('Поля не заполнены. Выберете изображение и укажите HAX-код.')
        return redirect(request.url)
    if not color_test.color_input_validation(request.form['need_color']):
        flash('HAX-код указан неверно.')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Изображение успешно загружно. Подсчёт количества пикселей показан ниже.')
        n_color = request.form['need_color']
        pix_inf = color_test.Count_Pixel(n_color, file.filename)
        return render_template('index.html', filename=filename, black=pix_inf[0], white=pix_inf[1], color=pix_inf[2], massage_1=pix_inf[3], qqq1=n_color)
    else:
        flash('Допустимы следующие форматы файлов - png, jpg, jpeg, gif')
        return redirect(request.url)


if __name__ == "__main__":
    app.run(debug=True)

