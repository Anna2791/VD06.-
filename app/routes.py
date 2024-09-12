from flask import render_template, request, redirect, url_for
from app import app

ankets = []

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Проверка на наличие данных перед добавлением
        if name and city and hobby and age:
            anketa = {'name': name, 'city': city, 'hobby': hobby, 'age': age}
            ankets.append(anketa)
            # Используется для обновления страницы и предотвращения повторной отправки формы
            return render_template('anketa.html', ankets=ankets, submitted_anketa=anketa)

    # Возвращает отрендеренный шаблон с переданными данными анкет
    return render_template('anketa.html', ankets=ankets, submitted_anketa=None)