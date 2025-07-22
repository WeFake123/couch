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
app.config['MAIL_USERNAME'] = 'Davidtorres.fitness1@gmail.com'
app.config['MAIL_PASSWORD'] = 'csed ugal lbdw afat'
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
        success_url=url_for('successTipsyConsejos', _external=True) + '?email=' + email_cliente,
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
        success_url=url_for('successBatidos', _external=True) + '?email=' + email_cliente,
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
                'unit_amount': 12000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('successRutinaPersonalizada', _external=True) + '?email=' + email_cliente,
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
                'unit_amount': 5000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('successGluteos1hr', _external=True) + '?email=' + email_cliente,
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
                'unit_amount': 6000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('successGluteos90dias', _external=True) + '?email=' + email_cliente,
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
                'unit_amount': 2500,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('successGluteos2doMes', _external=True) + '?email=' + email_cliente,
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
                'unit_amount': 2500,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('successGluteos1erMes', _external=True) + '?email=' + email_cliente,
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
        success_url=url_for('successCuerpoCompletoPrimerMes', _external=True) + '?email=' + email_cliente,
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
        success_url=url_for('successCuerpoCompleto2Mes', _external=True) + '?email=' + email_cliente,
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
                'unit_amount': 5000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('successPrograma90dias', _external=True) + '?email=' + email_cliente,
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
                'unit_amount': 5000,
            },
            'quantity': 1,
        }],
        mode='payment',
        customer_email=email_cliente,
        success_url=url_for('successPrograma1hr', _external=True) + '?email=' + email_cliente,
        cancel_url=url_for('index', _external=True),
    )
    return redirect(session.url, code=303)                
# ------------------------------------------------------------------------------------.
@app.route('/successTipsyConsejos') 
def successTipsyConsejos():
    email = request.args.get('email')

    msg = Message('Gracias por tu compra', sender='tu_correo@gmail.com', recipients=[email])
    msg.body = "Hola! Espero tu dia vaya increible ! Excelente que hayas tomado la decision de empezar con este programa que he construido en base a tus objetivos. Recueda que la constancia y disciplina seran indispensables para lograr ver resultados. Una buena alimentacion sera tambien parte importante para que el entrenamiento en el gimnacio muestre los resultados en tu cuerpo. Recuerda descansar bien y mantenerte siempre hidratando tu cuerpo. Todo esto hace parte de una mente, cuerpo y espiritu en balance. Recuerda que tambien ofrezco a mis clientes clases por videollamada para que asi podamos entrenar juntos y yo revisar las tecnicas, velocidad del movimiento, respiracion y postura correcta del cuerpo. Enviame un email y asi puedo darte mas informacion sobre las clases.Vamos a entrenar con toda la energia!! Hey! I hope your day is going amazing! It's great that you've decided to start this program, which I've built based on your goals. Remember that consistency and discipline will be essential to see results. A good diet will also be an important part of ensuring your gym workouts show results in your body. Remember to get plenty of rest and stay hydrated. All of this is part of a balanced mind, body, and spirit. Remember that I also offer video call classes, I give these classes to people all around the world thought the phone so I can review technique, speed of movement, breathing, and proper body posture. Send me an email so I can give you more information about the classes. Let's train with all our energy!! David Torres WELLNESS COACH"
    with app.open_resource("Presentacion.pdf") as adj:
        msg.attach("Presentacion.pdf", "application/pdf", adj.read())
    mail.send(msg)

    return render_template('success.html')

@app.route('/successBatidos')
def successBatidos():
    email = request.args.get('email')

    msg = Message('Gracias por tu compra', sender='tu_correo@gmail.com', recipients=[email])
    msg.body = "Hola! Espero tu dia vaya increible ! Excelente que hayas tomado la decision de empezar con este programa que he construido en base a tus objetivos. Recueda que la constancia y disciplina seran indispensables para lograr ver resultados. Una buena alimentacion sera tambien parte importante para que el entrenamiento en el gimnacio muestre los resultados en tu cuerpo. Recuerda descansar bien y mantenerte siempre hidratando tu cuerpo. Todo esto hace parte de una mente, cuerpo y espiritu en balance. Recuerda que tambien ofrezco a mis clientes clases por videollamada para que asi podamos entrenar juntos y yo revisar las tecnicas, velocidad del movimiento, respiracion y postura correcta del cuerpo. Enviame un email y asi puedo darte mas informacion sobre las clases.Vamos a entrenar con toda la energia!! Hey! I hope your day is going amazing! It's great that you've decided to start this program, which I've built based on your goals. Remember that consistency and discipline will be essential to see results. A good diet will also be an important part of ensuring your gym workouts show results in your body. Remember to get plenty of rest and stay hydrated. All of this is part of a balanced mind, body, and spirit. Remember that I also offer video call classes, I give these classes to people all around the world thought the phone so I can review technique, speed of movement, breathing, and proper body posture. Send me an email so I can give you more information about the classes. Let's train with all our energy!! David Torres WELLNESS COACH"
    with app.open_resource("Batidos(español).pdf") as adj:
        msg.attach("Batidos(español).pdf", "application/pdf", adj.read())
    with app.open_resource("Batidos(ingles).pdf") as adj:
        msg.attach("Batidos(ingles).pdf", "application/pdf", adj.read())    
    mail.send(msg)

    return render_template('success.html')    

@app.route('/successRutinaPersonalizada')
def successRutinaPersonalizada():
    email = request.args.get('email')

    msg = Message('Gracias por tu compra', sender='tu_correo@gmail.com', recipients=[email])
    msg.body = "Hola! Espero tu dia vaya increible ! Excelente que hayas tomado la decision de empezar con este programa que he construido en base a tus objetivos. Recueda que la constancia y disciplina seran indispensables para lograr ver resultados. Una buena alimentacion sera tambien parte importante para que el entrenamiento en el gimnacio muestre los resultados en tu cuerpo. Recuerda descansar bien y mantenerte siempre hidratando tu cuerpo. Todo esto hace parte de una mente, cuerpo y espiritu en balance. Recuerda que tambien ofrezco a mis clientes clases por videollamada para que asi podamos entrenar juntos y yo revisar las tecnicas, velocidad del movimiento, respiracion y postura correcta del cuerpo. Enviame un email y asi puedo darte mas informacion sobre las clases.Vamos a entrenar con toda la energia!! Hey! I hope your day is going amazing! It's great that you've decided to start this program, which I've built based on your goals. Remember that consistency and discipline will be essential to see results. A good diet will also be an important part of ensuring your gym workouts show results in your body. Remember to get plenty of rest and stay hydrated. All of this is part of a balanced mind, body, and spirit. Remember that I also offer video call classes, I give these classes to people all around the world thought the phone so I can review technique, speed of movement, breathing, and proper body posture. Send me an email so I can give you more information about the classes. Let's train with all our energy!! David Torres WELLNESS COACH"
    with app.open_resource("Presentacion.pdf") as adj:
        msg.attach("Presentacion.pdf", "application/pdf", adj.read())   
    mail.send(msg)

    return render_template('success.html')   
@app.route('/successGluteos1hr')
def successGluteos1hr():
    email = request.args.get('email')

    msg = Message('Gracias por tu compra', sender='tu_correo@gmail.com', recipients=[email])
    msg.body = "Hola! Espero tu dia vaya increible ! Excelente que hayas tomado la decision de empezar con este programa que he construido en base a tus objetivos. Recueda que la constancia y disciplina seran indispensables para lograr ver resultados. Una buena alimentacion sera tambien parte importante para que el entrenamiento en el gimnacio muestre los resultados en tu cuerpo. Recuerda descansar bien y mantenerte siempre hidratando tu cuerpo. Todo esto hace parte de una mente, cuerpo y espiritu en balance. Recuerda que tambien ofrezco a mis clientes clases por videollamada para que asi podamos entrenar juntos y yo revisar las tecnicas, velocidad del movimiento, respiracion y postura correcta del cuerpo. Enviame un email y asi puedo darte mas informacion sobre las clases.Vamos a entrenar con toda la energia!! Hey! I hope your day is going amazing! It's great that you've decided to start this program, which I've built based on your goals. Remember that consistency and discipline will be essential to see results. A good diet will also be an important part of ensuring your gym workouts show results in your body. Remember to get plenty of rest and stay hydrated. All of this is part of a balanced mind, body, and spirit. Remember that I also offer video call classes, I give these classes to people all around the world thought the phone so I can review technique, speed of movement, breathing, and proper body posture. Send me an email so I can give you more information about the classes. Let's train with all our energy!! David Torres WELLNESS COACH"
    with app.open_resource("Presentacion.pdf") as adj:
        msg.attach("Presentacion.pdf", "application/pdf", adj.read())   
    mail.send(msg)

    return render_template('success.html')  
# falta
@app.route('/successGluteos90dias')
def successGluteos90dias():
    email = request.args.get('email')

    msg = Message('Gracias por tu compra', sender='tu_correo@gmail.com', recipients=[email])
    msg.body = "Hola! Espero tu dia vaya increible ! Excelente que hayas tomado la decision de empezar con este programa que he construido en base a tus objetivos. Recueda que la constancia y disciplina seran indispensables para lograr ver resultados. Una buena alimentacion sera tambien parte importante para que el entrenamiento en el gimnacio muestre los resultados en tu cuerpo. Recuerda descansar bien y mantenerte siempre hidratando tu cuerpo. Todo esto hace parte de una mente, cuerpo y espiritu en balance. Recuerda que tambien ofrezco a mis clientes clases por videollamada para que asi podamos entrenar juntos y yo revisar las tecnicas, velocidad del movimiento, respiracion y postura correcta del cuerpo. Enviame un email y asi puedo darte mas informacion sobre las clases.Vamos a entrenar con toda la energia!! Hey! I hope your day is going amazing! It's great that you've decided to start this program, which I've built based on your goals. Remember that consistency and discipline will be essential to see results. A good diet will also be an important part of ensuring your gym workouts show results in your body. Remember to get plenty of rest and stay hydrated. All of this is part of a balanced mind, body, and spirit. Remember that I also offer video call classes, I give these classes to people all around the world thought the phone so I can review technique, speed of movement, breathing, and proper body posture. Send me an email so I can give you more information about the classes. Let's train with all our energy!! David Torres WELLNESS COACH"
    with app.open_resource("archivo_para_enviar.pdf") as adj:
        msg.attach("archivo_para_enviar.pdf", "application/pdf", adj.read())   
    mail.send(msg)

    return render_template('success.html')  

@app.route('/successGluteos2doMes')
def successGluteos2doMes():
    email = request.args.get('email')

    msg = Message('Gracias por tu compra', sender='tu_correo@gmail.com', recipients=[email])
    msg.body = "Hola! Espero tu dia vaya increible ! Excelente que hayas tomado la decision de empezar con este programa que he construido en base a tus objetivos. Recueda que la constancia y disciplina seran indispensables para lograr ver resultados. Una buena alimentacion sera tambien parte importante para que el entrenamiento en el gimnacio muestre los resultados en tu cuerpo. Recuerda descansar bien y mantenerte siempre hidratando tu cuerpo. Todo esto hace parte de una mente, cuerpo y espiritu en balance. Recuerda que tambien ofrezco a mis clientes clases por videollamada para que asi podamos entrenar juntos y yo revisar las tecnicas, velocidad del movimiento, respiracion y postura correcta del cuerpo. Enviame un email y asi puedo darte mas informacion sobre las clases.Vamos a entrenar con toda la energia!! Hey! I hope your day is going amazing! It's great that you've decided to start this program, which I've built based on your goals. Remember that consistency and discipline will be essential to see results. A good diet will also be an important part of ensuring your gym workouts show results in your body. Remember to get plenty of rest and stay hydrated. All of this is part of a balanced mind, body, and spirit. Remember that I also offer video call classes, I give these classes to people all around the world thought the phone so I can review technique, speed of movement, breathing, and proper body posture. Send me an email so I can give you more information about the classes. Let's train with all our energy!! David Torres WELLNESS COACH"
    with app.open_resource("GluteosMes2(español).pdf") as adj:
        msg.attach("GluteosMes2(español).pdf", "application/pdf", adj.read())
    with app.open_resource("GluteosMes2(ingles).pdf") as adj:
        msg.attach("GluteosMes2(ingles).pdf", "application/pdf", adj.read())             
    mail.send(msg)

    return render_template('success.html') 

@app.route('/successGluteos1erMes')
def successGluteos1erMes():
    email = request.args.get('email')

    msg = Message('Gracias por tu compra', sender='tu_correo@gmail.com', recipients=[email])
    msg.body = "Hola! Espero tu dia vaya increible ! Excelente que hayas tomado la decision de empezar con este programa que he construido en base a tus objetivos. Recueda que la constancia y disciplina seran indispensables para lograr ver resultados. Una buena alimentacion sera tambien parte importante para que el entrenamiento en el gimnacio muestre los resultados en tu cuerpo. Recuerda descansar bien y mantenerte siempre hidratando tu cuerpo. Todo esto hace parte de una mente, cuerpo y espiritu en balance. Recuerda que tambien ofrezco a mis clientes clases por videollamada para que asi podamos entrenar juntos y yo revisar las tecnicas, velocidad del movimiento, respiracion y postura correcta del cuerpo. Enviame un email y asi puedo darte mas informacion sobre las clases.Vamos a entrenar con toda la energia!! Hey! I hope your day is going amazing! It's great that you've decided to start this program, which I've built based on your goals. Remember that consistency and discipline will be essential to see results. A good diet will also be an important part of ensuring your gym workouts show results in your body. Remember to get plenty of rest and stay hydrated. All of this is part of a balanced mind, body, and spirit. Remember that I also offer video call classes, I give these classes to people all around the world thought the phone so I can review technique, speed of movement, breathing, and proper body posture. Send me an email so I can give you more information about the classes. Let's train with all our energy!! David Torres WELLNESS COACH"
    with app.open_resource("GluteosMes1(ingles).pdf") as adj:
        msg.attach("GluteosMes1(ingles).pdf", "application/pdf", adj.read())
    with app.open_resource("GluteosMes1(español).pdf") as adj:
        msg.attach("GluteosMes1(español).pdf", "application/pdf", adj.read())             
    mail.send(msg)

    return render_template('success.html')    


@app.route('/successCuerpoCompletoPrimerMes')
def successCuerpoCompletoPrimerMes():
    email = request.args.get('email')

    msg = Message('Gracias por tu compra', sender='tu_correo@gmail.com', recipients=[email])
    msg.body = "Hola! Espero tu dia vaya increible ! Excelente que hayas tomado la decision de empezar con este programa que he construido en base a tus objetivos. Recueda que la constancia y disciplina seran indispensables para lograr ver resultados. Una buena alimentacion sera tambien parte importante para que el entrenamiento en el gimnacio muestre los resultados en tu cuerpo. Recuerda descansar bien y mantenerte siempre hidratando tu cuerpo. Todo esto hace parte de una mente, cuerpo y espiritu en balance. Recuerda que tambien ofrezco a mis clientes clases por videollamada para que asi podamos entrenar juntos y yo revisar las tecnicas, velocidad del movimiento, respiracion y postura correcta del cuerpo. Enviame un email y asi puedo darte mas informacion sobre las clases.Vamos a entrenar con toda la energia!! Hey! I hope your day is going amazing! It's great that you've decided to start this program, which I've built based on your goals. Remember that consistency and discipline will be essential to see results. A good diet will also be an important part of ensuring your gym workouts show results in your body. Remember to get plenty of rest and stay hydrated. All of this is part of a balanced mind, body, and spirit. Remember that I also offer video call classes, I give these classes to people all around the world thought the phone so I can review technique, speed of movement, breathing, and proper body posture. Send me an email so I can give you more information about the classes. Let's train with all our energy!! David Torres WELLNESS COACH"
    with app.open_resource("Cuerpocompletomes1(español).pdf") as adj:
        msg.attach("Cuerpocompletomes1(español).pdf", "application/pdf", adj.read())
    with app.open_resource("Cuerpocompletomes1(ingles).pdf") as adj:
        msg.attach("Cuerpocompletomes1(ingles).pdf", "application/pdf", adj.read())             
    mail.send(msg)

    return render_template('success.html')    

@app.route('/successCuerpoCompleto2Mes')
def successCuerpoCompleto2Mes():
    email = request.args.get('email')

    msg = Message('Gracias por tu compra', sender='tu_correo@gmail.com', recipients=[email])
    msg.body = "Hola! Espero tu dia vaya increible ! Excelente que hayas tomado la decision de empezar con este programa que he construido en base a tus objetivos. Recueda que la constancia y disciplina seran indispensables para lograr ver resultados. Una buena alimentacion sera tambien parte importante para que el entrenamiento en el gimnacio muestre los resultados en tu cuerpo. Recuerda descansar bien y mantenerte siempre hidratando tu cuerpo. Todo esto hace parte de una mente, cuerpo y espiritu en balance. Recuerda que tambien ofrezco a mis clientes clases por videollamada para que asi podamos entrenar juntos y yo revisar las tecnicas, velocidad del movimiento, respiracion y postura correcta del cuerpo. Enviame un email y asi puedo darte mas informacion sobre las clases.Vamos a entrenar con toda la energia!! Hey! I hope your day is going amazing! It's great that you've decided to start this program, which I've built based on your goals. Remember that consistency and discipline will be essential to see results. A good diet will also be an important part of ensuring your gym workouts show results in your body. Remember to get plenty of rest and stay hydrated. All of this is part of a balanced mind, body, and spirit. Remember that I also offer video call classes, I give these classes to people all around the world thought the phone so I can review technique, speed of movement, breathing, and proper body posture. Send me an email so I can give you more information about the classes. Let's train with all our energy!! David Torres WELLNESS COACH"
    with app.open_resource("Cuerpocompletomes2(español).pdf") as adj:
        msg.attach("Cuerpocompletomes2(español).pdf", "application/pdf", adj.read())
    with app.open_resource("Cuerpocompletomes2(ingles).pdf") as adj:
        msg.attach("Cuerpocompletomes2(ingles).pdf", "application/pdf", adj.read())             
    mail.send(msg)

    return render_template('success.html')  

@app.route('/successPrograma90dias')
def successPrograma90dias():
    email = request.args.get('email')

    msg = Message('Gracias por tu compra', sender='tu_correo@gmail.com', recipients=[email])
    msg.body = "Hola! Espero tu dia vaya increible ! Excelente que hayas tomado la decision de empezar con este programa que he construido en base a tus objetivos. Recueda que la constancia y disciplina seran indispensables para lograr ver resultados. Una buena alimentacion sera tambien parte importante para que el entrenamiento en el gimnacio muestre los resultados en tu cuerpo. Recuerda descansar bien y mantenerte siempre hidratando tu cuerpo. Todo esto hace parte de una mente, cuerpo y espiritu en balance. Recuerda que tambien ofrezco a mis clientes clases por videollamada para que asi podamos entrenar juntos y yo revisar las tecnicas, velocidad del movimiento, respiracion y postura correcta del cuerpo. Enviame un email y asi puedo darte mas informacion sobre las clases.Vamos a entrenar con toda la energia!! Hey! I hope your day is going amazing! It's great that you've decided to start this program, which I've built based on your goals. Remember that consistency and discipline will be essential to see results. A good diet will also be an important part of ensuring your gym workouts show results in your body. Remember to get plenty of rest and stay hydrated. All of this is part of a balanced mind, body, and spirit. Remember that I also offer video call classes, I give these classes to people all around the world thought the phone so I can review technique, speed of movement, breathing, and proper body posture. Send me an email so I can give you more information about the classes. Let's train with all our energy!! David Torres WELLNESS COACH"
    with app.open_resource("Cuerpocompleto3meses(español).pdf") as adj:
        msg.attach("Cuerpocompleto3meses(español).pdf", "application/pdf", adj.read())
        
    mail.send(msg)

    return render_template('success.html')         
@app.route('/successPrograma1hr')
def successPrograma1hr():
    email = request.args.get('email')

    msg = Message('Gracias por tu compra', sender='tu_correo@gmail.com', recipients=[email])
    msg.body = "Hola! Espero tu dia vaya increible ! Excelente que hayas tomado la decision de empezar con este programa que he construido en base a tus objetivos. Recueda que la constancia y disciplina seran indispensables para lograr ver resultados. Una buena alimentacion sera tambien parte importante para que el entrenamiento en el gimnacio muestre los resultados en tu cuerpo. Recuerda descansar bien y mantenerte siempre hidratando tu cuerpo. Todo esto hace parte de una mente, cuerpo y espiritu en balance. Recuerda que tambien ofrezco a mis clientes clases por videollamada para que asi podamos entrenar juntos y yo revisar las tecnicas, velocidad del movimiento, respiracion y postura correcta del cuerpo. Enviame un email y asi puedo darte mas informacion sobre las clases.Vamos a entrenar con toda la energia!! Hey! I hope your day is going amazing! It's great that you've decided to start this program, which I've built based on your goals. Remember that consistency and discipline will be essential to see results. A good diet will also be an important part of ensuring your gym workouts show results in your body. Remember to get plenty of rest and stay hydrated. All of this is part of a balanced mind, body, and spirit. Remember that I also offer video call classes, I give these classes to people all around the world thought the phone so I can review technique, speed of movement, breathing, and proper body posture. Send me an email so I can give you more information about the classes. Let's train with all our energy!! David Torres WELLNESS COACH"
    with app.open_resource("Presentacion.pdf") as adj:
        msg.attach("Presentacion.pdf", "application/pdf", adj.read())   
    mail.send(msg)

    return render_template('success.html')
           


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
