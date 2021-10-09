#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
import random

alumnos = { 
            'Lucas' : {'Cantidad de consultas' : 0, 'Promedio de entendimiento' : 0, 'Examenes intentados' : 0, 'Examenes aprobados' : 0, 'Promedio de errores en examen' : 0, 'Cantidad de entradas al chat' : 0}, 
            'Pablo' : {'Cantidad de consultas' : 0, 'Promedio de entendimiento' : 0, 'Examenes intentados' : 0, 'Examenes aprobados' : 0, 'Promedio de errores en examen' : 0, 'Cantidad de entradas al chat' : 0}, 
            'Luis' : {'Cantidad de consultas' : 0, 'Promedio de entendimiento' : 0, 'Examenes intentados' : 0, 'Examenes aprobados' : 0, 'Promedio de errores en examen' : 0, 'Cantidad de entradas al chat' : 0}, 
            'Mateo' : {'Cantidad de consultas' : 0, 'Promedio de entendimiento' : 0, 'Examenes intentados' : 0, 'Examenes aprobados' : 0, 'Promedio de errores en examen' : 0, 'Cantidad de entradas al chat' : 0}, 
            'Florencia' : {'Cantidad de consultas' : 0, 'Promedio de entendimiento' : 0, 'Examenes intentados' : 0, 'Examenes aprobados' : 0, 'Promedio de errores en examen' : 0, 'Cantidad de entradas al chat' : 0]
          }         
#alumnos = dict()

#materia = {
#                'temas_materia' : "Los temas de nuestra clase son: \n | El problema del cambio climático. \n | Las causas del cambio climático. \n | El impacto social del cambio climático. \n | El impacto en la salud humana del cambio climático. \n | El impacto demográfico del cambio climático. \n | El impacto económico del cambio climático. \n | Las soluciones al problema del cambio climático. ", 
#                'bibliografia' : "| Fuente: Pardo Buendía, M. (2007). El impacto social del cambio climático. \n | Link: https://e-archivo.uc3m.es/bitstream/handle/10016/10448/impacto_pardo_2007.pdf?sequence=1&isAllowed=y"
#          }
materia = {'temas_materia' : "asd"}

CANTIDAD_PREGUNTAS_EXAMEN = 6

def agregarAlumno(alumnoNuevo) :
    perfilNuevo = {
                    'Cantidad de consultas' : 0, 
                    'Promedio de entendimiento' : 0, 
                    'Examenes intentados' : 0, 
                    'Examenes aprobados' : 0, 
                    'Promedio de errores en examen' : 0, 
                    'Cantidad de entradas al chat' : 0
                  }
    alumnos[alumnoNuevo] = perfilNuevo

preguntasExamen = {
                    'pregunta1' : {'alternativa0' : "", 'alternativa1' : "", 'alternativa2' : ""}, 
                    'pregunta2' : {'alternativa0' : "", 'alternativa1' : "", 'alternativa2' : ""}, 
                    'pregunta3' : {'alternativa0' : "", 'alternativa1' : "", 'alternativa2' : ""}, 
                    'pregunta4' : {'alternativa0' : "", 'alternativa1' : "", 'alternativa2' : ""}, 
                    'pregunta5' : {'alternativa0' : "", 'alternativa1' : "", 'alternativa2' : ""}, 
                    'pregunta6' : {'alternativa0' : "", 'alternativa1' : "", 'alternativa2' : ""}
                  }
opcionesExamen = {
                    'pregunta1' : {'alternativa0' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}, 'alternativa1' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}, 'alternativa2' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}}, 
                    'pregunta2' : {'alternativa0' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}, 'alternativa1' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}, 'alternativa2' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}}, 
                    'pregunta3' : {'alternativa0' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}, 'alternativa1' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}, 'alternativa2' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}}, 
                    'pregunta4' : {'alternativa0' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}, 'alternativa1' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}, 'alternativa2' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}}, 
                    'pregunta5' : {'alternativa0' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}, 'alternativa1' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}, 'alternativa2' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}}, 
                    'pregunta6' : {'alternativa0' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}, 'alternativa1' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}, 'alternativa2' : {'opcionA' : "a. ", 'opcionB' : "b. ", 'opcionC' : "c. "}}
                 }
respuestasExamen = {
                        'pregunta1' : {'alternativa0' : "opcionA", 'alternativa1' : "opcionA", '2' : "opcionA"}, 
                        'pregunta2' : {'alternativa0' : "opcionA", 'alternativa1' : "opcionA", '2' : "opcionA"}, 
                        'pregunta3' : {'alternativa0' : "opcionA", 'alternativa1' : "opcionA", '2' : "opcionA"}, 
                        'pregunta4' : {'alternativa0' : "opcionA", 'alternativa1' : "opcionA", '2' : "opcionA"}, 
                        'pregunta5' : {'alternativa0' : "opcionA", 'alternativa1' : "opcionA", '2' : "opcionA"}, 
                        'pregunta6' : {'alternativa0' : "opcionA", 'alternativa1' : "opcionA", '2' : "opcionA"}
                   }

def generarEvaluacion():
    p1 = random.choice(list(preguntasExamen['pregunta1'].keys()))
    p2 = random.choice(list(preguntasExamen['pregunta2'].keys()))
    p3 = random.choice(list(preguntasExamen['pregunta3'].keys()))
    p4 = random.choice(list(preguntasExamen['pregunta4'].keys()))
    p5 = random.choice(list(preguntasExamen['pregunta5'].keys()))
    p6 = random.choice(list(preguntasExamen['pregunta6'].keys()))
    return {
                'pregunta1' : {'pregunta' : preguntasExamen['pregunta1'][p1], 'opciones' : opcionesExamen['pregunta1'][p1], 'respuesta' : respuestasExamen['pregunta1'][p1]}, 
                'pregunta2' : {'pregunta' : preguntasExamen['pregunta2'][p2], 'opciones' : opcionesExamen['pregunta2'][p2], 'respuesta' : respuestasExamen['pregunta2'][p2]}}, 
                'pregunta3' : {'pregunta' : preguntasExamen['pregunta3'][p3], 'opciones' : opcionesExamen['pregunta3'][p3], 'respuesta' : respuestasExamen['pregunta3'][p3]}}, 
                'pregunta4' : {'pregunta' : preguntasExamen['pregunta4'][p4], 'opciones' : opcionesExamen['pregunta4'][p4], 'respuesta' : respuestasExamen['pregunta4'][p4]}}, 
                'pregunta5' : {'pregunta' : preguntasExamen['pregunta5'][p5], 'opciones' : opcionesExamen['pregunta5'][p5]}, 'respuesta' : respuestasExamen['pregunta5'][p5]}, 
                'pregunta6' : {'pregunta' : preguntasExamen['pregunta6'][p6], 'opciones' : opcionesExamen['pregunta6'][p6], 'respuesta' : respuestasExamen['pregunta6'][p6]}}, 
           }

def corregirRespuestas(respuestas):
    correccionResp['cont'] = 0
    for i in range(len(respuestas)):
        j = i + 1
        llavePregunta = "pregunta" + j
        if respuestas[i] == examen[llavePregunta]['respuesta']:
            correccionResp['cont'] += 1
            correccionResp[llavePregunta] = "Respuesta " + j + ": CORRECTA."
        else:
            correccionResp[llavePregunta] = "Respuesta " + j + ": INCORRECTA."
    return correccionResp
    
def corregirEvaluacion(alum, examen, rta1, rta2, rta3, rta4, rta5, rta6):
    correccion = corregirRespuestas([rta1, rta2, rta3, rta4, rta5, rta6])
    if correccion['cont'] == CANTIDAD_PREGUNTAS_EXAMEN:
        correccion['devolucion'] = "¡Felicitaciones " + alum + "! ¡Aprobaste la evaluacion!"
        alumnos[alum]['Examenes aprobados'] += 1
    else
        correccion['devolucion'] = "No te desanimes " + alum + ", a seguir estudiando."
    alumnos[alum]['Promedio de errores en examen'] += ((CANTIDAD_PREGUNTAS_EXAMEN - correccion['cont']) / (alumnos[alum]['Examenes intentados'] + ('Examenes intentados' - 1)))
    return correccion

def main(dict):
    if dict['identificarse'] == 1:
        if alumnos[dict['nombre']] is None:
            agregarAlumno(dict['nombre'])
        alumnos[dict['nombre']]['Cantidad de entradas al chat'] += 1
        saludo = {'message' : "¡Un gusto " +  dict['nombre'] + "!"}
        return saludo
        
    if dict['temas'] == 1:
        temas = {'message' : materia['temas_materia']}
        return temas
        
    if dict['consulta'] == 1:
        alumnos[dict['nombre']]['Cantidad de consultas'] += 1
        return dict()
        
    if dict['bibliografia'] == 1:
        bibliografia = {'message' : materia['bibliografia']}
        return bibliografia
        
    if dict['evaluacion'] == 0:
        alumnos[dict['nombre']]['Examenes intentados'] += 1
        examen = generarEvaluacion()
        return examen
        
    if dict['evaluacion'] > 0 and dict['evaluacion'] < 7:
        llave = "pregunta" + dict['evaluacion']
        pta = examen[llave]
        return pta
        
    if dict['evaluacion'] == 7:
        correccion = corregirEvaluacion(dict['nombre'], examen, dict['rta1'], dict['rta2'], dict['rta3'], dict['rta4'], dict['rta5'], dict['rta6'])
        devolucion = {'message' : correccion['pregunta1'] + "\n" + correccion['pregunta2'] + "\n" + correccion['pregunta3'] + "\n" + correccion['pregunta4'] + "\n" + correccion['pregunta5'] + "\n" + correccion['pregunta6'] + "\n" + correccion['devolucion']}
        return devolucion 