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
            'Lucas' : {'cantidadConsultas' : 1, 'ultimaConsulta' : "consulta causas", 'cantidad consulta problema' : 0, 'cantidad consulta causas' : 0, 'cantidad consulta impacto social' : 0, 'cantidad consulta impacto salud' : 0, 'cantidad consulta impacto demografico' : 0, 'cantidad consulta impacto economico' : 0, 'cantidad consulta solucion' : 0, 'promedio entendimiento' : 1, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0}, 
            'Pablo' : {'cantidadConsultas' : 0, 'ultimaConsulta' : None, 'cantidad consulta problema' : 0, 'cantidad consulta causas' : 0, 'cantidad consulta impacto social' : 0, 'cantidad consulta impacto salud' : 0, 'cantidad consulta impacto demografico' : 0, 'cantidad consulta impacto economico' : 0, 'cantidad consulta solucion' : 0, 'promedio entendimiento' : 1, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0},
            'Luis' : {'cantidadConsultas' : 0, 'ultimaConsulta' : None, 'cantidad consulta problema' : 0, 'cantidad consulta causas' : 0, 'cantidad consulta impacto social' : 0, 'cantidad consulta impacto salud' : 0, 'cantidad consulta impacto demografico' : 0, 'cantidad consulta impacto economico' : 0, 'cantidad consulta solucion' : 0, 'promedio entendimiento' : 1, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0}, 
            'Mateo' : {'cantidadConsultas' : 0, 'ultimaConsulta' : None, 'cantidad consulta problema' : 0, 'cantidad consulta causas' : 0, 'cantidad consulta impacto social' : 0, 'cantidad consulta impacto salud' : 0, 'cantidad consulta impacto demografico' : 0, 'cantidad consulta impacto economico' : 0, 'cantidad consulta solucion' : 0, 'promedio entendimiento' : 1, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0}, 
            'Florencia' : {'cantidadConsultas' : 0, 'ultimaConsulta' : None, 'cantidad consulta problema' : 0, 'cantidad consulta causas' : 0, 'cantidad consulta impacto social' : 0, 'cantidad consulta impacto salud' : 0, 'cantidad consulta impacto demografico' : 0, 'cantidad consulta impacto economico' : 0, 'cantidad consulta solucion' : 0, 'promedio entendimiento' : 1, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0},
          }


materia = {
                'temas_materia' : "Los temas de nuestra clase son: \n | El problema del cambio climático. \n | Las causas del cambio climático. \n | El impacto social del cambio climático. \n | El impacto en la salud humana del cambio climático. \n | El impacto demográfico del cambio climático. \n | El impacto económico del cambio climático. \n | Las soluciones al problema del cambio climático. ", 
                'bibliografia' : "| Fuente: Pardo Buendía, M. (2007). El impacto social del cambio climático. \n | Link: https://e-archivo.uc3m.es/bitstream/handle/10016/10448/impacto_pardo_2007.pdf?sequence=1&isAllowed=y"
          }

respuestasConsultas = { 
                        'consulta problema' : {1 : "Respuesta problema 1", 2 : "https://imgur.com/ecmNey1", 3 : "Respuesta problema 3"},
                        'consulta causas' : {1 : "Respuesta causas 1", 2 : "https://imgur.com/nDNkpCN", 3 : "Respuesta causas 3"},
                        'consulta impacto social' : {1 : "Respuesta impacto social 1", 2 : "https://imgur.com/BzYkJdv", 3 : "Respuesta impacto social 3"},
                        'consulta impacto salud' : {1 : "Respuesta impacto salud 1", 2 : "https://imgur.com/33bcdvm", 3 : "Respuesta impacto salud 3"},
                        'consulta impacto demografico' : {1 : "Respuesta impacto demografico 1", 2 : "https://imgur.com/QALMpBJ", 3 : "Respuesta impacto demografico 3"},
                        'consulta impacto economico' : {1 : "Respuesta impacto economico 1", 2 : "Respuesta impacto economico 2", 3 : "Respuesta impacto economico 3"},
                        'consulta solucion' : {1 : "Respuesta solucion 1", 2 : "Respuesta solucion 2", 3 : "Respuesta solucion 3"}
                      }

CANTIDAD_PREGUNTAS_EXAMEN = 7
CANTIDAD_PREGUNTAS_EXAMEN_TEMA = 3

def agregarAlumno(alumnoNuevo) :
    perfilNuevo = {
                    'cantidadConsultas' : 0, 
                    'ultimaConsulta' : None,
                    'cantidad consulta problema' : 0,
                    'cantidad consulta causas' : 0,
                    'cantidad consulta impacto social' : 0,
                    'cantidad consulta impacto salud' : 0, 
                    'cantidad consulta impacto demografico' : 0, 
                    'cantidad consulta impacto economico' : 0,
                    'cantidad consulta solucion' : 0,
                    'promedio entendimiento' : 1, 
                    'examenes intentados' : 0, 
                    'examenes aprobados' : 0, 
                    'promedio errores examen' : 0, 
                    'cantidad entradas chat' : 0
                  }
    alumnos[alumnoNuevo] = perfilNuevo

preguntasExamen = {
                    'pregunta1' : {
                                    'alternativa0' : "Hay dos características del cambio climático actual que hace que los impactos biofísicos y sociales globales asociados sean únicos en la historia del planeta", 
                                    'alternativa1' : "¿Cuáles son los gases de efecto invernadero?", 
                                    'alternativa2' : "¿Cuánto aumento la temperatura global de la tierra debido al efecto invernadero en el último siglo?"
                                  }, 
                    'pregunta2' : {
                                    'alternativa0' : "¿Cuáles son las causantes del efecto invernadero?", 
                                    'alternativa1' : "¿Cuánto creció el consumo energético mundial en las 2 últimas décadas?", 
                                    'alternativa2' : "¿Cuánto se prevé que aumentara el consumo energético de aquí al 2030?"
                                  }, 
                    'pregunta3' : {
                                    'alternativa0' : "El cambio climático es:", 
                                    'alternativa1' : "El cambio climático afecta a…", 
                                    'alternativa2' : "¿El cambio climático también es consecuencia de la velocidad del cambio social en las sociedades contemporáneas que afecta?"
                                  }, 
                    'pregunta4' : {
                                    'alternativa0' : "El cambio climático, ¿perjudica y/o beneficia la salud humana?", 
                                    'alternativa1' : "Además de olas de calor, las cuales provocaron la muerte de muchas personas. ¿Que otras consecuencias hubo por el cambio climático?", 
                                    'alternativa2' : "Potenciales beneficios para la salud causados por el cambio climatico: "
                                  }, 
                    'pregunta5' : {
                                    'alternativa0' : "Las migraciones internacionales:", 
                                    'alternativa1' : "Las migraciones dentro de un pais", 
                                    'alternativa2' : "El/los impactos inmediatos de las migraciones se manifiestan en:"
                                  }, 
                    'pregunta6' : {
                                    'alternativa0' : "La rápida urbanización de zonas bajas costeras, tanto en el mundo económicamente desarrollado como en el mundo empobrecido, está produciendo:", 
                                    'alternativa1' : "¿Que asentamientos humanos son mas vulnerables a los impactos del cambio climatico?",
                                    'alternativa2' : "Existen testimonios que corroboran el colapso de civilizaciones por razones medioambientales a los que no quisieron o no supieron adaptarse, ¿cuál sería un ejemplo?"
                                  },
                    'pregunta7' : {
                                    'alternativa0' : "¿Que cambio en el modelo energetico hegemonico seria propicio como solucion al cambio climatico?",
                                    'alternativa1' : "¿Cuál es un acuerdo mundial para la lucha del cambio climático?", 
                                    'alternativa2' : "¿Cuántos países firmaron el acuerdo mundial para la lucha del cambio climático?"
                                  }
                  }
                  
opcionesExamen = {
                    'pregunta1' : {
                                    'alternativa0' : {'opcionA' : "Pasividad y debilidad", 'opcionB' : "Rapidez e intensidad", 'opcionC' : "Lento e intenso"}, 
                                    'alternativa1' : {'opcionA' : "Dióxido de carbono, Metano y Óxidos de nitrógeno", 'opcionB' : "Amoniaco, Benceno y neón", 'opcionC' : "Sulfuro de hidrógeno, Monóxido de carbono"}, 
                                    'alternativa2' : {'opcionA' : "0, 5º C", 'opcionB' : "0, 7º C", 'opcionC' : "0, 9º C"}
                                  }, 
                    'pregunta2' : {
                                    'alternativa0' : {'opcionA' : "El petróleo, el gas natural y el carbón", 'opcionB' : "El petroleo y el gas natural", 'opcionC' : "El carbon y el petroleo"}, 
                                    'alternativa1' : {'opcionA' : "30%", 'opcionB' : "40%", 'opcionC' : "25%"}, 
                                    'alternativa2' : {'opcionA' : "48%", 'opcionB' : "53%", 'opcionC' : "67%"}
                                  }, 
                    'pregunta3' : {
                                    'alternativa0' : {'opcionA' : "Un hecho social", 'opcionB' : "Un hecho ambiental", 'opcionC' : "Un hecho economico"}, 
                                    'alternativa1' : {'opcionA' : "Todos sus ecosistemas y a todas sus sociedades, incluyendo las generaciones futuras", 'opcionB' : "Solo las sociedades", 'opcionC' : "Generaciones futuras"}, 
                                    'alternativa2' : {'opcionA' : "Verdadero", 'opcionB' : "Falso", 'opcionC' : "Depende de otros factores"}
                                  }, 
                    'pregunta4' : {
                                    'alternativa0' : {'opcionA' : "Perjudica", 'opcionB' : "Beneficia", 'opcionC' : "Perjudica y beneficia en algunos casos"}, 
                                    'alternativa1' : {'opcionA' : "Diseminación de enfermedades y problemas respiratorios", 'opcionB' : "Aumento de cáncer en la piel y lesiones oculares", 'opcionC' : "Todos los mencionados, entre otros"}, 
                                    'alternativa2' : {'opcionA' : "Inviernos menos fríos en algunas regiones y el calentamiento y las sequías que en algunas zonas pueden disminuir el ciclo vital de los mosquitos y su periodo de transmisión", 'opcionB' : "Inviernos menos fríos en algunas regiones", 'opcionC' : "El calentamiento y las sequías que en algunas zonas pueden disminuir el ciclo vital de los mosquitos y su periodo de transmisión"}
                                  }, 
                    'pregunta5' : {
                                    'alternativa0' : {'opcionA' : "Aumentaron", 'opcionB' : "Disminuyeron", 'opcionC' : "No se vieron afectadas"}, 
                                    'alternativa1' : {'opcionA' : "Aumentaron", 'opcionB' : "Disminuyeron", 'opcionC' : "No se vieron afectadas"}, 
                                    'alternativa2' : {'opcionA' : "La esfera económica, las relaciones sociales, la cultura, la política nacional y las relaciones internacionales", 'opcionB' : "La esfera económica", 'opcionC' : "La esfera económica, las relaciones sociales y la cultura"}
                                  }, 
                    'pregunta6' : {
                                    'alternativa0' : {'opcionA' : "un aumento de la densidad de población y de los bienes humanos expuestos a extremos climáticos en las costas", 'opcionB' : "una bajada de la densidad de población y de los bienes humanos expuestos a extremos climáticos en las costas", 'opcionC' : "un aumento de la densidad de población pero sin exposicion a extremos climáticos en las costas"}, 
                                    'alternativa1' : {'opcionA' : "Aquellos con poca diversificacion economica", 'opcionB' : "Aquellos con economias diversificadas", 'opcionC' : "Aquellos con poca diversificación económica, y en los que un elevado porcentaje de la renta proviene del sector primario sensible al clima"}, 
                                    'alternativa2' : {'opcionA' : "Isla de Pascua (Chile)", 'opcionB' : "Islas Galápagos (Ecuador)", 'opcionC' : "Isla del Sol (Bolivia)"}
                                  },
                    'pregunta7' : {
                                    'alternativa0' : {'opcionA' : "Continuar utilizando combustibles fosiles", 'opcionB' : "Aun no se conoce ningun modelo alternativo que no contribuya al cambio climatico", 'opcionC' : "Cambiar a un modelo donde las energias renovables, limpias, y sostenidas sean protagonistas"}, 
                                    'alternativa1' : {'opcionA' : "El Protocolo de Kioto", 'opcionB' : "El Protocolo Kansai", 'opcionC' : "El Protocolo Kisawa"}, 
                                    'alternativa2' : {'opcionA' : "50", 'opcionB' : "150", 'opcionC' : "Mas de 150"}
                                  }
                 }
respuestasExamen = {
                        'pregunta1' : {
                                        'alternativa0' : "Rapidez e intensidad", 
                                        'alternativa1' : "Dióxido de carbono, Metano y Óxidos de nitrógeno", 
                                        'alternativa2' : "0, 7º C"
                                      }, 
                        'pregunta2' : {
                                        'alternativa0' : "El petróleo, el gas natural y el carbón", 
                                        'alternativa1' : "30%", 
                                        'alternativa2' : "53 %"
                                      }, 
                        'pregunta3' : {
                                        'alternativa0' : "Un hecho social", 
                                        'alternativa1' : "Todos sus ecosistemas y a todas sus sociedades, incluyendo las generaciones futuras", 
                                        'alternativa2' : "Verdadero"         
                                      }, 
                        'pregunta4' : {
                                        'alternativa0' : "Perjudica y beneficia en algunos casos", 
                                        'alternativa1' : "Todos los mencionados, entre otros", 
                                        'alternativa2' : "Inviernos menos fríos en algunas regiones y el calentamiento y las sequías que en algunas zonas pueden disminuir el ciclo vital de los mosquitos y su periodo de transmisión"
                                      }, 
                        'pregunta5' : {
                                        'alternativa0' : "Aumentaron", 
                                        'alternativa1' : "Disminuyeron", 
                                        'alternativa2' : "La esfera económica, las relaciones sociales, la cultura, la política nacional y las relaciones internacionales"
                                      }, 
                        'pregunta6' : {
                                        'alternativa0' : "un aumento de la densidad de población y de los bienes humanos expuestos a extremos climáticos en las costas", 
                                        'alternativa1' : "Aquellos con poca diversificación económica, y en los que un elevado porcentaje de la renta proviene del sector primario sensible al clima", 
                                        'alternativa2' : "Isla de Pascua (Chile)"
                                      },
                        'pregunta7' : {
                                        'alternativa0' : "Cambiar a un modelo donde las energias renovables, limpias, y sostenidas sean protagonistas", 
                                        'alternativa1' : "El Protocolo Kioto", 
                                        'alternativa2' : "Mas de 150"
                                      }
                   }

def generarEvaluacion():
    p1 = random.choice(list(preguntasExamen['pregunta1'].keys()))
    p2 = random.choice(list(preguntasExamen['pregunta2'].keys()))
    p3 = random.choice(list(preguntasExamen['pregunta3'].keys()))
    p4 = random.choice(list(preguntasExamen['pregunta4'].keys()))
    p5 = random.choice(list(preguntasExamen['pregunta5'].keys()))
    p6 = random.choice(list(preguntasExamen['pregunta6'].keys()))
    p7 = random.choice(list(preguntasExamen['pregunta7'].keys()))
    return {
                'pregunta1' : {'pregunta' : preguntasExamen['pregunta1'][p1], 'opciones' : opcionesExamen['pregunta1'][p1], 'respuesta' : respuestasExamen['pregunta1'][p1]}, 
                'pregunta2' : {'pregunta' : preguntasExamen['pregunta2'][p2], 'opciones' : opcionesExamen['pregunta2'][p2], 'respuesta' : respuestasExamen['pregunta2'][p2]}, 
                'pregunta3' : {'pregunta' : preguntasExamen['pregunta3'][p3], 'opciones' : opcionesExamen['pregunta3'][p3], 'respuesta' : respuestasExamen['pregunta3'][p3]}, 
                'pregunta4' : {'pregunta' : preguntasExamen['pregunta4'][p4], 'opciones' : opcionesExamen['pregunta4'][p4], 'respuesta' : respuestasExamen['pregunta4'][p4]}, 
                'pregunta5' : {'pregunta' : preguntasExamen['pregunta5'][p5], 'opciones' : opcionesExamen['pregunta5'][p5], 'respuesta' : respuestasExamen['pregunta5'][p5]}, 
                'pregunta6' : {'pregunta' : preguntasExamen['pregunta6'][p6], 'opciones' : opcionesExamen['pregunta6'][p6], 'respuesta' : respuestasExamen['pregunta6'][p6]},
                'pregunta7' : {'pregunta' : preguntasExamen['pregunta7'][p7], 'opciones' : opcionesExamen['pregunta7'][p7], 'respuesta' : respuestasExamen['pregunta7'][p7]}
           }

def buenConcepto(alum):
    if alumnos[alum]['cantidadConsultas'] >= 10 and alumnos[alum]['cantidad entradas chat'] >= 10:
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
    
def corregirEvaluacion(alum, examen, rta1, rta2, rta3, rta4, rta5, rta6, rta7):
    correccion = corregirRespuestas([rta1, rta2, rta3, rta4, rta5, rta6, rta7], examen)
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
    alumnos[alum]['promedio errores examen'] += ((CANTIDAD_PREGUNTAS_EXAMEN - correccion['cont']) / (alumnos[alum]['examenes intentados'] + (alumnos[alum]['examenes intentados'] - 1)))
    return correccion

def corregirEvaluacionTema(alum, examen, rta1, rta2, rta3):
    correccion = corregirRespuestas([rta1, rta2, rta3], examen)
    if correccion['cont'] == CANTIDAD_PREGUNTAS_EXAMEN_TEMA:
        correccion['devolucion'] = "¡Felicitaciones " + alum + "! ¡Aprobaste la mini evaluacion!"
    else:
       correccion['devolucion'] = "No te desanimes " + alum + ", a seguir estudiando."
    return correccion

def generarEvaluacionTema(tema):
    if tema == 'consulta problema':
        llave = 'pregunta1'
    if tema == 'consulta causas':
        llave = 'pregunta2'
    if tema == 'consulta impacto social':
        llave = 'pregunta3'
    if tema == 'consulta impacto salud':
        llave = 'pregunta4'
    if tema == 'consulta impacto demografico':
        llave = 'pregunta5'
    if tema == 'consulta impacto economico':
        llave = 'pregunta6'
    if tema == 'consulta solucion':
        llave = 'pregunta7'
    return {
                'pregunta1' : {'pregunta' : preguntasExamen[llave]['alternativa0'], 'opciones' : opcionesExamen[llave]['alternativa0'], 'respuesta' : respuestasExamen[llave]['alternativa0']}, 
                'pregunta2' : {'pregunta' : preguntasExamen[llave]['alternativa1'], 'opciones' : opcionesExamen[llave]['alternativa1'], 'respuesta' : respuestasExamen[llave]['alternativa1']}, 
                'pregunta3' : {'pregunta' : preguntasExamen[llave]['alternativa2'], 'opciones' : opcionesExamen[llave]['alternativa2'], 'respuesta' : respuestasExamen[llave]['alternativa2']}
           }

def identificarse(alum):
    if not alum in alumnos.keys():
            agregarAlumno(alum)
    alumnos[alum]['cantidad entradas chat'] += 1
    return {'message' : "¡Un gusto " +  alum + "!"}

def ultimaConsulta(alum):
    if alumnos[alum]['ultimaConsulta'] != None:
        return {'message' : alum + ", la ultima vez consultaste sobre: " +  alumnos[alum]['ultimaConsulta'] + "\n ¿querés hacer una evaluacion sobre ese tema en forma de repaso?"}
    else:
        return {'message' : alum + ", aun no has realizado ninguna consulta en esta clase"}

def temas():
    return {'message' : materia['temas_materia']}

def consulta(alum, llaveConsulta, tipoConsulta, contador):
    alumnos[alum]['cantidadConsultas'] += 1
    alumnos[alum][llaveConsulta] += 1
    if alumnos[alum]['ultimaConsulta'] != tipoConsulta:
        alumnos[alum]['ultimaConsulta'] = tipoConsulta
        contador = 1 #se iniciaria en uno?
    if contador > 1 and contador <= 3:
        respuesta = {'message' : respuestasConsultas[tipoConsulta][contador], "entiende" : contador}
    elif contador > 3:
        respuesta = {'message' : "Vas a tener que seguir estudiando " + alum + ", te recomiendo revisar la bibliografia del curso: \n" + materia['bibliografia']}
    else:
        respuesta = {'message' : respuestasConsultas[tipoConsulta][alumnos[alum]['promedio entendimiento']], 'entiende' : 1}
    return respuesta
            
def verificarEntendimiento(alum, nivelEntendimiento):
    alumnos[alum]['promedio entendimiento'] = round((((alumnos[alum]['cantidadConsultas'] - 1) * alumnos[alum]['promedio entendimiento']) + nivelEntendimiento) / alumnos[alum]['cantidadConsultas'])
    return {'' : ""}

def actualizarContador(cont):
    cont['valor'] += 1
    return cont

def main(dict):
    if dict['identificarse'] == 1:
        return identificarse(dict['nombre'])
        
    if dict['temas'] == 1:
        return temas()
    
    if dict['ultimaConsulta'] == 1:
        return ultimaConsulta(dict['nombre'])
        
    if dict['evaluacionTema'] != -1:
        if dict['evaluacionTema'] == 0:
            return generarEvaluacionTema(alumnos[dict['nombre']]['ultimaConsulta'])
        if dict['evaluacionTema'] > 0 and dict['evaluacionTema'] <= CANTIDAD_PREGUNTAS_EXAMEN_TEMA:
            llavePregunta = "pregunta" + repr(dict['evaluacionTema'])
            return dict['examenTema'][llavePregunta]
        if dict['evaluacionTema'] == CANTIDAD_PREGUNTAS_EXAMEN_TEMA + 1:
            correccion = corregirEvaluacionTema(dict['nombre'], dict['examenTema'], dict['rta1tema'], dict['rta2tema'], dict['rta3tema'])
            return {'message' : correccion['pregunta1'] + "\n" + correccion['pregunta2'] + "\n" + correccion['pregunta3'] + "\n" + correccion['devolucion']}
        
    if dict['tipoConsulta'] != -1:
        llaveConsulta = "cantidad " + dict['tipoConsulta']
        return consulta(dict['nombre'], llaveConsulta, dict['tipoConsulta'], dict['contadorNoEntiende']['valor'])
    
    if dict['verificarEntendimiento'] == 1:
        return verificarEntendimiento(dict['nombre'], dict['entiende']['entiende'])
    
    if dict['niegaEntendimiento'] == 1:
        return actualizarContador(dict['contadorNoEntiende'])

    if dict['bibliografia'] == 1:
        return {'message' : materia['bibliografia']}
    
    if dict['evaluacion'] != -1:
        if dict['evaluacion'] == 0:
            alumnos[dict['nombre']]['examenes intentados'] += 1
            return generarEvaluacion()
        if dict['evaluacion'] > 0 and dict['evaluacion'] <= CANTIDAD_PREGUNTAS_EXAMEN:
            llavePregunta = "pregunta" + repr(dict['evaluacion'])
            return dict['examen'][llavePregunta]
        if dict['evaluacion'] == CANTIDAD_PREGUNTAS_EXAMEN + 1:
            correccion = corregirEvaluacion(dict['nombre'], dict['examen'], dict['rta1'], dict['rta2'], dict['rta3'], dict['rta4'], dict['rta5'], dict['rta6'], dict['rta7'])
            return {'message' : correccion['pregunta1'] + "\n" + correccion['pregunta2'] + "\n" + correccion['pregunta3'] + "\n" + correccion['pregunta4'] + "\n" + correccion['pregunta5'] + "\n" + correccion['pregunta6'] + "\n" + correccion['devolucion']}