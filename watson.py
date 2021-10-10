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
            'Lucas' : {'cantidad consultas' : 0, 'ultima consulta' : None, 'cantidad consulta problema' : 0, 'cantidad consulta causas' : 0, 'cantidad consulta impacto social' : 0, 'cantidad consulta impacto salud' : 0, 'cantidad consulta impacto demografico' : 0, 'cantidad consulta impacto economico' : 0, 'cantidad consulta solucion' : 0, 'promedio entendimiento' : 0, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0}, 
            'Pablo' : {'cantidad consultas' : 0, 'ultima consulta' : None, 'cantidad consulta problema' : 0, 'cantidad consulta causas' : 0, 'cantidad consulta impacto social' : 0, 'cantidad consulta impacto salud' : 0, 'cantidad consulta impacto demografico' : 0, 'cantidad consulta impacto economico' : 0, 'cantidad consulta solucion' : 0, 'promedio entendimiento' : 0, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0},
            'Luis' : {'cantidad consultas' : 0, 'ultima consulta' : None, 'cantidad consulta problema' : 0, 'cantidad consulta causas' : 0, 'cantidad consulta impacto social' : 0, 'cantidad consulta impacto salud' : 0, 'cantidad consulta impacto demografico' : 0, 'cantidad consulta impacto economico' : 0, 'cantidad consulta solucion' : 0, 'promedio entendimiento' : 0, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0}, 
            'Mateo' : {'cantidad consultas' : 0, 'ultima consulta' : None, 'cantidad consulta problema' : 0, 'cantidad consulta causas' : 0, 'cantidad consulta impacto social' : 0, 'cantidad consulta impacto salud' : 0, 'cantidad consulta impacto demografico' : 0, 'cantidad consulta impacto economico' : 0, 'cantidad consulta solucion' : 0, 'promedio entendimiento' : 0, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0}, 
            'Florencia' : {'cantidad consultas' : 0, 'ultima consulta' : None, 'cantidad consulta problema' : 0, 'cantidad consulta causas' : 0, 'cantidad consulta impacto social' : 0, 'cantidad consulta impacto salud' : 0, 'cantidad consulta impacto demografico' : 0, 'cantidad consulta impacto economico' : 0, 'cantidad consulta solucion' : 0, 'promedio entendimiento' : 0, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0}
          }

materia = {
                'temas_materia' : "Los temas de nuestra clase son: \n | El problema del cambio climático. \n | Las causas del cambio climático. \n | El impacto social del cambio climático. \n | El impacto en la salud humana del cambio climático. \n | El impacto demográfico del cambio climático. \n | El impacto económico del cambio climático. \n | Las soluciones al problema del cambio climático. ", 
                'bibliografia' : "| Fuente: Pardo Buendía, M. (2007). El impacto social del cambio climático. \n | Link: https://e-archivo.uc3m.es/bitstream/handle/10016/10448/impacto_pardo_2007.pdf?sequence=1&isAllowed=y"
          }

CANTIDAD_PREGUNTAS_EXAMEN = 6 

def agregarAlumno(alumnoNuevo) :
    perfilNuevo = {
                    'cantidad consultas' : 0, 
                    'ultima consulta' : None,
                    'cantidad consulta problema' : 0,
                    'cantidad consulta causas' : 0,
                    'cantidad consulta impacto social' : 0,
                    'cantidad consulta impacto salud' : 0, 
                    'cantidad consulta impacto demografico' : 0, 
                    'cantidad consulta impacto economico' : 0,
                    'cantidad consulta solucion' : 0,
                    'promedio entendimiento' : 0, 
                    'examenes intentados' : 0, 
                    'examenes aprobados' : 0, 
                    'promedio errores examen' : 0, 
                    'cantidad entradas chat' : 0
                  }
    alumnos[alumnoNuevo] = perfilNuevo

preguntasExamen = {
                    'pregunta1' : {'alternativa0' : "pregunta1 alternativa0", 'alternativa1' : "pregunta1 alternativa1", 'alternativa2' : "pregunta1 alternativa2"}, 
                    'pregunta2' : {'alternativa0' : "pregunta2 alternativa0", 'alternativa1' : "pregunta2 alternativa1", 'alternativa2' : "pregunta2 alternativa2"}, 
                    'pregunta3' : {'alternativa0' : "pregunta3 alternativa0", 'alternativa1' : "pregunta3 alternativa1", 'alternativa2' : "pregunta3 alternativa2"}, 
                    'pregunta4' : {'alternativa0' : "pregunta4 alternativa0", 'alternativa1' : "pregunta4 alternativa1", 'alternativa2' : "pregunta4 alternativa2"}, 
                    'pregunta5' : {'alternativa0' : "pregunta5 alternativa0", 'alternativa1' : "pregunta5 alternativa1", 'alternativa2' : "pregunta5 alternativa2"}, 
                    'pregunta6' : {'alternativa0' : "pregunta6 alternativa0", 'alternativa1' : "pregunta6 alternativa1", 'alternativa2' : "pregunta6 alternativa1"}
                  }
opcionesExamen = {
                    'pregunta1' : {
                                    'alternativa0' : {'opcionA' : "pregunta1 alternativa0 opcionA", 'opcionB' : "pregunta1 alternativa0 opcionB", 'opcionC' : "pregunta1 alternativa0 opcionC"}, 
                                    'alternativa1' : {'opcionA' : "pregunta1 alternativa1 opcionA", 'opcionB' : "pregunta1 alternativa1 opcionB", 'opcionC' : "pregunta1 alternativa1 opcionC"}, 
                                    'alternativa2' : {'opcionA' : "pregunta1 alternativa2 opcionA", 'opcionB' : "pregunta1 alternativa2 opcionB", 'opcionC' : "pregunta1 alternativa2 opcionC"}
                                  }, 
                    'pregunta2' : {
                                    'alternativa0' : {'opcionA' : "pregunta2 alternativa0 opcionA", 'opcionB' : "pregunta2 alternativa0 opcionB", 'opcionC' : "pregunta2 alternativa0 opcionC"}, 
                                    'alternativa1' : {'opcionA' : "pregunta2 alternativa1 opcionA", 'opcionB' : "pregunta2 alternativa1 opcionB", 'opcionC' : "pregunta2 alternativa1 opcionC"}, 
                                    'alternativa2' : {'opcionA' : "pregunta2 alternativa2 opcionA", 'opcionB' : "pregunta2 alternativa2 opcionB", 'opcionC' : "pregunta2 alternativa2 opcionC"}
                                  }, 
                    'pregunta3' : {
                                    'alternativa0' : {'opcionA' : "pregunta3 alternativa0 opcionA", 'opcionB' : "pregunta3 alternativa0 opcionB", 'opcionC' : "pregunta3 alternativa0 opcionC"}, 
                                    'alternativa1' : {'opcionA' : "pregunta3 alternativa1 opcionA", 'opcionB' : "pregunta3 alternativa1 opcionB", 'opcionC' : "pregunta3 alternativa1 opcionC"}, 
                                    'alternativa2' : {'opcionA' : "pregunta3 alternativa2 opcionA", 'opcionB' : "pregunta3 alternativa2 opcionB", 'opcionC' : "pregunta3 alternativa2 opcionC"}
                                  }, 
                    'pregunta4' : {
                                    'alternativa0' : {'opcionA' : "pregunta4 alternativa0 opcionA", 'opcionB' : "pregunta4 alternativa0 opcionB", 'opcionC' : "pregunta4 alternativa0 opcionC"}, 
                                    'alternativa1' : {'opcionA' : "pregunta4 alternativa1 opcionA", 'opcionB' : "pregunta4 alternativa1 opcionB", 'opcionC' : "pregunta4 alternativa1 opcionC"}, 
                                    'alternativa2' : {'opcionA' : "pregunta4 alternativa2 opcionA", 'opcionB' : "pregunta4 alternativa2 opcionB", 'opcionC' : "pregunta4 alternativa2 opcionC"}
                                  }, 
                    'pregunta5' : {
                                    'alternativa0' : {'opcionA' : "pregunta5 alternativa0 opcionA", 'opcionB' : "pregunta5 alternativa0 opcionB", 'opcionC' : "pregunta5 alternativa0 opcionC"}, 
                                    'alternativa1' : {'opcionA' : "pregunta5 alternativa1 opcionA", 'opcionB' : "pregunta5 alternativa1 opcionB", 'opcionC' : "pregunta5 alternativa1 opcionC"}, 
                                    'alternativa2' : {'opcionA' : "pregunta5 alternativa2 opcionA", 'opcionB' : "pregunta5 alternativa2 opcionB", 'opcionC' : "pregunta5 alternativa2 opcionC"}
                                  }, 
                    'pregunta6' : {
                                    'alternativa0' : {'opcionA' : "pregunta6 alternativa0 opcionA", 'opcionB' : "pregunta6 alternativa0 opcionB", 'opcionC' : "pregunta6 alternativa0 opcionC"}, 
                                    'alternativa1' : {'opcionA' : "pregunta6 alternativa1 opcionA", 'opcionB' : "pregunta6 alternativa1 opcionB", 'opcionC' : "pregunta6 alternativa1 opcionC"}, 
                                    'alternativa2' : {'opcionA' : "pregunta6 alternativa2 opcionA", 'opcionB' : "pregunta6 alternativa2 opcionB", 'opcionC' : "pregunta6 alternativa2 opcionC"}
                                  }
                 }
respuestasExamen = {
                        'pregunta1' : {
                                        'alternativa0' : "pregunta1 alternativa0 opcionA", 
                                        'alternativa1' : "pregunta1 alternativa1 opcionA", 
                                        'alternativa2' : "pregunta1 alternativa2 opcionA"
                                      }, 
                        'pregunta2' : {
                                        'alternativa0' : "pregunta2 alternativa0 opcionA", 
                                        'alternativa1' : "pregunta2 alternativa1 opcionA", 
                                        'alternativa2' : "pregunta2 alternativa2 opcionA"
                                      }, 
                        'pregunta3' : {
                                        'alternativa0' : "pregunta3 alternativa0 opcionA", 
                                        'alternativa1' : "pregunta3 alternativa1 opcionA", 
                                        'alternativa2' : "pregunta3 alternativa2 opcionA"         
                                      }, 
                        'pregunta4' : {
                                        'alternativa0' : "pregunta4 alternativa0 opcionA", 
                                        'alternativa1' : "pregunta4 alternativa1 opcionA", 
                                        'alternativa2' : "pregunta4 alternativa2 opcionA"
                                      }, 
                        'pregunta5' : {
                                        'alternativa0' : "pregunta5 alternativa0 opcionA", 
                                        'alternativa1' : "pregunta5 alternativa1 opcionA", 
                                        'alternativa2' : "pregunta5 alternativa2 opcionA"
                                      }, 
                        'pregunta6' : {
                                        'alternativa0' : "pregunta6 alternativa0 opcionA", 
                                        'alternativa1' : "pregunta6 alternativa1 opcionA", 
                                        'alternativa2' : "pregunta6 alternativa2 opcionA"
                                      }
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
                'pregunta2' : {'pregunta' : preguntasExamen['pregunta2'][p2], 'opciones' : opcionesExamen['pregunta2'][p2], 'respuesta' : respuestasExamen['pregunta2'][p2]}, 
                'pregunta3' : {'pregunta' : preguntasExamen['pregunta3'][p3], 'opciones' : opcionesExamen['pregunta3'][p3], 'respuesta' : respuestasExamen['pregunta3'][p3]}, 
                'pregunta4' : {'pregunta' : preguntasExamen['pregunta4'][p4], 'opciones' : opcionesExamen['pregunta4'][p4], 'respuesta' : respuestasExamen['pregunta4'][p4]}, 
                'pregunta5' : {'pregunta' : preguntasExamen['pregunta5'][p5], 'opciones' : opcionesExamen['pregunta5'][p5], 'respuesta' : respuestasExamen['pregunta5'][p5]}, 
                'pregunta6' : {'pregunta' : preguntasExamen['pregunta6'][p6], 'opciones' : opcionesExamen['pregunta6'][p6], 'respuesta' : respuestasExamen['pregunta6'][p6]}, 
           }

def buenConcepto(alum):
    if alumnos[alum]['cantidad consultas'] >= 10 and alumnos[alum]['cantidad entradas chat'] >= 10:
     return True
    else: 
     return False

def corregirRespuestas(respuestas, examen):
    correccionResp = dict()
    correccionResp['cont'] = 0
    for i in range(len(respuestas)):
        j = i + 1
        llavePregunta = "pregunta" + repr(j)
        if respuestas[i] == examen[llavePregunta]['respuesta']:
            correccionResp['cont'] += 1
            correccionResp[llavePregunta] = "Respuesta " + repr(j) + ": CORRECTA."
        else:
            correccionResp[llavePregunta] = "Respuesta " + repr(j) + ": INCORRECTA."
    return correccionResp
    
def corregirEvaluacion(alum, examen, rta1, rta2, rta3, rta4, rta5, rta6):
    correccion = corregirRespuestas([rta1, rta2, rta3, rta4, rta5, rta6], examen)
    if correccion['cont'] < CANTIDAD_PREGUNTAS_EXAMEN-2:
       correccion['devolucion'] = "No te desanimes " + alum + ", a seguir estudiando."
    else:
       if correccion['cont'] == CANTIDAD_PREGUNTAS_EXAMEN-2 and buenConcepto(alum):
             alumnos[alum]['examenes aprobados'] += 1
             correccion['devolucion'] = "¡Felicitaciones " + alum + "! ¡Aprobaste la evaluacion!" + " Pero ojo pero un punto fue de concepto, por tu participacion, ¡a estudiar un poco mas!"
       else:
            if correccion['cont'] == CANTIDAD_PREGUNTAS_EXAMEN-2 and buenConcepto(alum) == False:
              correccion['devolucion'] = "No te desanimes " + alum + ", a seguir estudiando."
            else:
                if correccion['cont'] >= CANTIDAD_PREGUNTAS_EXAMEN-1: 
                   alumnos[alum]['examenes aprobados'] += 1
                   correccion['devolucion'] = "¡Felicitaciones " + alum + "! ¡Aprobaste la evaluacion!"              
    # este es el que se probo y anduvo
    #    alumnos[alum]['Examenes aprobados'] += 1      
   # if correccion['cont'] == CANTIDAD_PREGUNTAS_EXAMEN:
    #    correccion['devolucion'] = "¡Felicitaciones " + alum + "! ¡Aprobaste la evaluacion!"
    #    alumnos[alum]['examenes aprobados'] += 1
    #else:
    #    correccion['devolucion'] = "No te desanimes " + alum + ", a seguir estudiando."
    alumnos[alum]['promedio errores examen'] += ((CANTIDAD_PREGUNTAS_EXAMEN - correccion['cont']) / (alumnos[alum]['examenes intentados'] + (alumnos[alum]['examenes intentados'] - 1)))
    return correccion

def main(dict):
    if dict['identificarse'] == 1:
        if not dict['nombre'] in alumnos.keys():
            agregarAlumno(dict['nombre'])
        alumnos[dict['nombre']]['cantidad entradas chat'] += 1
        saludo = {'message' : "¡Un gusto " +  dict['nombre'] + "!"}
        return saludo
        
    if dict['temas'] == 1:
        temas = {'message' : materia['temas_materia']}
        return temas
    
    if dict['ultima consulta'] == 1:
        salida = {'message' : dict['nombre'] + "la ultima vez consultaste sobre " +  alumnos[dict['nombre']][dict['ultima consulta']] + "¿querés hacer una evaluacion sobre ese tema en forma de respaso?"}
        return salida  
        
    if dict['consulta'] == 1:
        alumnos[dict['nombre']]['cantidad consultas'] += 1
        return dict()
        
    if dict['tipo consulta'] != -1:
        llaveConsulta = "cantidad " + dict['tipo consulta']
        alumnos[dict['nombre']][llaveConsulta] += 1
        alumnos[dict['nombre']]['ultima consulta'] = dict['tipo consulta']
        
    if dict['bibliografia'] == 1:
        bibliografia = {'message' : materia['bibliografia']}
        return bibliografia
        
    if dict['evaluacion'] == 0:
        alumnos[dict['nombre']]['examenes intentados'] += 1
        examen = generarEvaluacion()
        dict['examen'] = examen
        return examen
        
    if dict['evaluacion'] > 0 and dict['evaluacion'] < 7:
        llave = "pregunta" + repr(dict['evaluacion'])
        pta = dict['examen'][llave]
        return pta
        
    if dict['evaluacion'] == 7:
        correccion = corregirEvaluacion(dict['nombre'], dict['examen'], dict['rta1'], dict['rta2'], dict['rta3'], dict['rta4'], dict['rta5'], dict['rta6'])
        devolucion = {'message' : correccion['pregunta1'] + "\n" + correccion['pregunta2'] + "\n" + correccion['pregunta3'] + "\n" + correccion['pregunta4'] + "\n" + correccion['pregunta5'] + "\n" + correccion['pregunta6'] + "\n" + correccion['devolucion']}
        return devolucion