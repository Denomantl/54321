from flask import Flask, render_template
from werkzeug.utils import redirect
from data import db_session
from data.users import User
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/two_cat', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            if float(form.password.data.replace(' ', '')) > 0 and \
                    float(form.email.data.replace(' ', '')) > 0:
                return render_template('register.html', title='Калькулятор',
                                       form=form,
                                       message=("Ваш результат: " +
                                                str(
                                                    0.5 * float(
                                                        form.password.data) *
                                                    float(
                                                        form.email.data))))
            elif float(form.password.data.replace(' ', '')) <= 0 or \
                    float(form.email.data.replace(' ', '')) <= 0:
                return render_template('register.html', title='Калькулятор',
                                       form=form,
                                       message=
                                       "Один или несколько параметров равны 0 "
                                       "или отрицательны")
        except ValueError:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message=
                                   "Не указан 1 или несколько параметров")

    return render_template('register.html', title='Через 2 катета', form=form)


def main():
    app.run()


if __name__ == '__main__':
    main()
