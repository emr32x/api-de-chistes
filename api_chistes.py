from flask import Flask, jsonify
import random

app = Flask(__name__)
# --- ¡AQUÍ ESTÁ LA SOLUCIÓN! ---
app.config['JSON_AS_ASCII'] = False
# -------------------------------

chistes_sanos = [
    {"id": 1, "chiste": "¿Qué le dice un pez a otro? ¡Nada!"},
    {"id": 2, "chiste": "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter."},
    {"id": 3, "chiste": "Fui a comprar camuflaje el otro día, pero no pude encontrar nada."},
    {"id": 4, "chiste": "¿Sabes por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas."},
    {"id": 5, "chiste": "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!"},
    {"id": 6, "chiste": "Le dije a mi esposa que dibujara sus cejas más arriba. Parecía sorprendida."},
    {"id": 7, "chiste": "¿Cuál es el último animal en subir al arca de Noé? El del-fín."},
    {"id": 8, "chiste": "¿Qué le dice un techo a otro? Techo de menos."},
    {"id": 9, "chiste": "Me robaron todas las sillas de mi casa. No saben cómo me siento."},
    {"id": 10, "chiste": "¿Por qué el semáforo se puso rojo? ¡Porque le dio vergüenza cambiarse delante de todos!"},
    {"id": 11, "chiste": "¿Qué es un punto verde en la esquina de una casa? Un guisante castigado."},
    {"id": 12, "chiste": "Un hombre entra a un bar de pinchos y dice: Ay, ay, ay."},
    {"id": 13, "chiste": "¿Cómo estornuda un tomate? ¡Keeeétchup!"},
    {"id": 14, "chiste": "¿Por qué las focas del circo miran siempre hacia arriba? Porque allí están los focos."},
    {"id": 15, "chiste": "Papá, ¿qué se siente tener un hijo tan guapo? No sé, hijo, pregúntale a tu abuelo."},
    {"id": 16, "chiste": "¿Por qué los dálmatas no pueden jugar al escondite? Porque siempre los ven."},
    {"id": 17, "chiste": "El futuro, el presente y el pasado entraron a un bar. La situación se puso un poco tensa."},
    {"id": 18, "chiste": "¿Qué le dice un espagueti a otro? ¡Oye, mi cuerpo pide salsa!"},
    {"id": 19, "chiste": "¿Por qué el esqueleto no cruzó la calle? Porque no tenía agallas."},
    {"id": 20, "chiste": "Me compré un cinturón de asteroides, ¡qué galaxia de pantalón!"},
    {"id": 21, "chiste": "¿Cómo llamas a un oso que cuenta chistes? Un oso comediante."},
    {"id": 22, "chiste": "Si los zombies se descomponen, ¿es un apocalipsis zombie o un apocalipsis de abono?"},
    {"id": 23, "chiste": "¿Qué hace una vaca pensando? Hace leche concentrada."},
    {"id": 24, "chiste": "¿Por qué el mar no se seca? Porque no tiene toalla."},
    {"id": 25, "chiste": "Si se te cae un tenedor, viene un hombre. Si se te cae una cuchara, una mujer. Si se me cae el sueldo, ¿viene el gobierno?"},
    {"id": 26, "chiste": "¿Qué le dice un 3 a un 30? Para ser como yo, tienes que ser sincero."},
    {"id": 27, "chiste": "Me caí y pensé: ¿Llamo a una ambulancia? Mejor me río un rato."},
    {"id": 28, "chiste": "¿Por qué no se puede confiar en los átomos? Porque lo componen todo."},
    {"id": 29, "chiste": "Mi memoria es tan mala que olvidé que tenía mala memoria."},
    {"id": 30, "chiste": "¿Cómo llamas a un queso que no es tuyo? Nacho cheese."},
    {"id": 31, "chiste": "¿Qué le dice un semáforo a un coche? ¡No me mires que me estoy cambiando!"},
    {"id": 32, "chiste": "¿Por qué los buzos se tiran de espaldas al agua? Porque si se tiran para adelante, caen en el barco."},
    {"id": 33, "chiste": "He inventado un nuevo sabor de helado, pero no sé de qué está hecho. Es un sabor de incógnito."},
    {"id": 34, "chiste": "¿Por qué los flamencos levantan una pata? Porque si levantaran las dos, se caerían."},
    {"id": 35, "chiste": "¿Qué le dice un jaguar a otro? Jaguar you?"},
    {"id": 36, "chiste": "¿Cómo se despiden los químicos? Ácido un placer."},
    {"id": 37, "chiste": "¿Por qué lloraba la escoba? Porque la dejaron barrida."},
    {"id": 38, "chiste": "Si un abogado enloquece, ¿pierde el juicio?"},
    {"id": 39, "chiste": "Un pez le pregunta a su amigo: ¿Tu papá qué hace? Y el otro le responde: Nada."},
    {"id": 40, "chiste": "Quería contar un chiste sobre el tiempo, pero es muy largo."},
    {"id": 41, "chiste": "¿Qué le dice un semáforo a otro? ¡No me mires, que me estoy cambiando!"},
    {"id": 42, "chiste": "¿Cómo organizas una fiesta en el espacio? La planeas."},
    {"id": 43, "chiste": "¿Qué bebe el hombre invisible? Leche evaporada."},
    {"id": 44, "chiste": "Ayer llamé a la policía porque vi a dos hombres robando en mi jardín. Me dijeron que eran mis vecinos."},
    {"id": 45, "chiste": "¿Qué hace una impresora en el desierto? ¡Impresionante!"},
    {"id": 46, "chiste": "¿Por qué el espantapájaros ganó un premio? Porque era sobresaliente en su campo."},
    {"id": 47, "chiste": "¿Qué le dice un pato a otro pato? ¡Estamos empatados!"},
    {"id": 48, "chiste": "Tengo un amigo que es tan vago, que cuando le da un ataque de risa, se apoya en la pared."},
    {"id": 49, "chiste": "¿Cómo se llama el campeón de buceo japonés? Tokofondo."},
    {"id": 50, "chiste": "Le pregunté a un bibliotecario si tenían libros sobre la paranoia. Me susurró: 'Están justo detrás de ti'."},
    {"id": 51, "chiste": "Un ciego entra en una cocina y dice: '¡Hola a todas!'" },
    {"id": 52, "chiste": "¿Por qué los ordenadores tienen frío? Porque tienen Windows abiertos."},
    {"id": 53, "chiste": "¿Cuál es la fruta más divertida? ¡La naranja ja-ja-ja!"},
    {"id": 54, "chiste": "¿Cómo se dice pañuelo en japonés? Sakamoko."},
    {"id": 55, "chiste": "¿Qué le dice un gusano a otro? Voy a dar una vuelta a la manzana."},
    {"id": 56, "chiste": "Mi perro solía perseguir a la gente en bicicleta. Se puso tan mal que tuve que quitarle la bicicleta."},
    {"id": 57, "chiste": "¿Por qué las bicicletas no pueden mantenerse de pie por sí solas? Porque están dos-cansadas (two-tired)."},
    {"id": 58, "chiste": "No es que sea perezoso, es que estoy en modo ahorro de energía."},
    {"id": 59, "chiste": "¿Qué le dice una pared a otra? Nos vemos en la esquina."},
    {"id": 60, "chiste": "¿Por qué el océano es tan salado? Porque los peces no saben usar el pimentero."},
    {"id": 61, "chiste": "¿Qué es amarillo y dispara? Un plátano-metralleta."},
    {"id": 62, "chiste": "¿Cómo llamas a un boomerang que no vuelve? Un palo."},
    {"id": 63, "chiste": "Me encanta la miel, es un negocio que va sobre abejas."},
    {"id": 64, "chiste": "¿Cuál es el café más peligroso del mundo? El ex-preso."},
    {"id": 65, "chiste": "¿Qué le dice un jardinero a otro? Nos vemos cuando podamos."},
    {"id": 66, "chiste": "Me compré un coche por un dólar y venía con dos ruedas de repuesto. ¡Qué ofertón de cuatro ruedas!"},
    {"id": 67, "chiste": "La pereza es la madre de todos los vicios, y como a la madre hay que respetarla..."}
]

@app.route('/api/chiste', methods=['GET'])
def obtener_chiste_aleatorio():
    chiste_aleatorio = random.choice(chistes_sanos)
    return jsonify(chiste_aleatorio)

@app.route('/api/chiste/<int:chiste_id>', methods=['GET'])
def obtener_chiste_por_id(chiste_id):
    chiste_encontrado = next((chiste for chiste in chistes_sanos if chiste["id"] == chiste_id), None)
    if chiste_encontrado:
        return jsonify(chiste_encontrado)
    else:
        return jsonify({"error": "Chiste no encontrado"}), 404

@app.route('/')
def index():
    return "¡Bienvenido a la API de Chistes! Usa /api/chiste para obtener uno."

if __name__ == '__main__':
    app.run(debug=True)