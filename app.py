import stripe
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# CONFIGURACIÓN STRIPE
stripe.api_key = 'sk_test_51RgwiC03V20xU4mqVhWE7AQDzWQKDWBKAGACOoD0QJ1YnCz3EWDp8wFckB60KvP1gZQvKnHtGynXzohWUFIAm49K00KjL2ufMT'

# CONFIGURACIÓN DE EMAIL
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'augustoagi12345@gmail.com'
app.config['MAIL_PASSWORD'] = 'fzdf jcnr cibf ehyp'
mail = Mail(app)

# Renders ------------------------------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consejos/batidos')
def batidos():
    return render_template('pagos/batidos.html')

@app.route('/consejos/tipsyConsejos')
def tipsyConsejos():
    return render_template('pagos/tipsyConsejos.html')    

@app.route('/rutina/rutinaPersonalizada')
def rutinaPersonalizada2():
    return render_template('pagos/rutinaPersonalizada.html')

@app.route('/gluteos/gluteosPrimerMes')
def gluteosPrimerMes():
    return render_template('pagos/gluteosPrimerMes.html')

@app.route('/gluteos/gluteosSegundoMes')
def gluteosSedundoMes():
    return render_template('pagos/gluteosSegundoMes.html')   

@app.route('/gluteos/gluteos90dias')
def gluteos90Dias():
    return render_template('pagos/gluteos90dias.html')

@app.route('/gluteos/gluteos1hrentrenamiento')
def gluteos1hrEntrenamiento():
    return render_template('pagos/gluteos1hrentrenamiento.html')    

@app.route('/cuerpoCompleto/CuerpoCompletoPrimerMes')
def cuerpoCompletoPrimerMes():
    return render_template('pagos/cuerpoCompletoPrimerMes.html')

@app.route('/cuerpoCompleto/CuerpoCompletoSegundoMes')
def cuerpoCompletoSegundoMes():
    return render_template('pagos/cuerpoCompletoSegundoMes.html')


@app.route('/cuerpoCompleto/CuerpoCompleto90Dias')
def cuerpoCompleto90Dias():
    return render_template('pagos/cuerpoCompleto90Dias.html')

@app.route('/cuerpoCompleto/CuerpoCompleto1hrEntrenamiento')
def cuerpoCompleto1hrEntrenamiento():
    return render_template('pagos/cuerpoCompleto1hrEntrenamiento.html')


@app.route('/cuerpoCompleto')
def cuerpoCompleto():
    return render_template('cuerpoCompleto.html')

@app.route('/testimonios')
def restimonios():
    return render_template('testimonios.html')

@app.route('/licuados')
def licuados():
    return render_template('licuados.html')    

@app.route('/rutinaPersonalizada')
def rutinaPersonalizada():
    return render_template('rutinaPersonalizada.html')    

@app.route('/rutinaGluteos')
def rutinaGluteos():
    return render_template('rutinaGluteos.html')

# Links de pagos ------------------------------------------------------------------------------------------

@app.route('/tipsYconsejos', methods=['POST'])
def create_checkout_session11():
    email_cliente = request.form['email']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Tips y consejos',
                    'description': '¡Con este programa llegaras sin duda al SIGUIENTE NIVEL, Creare tu alimentación y rutinas de entrenamiento personalizadas para ti! Tendrás comunicación via whatsaap para que podamos ir revisando día a dia como te sientes y tu progreso, para así poderte guiarte para que juntos lograremos ese cuerpo que sueñas, así que si decides hacer este programa es porque realmente quieres tomarte esto en serio y quieres ver grandes resultados',
                },
                'unit_amount': 1500,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('success', _external=True) + '?email=' + email_cliente,
        cancel_url=url_for('index', _external=True),
    )
    return redirect(session.url, code=303)


@app.route('/batidos', methods=['POST'])
def create_checkout_session10():
    email_cliente = request.form['email']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Batidos',
                    'description': '¡Con este programa llegaras sin duda al SIGUIENTE NIVEL, Creare tu alimentación y rutinas de entrenamiento personalizadas para ti! Tendrás comunicación via whatsaap para que podamos ir revisando día a dia como te sientes y tu progreso, para así poderte guiarte para que juntos lograremos ese cuerpo que sueñas, así que si decides hacer este programa es porque realmente quieres tomarte esto en serio y quieres ver grandes resultados',
                },
                'unit_amount': 1500,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('success', _external=True) + '?email=' + email_cliente,
        cancel_url=url_for('index', _external=True),
    )
    return redirect(session.url, code=303)


@app.route('/rutina_personalizada', methods=['POST'])
def create_checkout_session9():
    email_cliente = request.form['email']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Rutina personalizada',
                    'description': '¡Con este programa llegaras sin duda al SIGUIENTE NIVEL, Creare tu alimentación y rutinas de entrenamiento personalizadas para ti! Tendrás comunicación via whatsaap para que podamos ir revisando día a dia como te sientes y tu progreso, para así poderte guiarte para que juntos lograremos ese cuerpo que sueñas, así que si decides hacer este programa es porque realmente quieres tomarte esto en serio y quieres ver grandes resultados',
                },
                'unit_amount': 5000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('success', _external=True) + '?email=' + email_cliente,
        cancel_url=url_for('index', _external=True),
    )
    return redirect(session.url, code=303)


@app.route('/gluteos_1_hr', methods=['POST'])
def create_checkout_session8():
    email_cliente = request.form['email']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Programa 1hr entrenamiento conmigo',
                    'description': 'En este programa encontraras mis rutinas de entrenamientos más efectivas para hacer mejorar tus piernas especialmente tus GLUTEOS. Te ayudara a ver un excelente cambio para que se vean más fuerte, levantados y grandes. Mejorando tu fuerza y resistencia.',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('success', _external=True) + '?email=' + email_cliente,
        cancel_url=url_for('index', _external=True),
    )
    return redirect(session.url, code=303)

@app.route('/gluteos_90_dias', methods=['POST'])
def create_checkout_session7():
    email_cliente = request.form['email']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Programa 90 dias',
                    'description': 'En este programa encontraras mis rutinas de entrenamientos más efectivas para hacer mejorar tus piernas especialmente tus GLUTEOS. Te ayudara a ver un excelente cambio para que se vean más fuerte, levantados y grandes. Mejorando tu fuerza y resistencia.',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('success', _external=True) + '?email=' + email_cliente,
        cancel_url=url_for('index', _external=True),
    )
    return redirect(session.url, code=303)

@app.route('/gluteos_segundo_mes', methods=['POST'])
def create_checkout_session6():
    email_cliente = request.form['email']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Programa segundo mes',
                    'description': 'En este programa encontraras mis rutinas de entrenamientos más efectivas para hacer mejorar tus piernas especialmente tus GLUTEOS. Te ayudara a ver un excelente cambio para que se vean más fuerte, levantados y grandes. Mejorando tu fuerza y resistencia.',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('success', _external=True) + '?email=' + email_cliente,
        cancel_url=url_for('index', _external=True),
    )
    return redirect(session.url, code=303)

@app.route('/gluteos_primer_mes', methods=['POST'])
def create_checkout_session5():
    email_cliente = request.form['email']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Programa primer mes',
                    'description': 'En este programa encontraras mis rutinas de entrenamientos más efectivas para hacer mejorar tus piernas especialmente tus GLUTEOS. Te ayudara a ver un excelente cambio para que se vean más fuerte, levantados y grandes. Mejorando tu fuerza y resistencia.',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('success', _external=True) + '?email=' + email_cliente,
        cancel_url=url_for('index', _external=True),
    )
    return redirect(session.url, code=303)


@app.route('/programa_primer_mes', methods=['POST'])
def create_checkout_session():
    email_cliente = request.form['email']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Programa primer mes',
                    'description': 'Mi programa de entrenamiento cuerpo completo está diseñado para ayudarte a construir ese cuerpo que tanto has estado buscando una manera saludable y con una buena simetría corporal. será de 4/5 días de rutinas de entrenamiento efectivas para todas las partes de tu cuerpo.',
                },
                'unit_amount': 3000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('success', _external=True) + '?email=' + email_cliente,
        cancel_url=url_for('index', _external=True),
    )
    return redirect(session.url, code=303)

@app.route('/programa_segundo_mes', methods=['POST'])
def create_checkout_session2():
    email_cliente = request.form['email']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Programa segundo mes',
                    'description': 'Mi programa de entrenamiento cuerpo completo está diseñado para ayudarte a construir ese cuerpo que tanto has estado buscando una manera saludable y con una buena simetría corporal. será de 4/5 días de rutinas de entrenamiento efectivas para todas las partes de tu cuerpo.',
                },
                'unit_amount': 3000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('success', _external=True) + '?email=' + email_cliente,
        cancel_url=url_for('index', _external=True),
    )
    return redirect(session.url, code=303)

@app.route('/programa_90_dias', methods=['POST'])
def create_checkout_session3():
    email_cliente = request.form['email']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Programa 90 dias',
                    'description': 'Mi programa de entrenamiento cuerpo completo está diseñado para ayudarte a construir ese cuerpo que tanto has estado buscando una manera saludable y con una buena simetría corporal. será de 4/5 días de rutinas de entrenamiento efectivas para todas las partes de tu cuerpo.',
                },
                'unit_amount': 3000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('success', _external=True) + '?email=' + email_cliente,
        cancel_url=url_for('index', _external=True),
    )
    return redirect(session.url, code=303)

@app.route('/programa_1_hr', methods=['POST'])
def create_checkout_session4():
    email_cliente = request.form['email']

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Programa 1hr entrenamiento conmigo',
                    'description': 'Mi programa de entrenamiento cuerpo completo está diseñado para ayudarte a construir ese cuerpo que tanto has estado buscando una manera saludable y con una buena simetría corporal. será de 4/5 días de rutinas de entrenamiento efectivas para todas las partes de tu cuerpo.',
                },
                'unit_amount': 3000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('success', _external=True) + '?email=' + email_cliente,
        cancel_url=url_for('index', _external=True),
    )
    return redirect(session.url, code=303)                

@app.route('/success')
def success():
    email = request.args.get('email')

    msg = Message('Gracias por tu compra', sender='tu_correo@gmail.com', recipients=[email])
    msg.body = 'Aquí está tu archivo.'
    with app.open_resource("archivo_para_enviar.pdf") as adj:
        msg.attach("archivo_para_enviar.pdf", "application/pdf", adj.read())
    mail.send(msg)

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
