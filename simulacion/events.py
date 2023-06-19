import random

fightEventsList = [
    "Te encuentras con un grupo de bandidos que intenta robarte. ¡Prepárate para la pelea!",
    "Un monstruo salvaje aparece de repente y te desafía a un combate.",
    "Un enemigo poderoso te acecha desde las sombras. ¡Debes luchar por tu vida!",
    "Un grupo de soldados hostiles te desafía a un duelo. ¡Defiéndete!",
    "Un mago oscuro aparece y lanza un hechizo contra ti. ¡Es hora de la batalla mágica!",
    "Una criatura gigante emerge del agua y te ataca. ¡No tienes más opción que luchar!",
    "Un ejército de no-muertos se levanta de sus tumbas y te ataca. ¡Prepárate para una batalla épica!",
    "Un gremio de ladrones te considera una amenaza y te desafía a una pelea.",
    "Un grupo de cazadores te confunde con una bestia y te ataca. ¡Debes defenderte!",
    "Un antiguo golem de piedra cobra vida y te ataca. ¡Es hora de demostrar tu valentía!",
    "Una manada de lobos hambrientos se abalanza sobre ti. ¡Prepárate para la lucha por tu vida!",
    "Un guerrero legendario busca un oponente digno. ¡Demuéstrale tu habilidad en el combate!",
    "Un hechicero rival desea probar su poder contra el tuyo. ¡Es hora de mostrar quién es el más fuerte!",
    "Un grupo de bárbaros te reta a una batalla cuerpo a cuerpo. ¡Defiéndete con todas tus fuerzas!",
    "Un dragón furioso aparece en el horizonte y exige un enfrentamiento. ¡Prepárate para la batalla definitiva!",
]

mazeEventsList = [
    "Encuentras una puerta cerrada. Para abrirla, debes resolver un complicado acertijo.",
    "Te encuentras con un puente roto. Debes buscar una manera de cruzarlo sin caer al abismo.",
    "Descubres una habitación llena de trampas mortales. Debes sortearlas con cuidado.",
    "Te topas con un guardián poderoso que protege el tesoro de la mazmorra. ¡Prepárate para la batalla!",
    "Encuentras un pasaje secreto que conduce a una sala oculta con tesoros antiguos.",
    "Te pierdes en los laberintos de la mazmorra y debes encontrar la salida.",
    "Descubres un antiguo altar y un misterioso ritual. Puedes intentar completarlo para obtener una recompensa.",
    "Una maldición antigua se activa cuando entras a una sala, debes encontrar la manera de romperla.",
    "Te encuentras con un grupo de esqueletos animados que defienden la mazmorra. ¡Prepárate para la pelea!",
    "Una estatua te habla y te da una enigmática pista para avanzar en la mazmorra.",
    "Te enfrentas a una serie de enigmas y rompecabezas que debes resolver para avanzar.",
    "Encuentras una sala llena de espejos y reflejos engañosos. Debes encontrar el camino correcto.",
    "Te encuentras con un pasadizo secreto que te lleva a una cámara de tesoros escondidos.",
    "Una extraña niebla te envuelve y debes encontrar la salida antes de que sea demasiado tarde.",
    "Descubres un libro antiguo que contiene información vital para resolver los misterios de la mazmorra.",

]

castleEventsList = [
    "Encuentras una habitación secreta con un tesoro escondido.",
    "Un guardia te reta a un duelo de espadas para probar tu valía.",
    "Te encuentras con un fantasma atormentado que busca ayuda para resolver su tragedia.",
    "Descubres un mapa antiguo que revela la ubicación de una sala secreta.",
    "Un intrépido ladrón intenta robar tus pertenencias. ¡Prepárate para defender tus posesiones!",
    "Te topas con una sala llena de espejos que distorsionan la realidad. Debes encontrar el camino correcto.",
    "Encuentras una biblioteca ancestral con libros llenos de sabiduría y conocimientos ocultos.",
    "Un grupo de caballeros te desafía a una competencia de habilidades en el patio del castillo.",
    "Te encuentras con un prisionero injustamente encerrado. Ayúdalo a escapar o enfrenta las consecuencias.",
    "Descubres una habitación encantada que requiere resolver un enigma para liberar su antiguo secreto.",
    "Un poderoso hechicero te reta a superar sus pruebas mágicas para demostrar tu valía.",
    "Te enfrentas a una criatura mítica guardiana del castillo. ¡La batalla será feroz!",
    "Encuentras una sala de banquetes con una mesa llena de manjares y festines. ¿Será una trampa?",
    "Un grupo de conspiradores se reúne en una sala oculta. Escucha sus conversaciones y descubre sus planes.",
    "Descubres un jardín encantado lleno de plantas y flores mágicas. ¡Ten cuidado con sus poderes!",
]

swampEventsList = [
    "Te encuentras con un enjambre de insectos venenosos. ¡Prepárate para una lucha desesperada!",
    "Una densa niebla se desplaza sobre el pantano, dificultando la visibilidad y la orientación.",
    "Descubres un charco de lodo profundo. Debes encontrar una forma de cruzarlo sin quedarte atrapado.",
    "Te topas con una criatura reptiliana gigante que protege su territorio. ¡La batalla será intensa!",
    "Encuentras un antiguo artefacto maldito. Decidir si lo tomas o no puede tener graves consecuencias.",
    "Una tormenta eléctrica se desata sobre el pantano, aumentando la peligrosidad del entorno.",
    "Te encuentras con una tribu de seres místicos que pueden ayudarte o lanzarte una peligrosa maldición.",
    "Descubres un esqueleto medio enterrado en el pantano. ¿Es solo un resto olvidado o hay algo más en juego?",
    "Te enfrentas a una maraña de enredaderas y raíces retorcidas que bloquean tu camino. Debes encontrar una solución.",
    "Encuentras un refugio abandonado en medio del pantano. ¿Quién lo habitó antes y qué secretos guarda?",
    "Una criatura acuática acecha bajo la superficie del pantano. ¡Debes estar alerta para evitar ser su presa!",
    "Descubres una isla aparentemente segura en medio del pantano, pero ¿qué peligros oculta?",
    "Te adentras en un banco de niebla espesa que distorsiona la percepción y te confunde en tu camino.",
    "Encuentras una planta exótica con propiedades curativas. ¿Te atreves a recolectarla?",
    "Una figura sombría se desliza entre los árboles del pantano, observándote desde la oscuridad.",

]

forestEventsList = [
    "Te encuentras con una manada de lobos hambrientos. ¡Prepárate para defender tu vida!",
    "Un árbol antiguo y sabio te revela un secreto oculto del bosque.",
    "Descubres una cueva oculta detrás de una cascada. ¿Qué misterios aguardan en su interior?",
    "Te topas con una enredadera mágica que bloquea el camino. Debes encontrar una forma de superarla.",
    "Encuentras una pradera llena de flores exóticas y raras. ¿Tendrán propiedades especiales?",
    "Una densa niebla se extiende por el bosque, desorientando a los viajeros y ocultando peligros.",
    "Te enfrentas a un grupo de cazadores furtivos que amenazan la paz del bosque. ¡Es hora de detenerlos!",
    "Descubres un antiguo altar dedicado a los espíritus del bosque. ¿Te atreves a hacer una ofrenda?",
    "Un enjambre de luciérnagas guía tu camino a través del bosque. ¿Te llevarán a algún lugar especial?",
    "Encuentras una clara en el bosque donde las criaturas se reúnen para celebrar una festividad especial.",
    "Te adentras en un pantano fangoso dentro del bosque. Debes tener cuidado de no quedar atrapado.",
    "Descubres un nido de una criatura gigante en lo alto de un árbol. ¿Qué tesoro habrá allí?",
    "Te encuentras con un grupo de druidas que protegen y preservan el equilibrio del bosque.",
    "Encuentras un río cristalino que atraviesa el bosque. ¿Será seguro beber de sus aguas?",
    "Una extraña figura encapuchada aparece y te ofrece un trato misterioso. ¿Lo aceptarás?",
]

jokeEventsList = [
    "Te pica una mosca",
    "Te caes"
]

def doRandomEvent(eventList):
    eventList = random.choice(eventList)
    return eventList


def forestEvents():
    mainEvent = doRandomEvent(forestEvents)
    print("Evento del bosque:", mainEvent)

def fightEvents():
    mainEvent = doRandomEvent(fightEvents)
    print("Evento de pelea:", mainEvent)

def mazeEvents():
    mainEvent = doRandomEvent(mazeEvents)
    print("Evento del laberinto:", mainEvent)

def castleEvents():
    mainEvent = doRandomEvent(castleEvents)
    print("Evento del castillo:", mainEvent)

def swampEvents():
    mainEvent = doRandomEvent(swampEvents)
    print("Evento del pantano:", mainEvent)

def getRandomListEventsMain():
    random_list = random.choice([fightEventsList, mazeEventsList, castleEventsList, swampEventsList])
    return random_list

def generateEvent():
    eventList = getRandomListEventsMain()
    event = doRandomEvent(eventList)
    print(event)
