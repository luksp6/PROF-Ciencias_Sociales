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
            'Lucas' : {'cantidadConsultas' : 1, 'ultimaConsulta' : "el problema del cambio climatico", 'cantidad el problema del cambio climatico' : 0, 'cantidad las causas del cambio climatico' : 0, 'cantidad el problema del cambio climatico' : 0, 'cantidad las causas del cambio climatico' : 0, 'cantidad el impacto social del cambio climatico' : 0, 'cantidad el impacto del cambio climatico en la salud' : 0, 'cantidad el impacto demografico del cambio climatico' : 0, 'cantidad el impacto economico del cambio climatico' : 0, 'cantidad el impacto del cambio climatico en la organizacion social' : 0, 'cantidad la solucion al cambio climatico' : 0, 'promedio entendimiento' : 2, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0}, 
            'Pablo' : {'cantidadConsultas' : 1, 'ultimaConsulta' : None, 'cantidad el problema del cambio climatico' : 0, 'cantidad las causas del cambio climatico' : 0, 'cantidad el impacto social del cambio climatico' : 0, 'cantidad el impacto del cambio climatico en la salud' : 0, 'cantidad el impacto demografico del cambio climatico' : 0, 'cantidad el impacto economico del cambio climatico' : 0, 'cantidad el impacto en la organizacion de la sociedad' : 0, 'cantidad la solucion al cambio climatico' : 0, 'promedio entendimiento' : 1, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0},
            'Luis' : {'cantidadConsultas' : 1, 'ultimaConsulta' : None, 'cantidad el problema del cambio climatico' : 0, 'cantidad las causas del cambio climatico' : 0, 'cantidad el impacto social del cambio climatico' : 0, 'cantidad el impacto del cambio climatico en la salud' : 0, 'cantidad el impacto demografico del cambio climatico' : 0, 'cantidad el impacto economico del cambio climatico' : 0, 'cantidad el impacto en la organizacion de la sociedad' : 0, 'cantidad la solucion al cambio climatico' : 0, 'promedio entendimiento' : 1, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0}, 
            'Mateo' : {'cantidadConsultas' : 1, 'ultimaConsulta' : None, 'cantidad el problema del cambio climatico' : 0, 'cantidad las causas del cambio climatico' : 0, 'cantidad el impacto social del cambio climatico' : 0, 'cantidad el impacto del cambio climatico en la salud' : 0, 'cantidad el impacto demografico del cambio climatico' : 0, 'cantidad el impacto economico del cambio climatico' : 0, 'cantidad el impacto en la organizacion de la sociedad' : 0, 'cantidad la solucion al cambio climatico' : 0, 'promedio entendimiento' : 1, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0}, 
            'Florencia' : {'cantidadConsultas' : 1, 'ultimaConsulta' : None, 'cantidad el problema del cambio climatico' : 0, 'cantidad las causas del cambio climatico' : 0, 'cantidad el impacto social del cambio climatico' : 0, 'cantidad el impacto del cambio climatico en la salud' : 0, 'cantidad el impacto demografico del cambio climatico' : 0, 'cantidad el impacto economico del cambio climatico' : 0, 'cantidad el impacto en la organizacion de la sociedad' : 0, 'cantidad la solucion al cambio climatico' : 0, 'promedio entendimiento' : 1, 'examenes intentados' : 0, 'examenes aprobados' : 0, 'promedio errores examen' : 0, 'cantidad entradas chat' : 0},
          }


materia = {
                'temas_materia' : "Los temas de nuestra clase son: \n | El problema del cambio climático. \n | Las causas del cambio climático. \n | El impacto social del cambio climático. \n | El impacto en la salud humana del cambio climático. \n | El impacto demográfico del cambio climático. \n | El impacto económico del cambio climático. \n | El impacto en la organizacion social del cambio climatico \n | Las soluciones al problema del cambio climático. ", 
                'bibliografia' : "| Fuente: Pardo Buendía, M. (2007). El impacto social del cambio climático. \n | Link: https://e-archivo.uc3m.es/bitstream/handle/10016/10448/impacto_pardo_2007.pdf?sequence=1&isAllowed=y"
          }

respuestasConsultas = { 
                        'el problema del cambio climatico' : {1 : "Hay dos características del cambio climático actual que hace que los impactos biofísicos y sociales globales asociados sean únicos en la historia del planeta: la rapidez e intensidad con la que este cambio está teniendo lugar.El aumento de la concentración del CO2 (gas de efecto invernadero) y crece muy rápidamente, La concentración del metano sucede lo mismo, en poco tiempo aumento su concentración y su crecimiento es elevado. Aunque hoy mismo dejemos de emitir estos gases tardaría la atmósfera centenares de años (si no más, pues hay incertidumbre al respecto) en volver a los niveles previos a la industrialización. Como resultado de ello, la temperatura global de la Tierra ha aumentado ya 0, 7º C en el último siglo, y se asume (IPCC, 2007) como bastante inevitable un incremento de 2º C a final de siglo.A este ritmo y la suba promedio de 2º C tendrá consecuencias, en algunas partes del planeta se elevará la temperatura hasta cifras alarmantes, y en otras por el contrario pudieran llegar a bajar hasta convertirlas en fríos polares, también significa un aumento considerable de los episodios catastróficos de huracanes, inundaciones, sequías, aumento del nivel del mar. El huracán 'Mitch', 'Katrina', el fenómeno el 'Niño'   ", 2 : "En este link se encuentra un cuadro de resumen del tema, ¡Espero que te ayude! \n | https://imgur.com/ecmNey1", 3 : "Te dejo este video relacionado con tu consulta, ¡Espero que te ayude! \n | https://www.youtube.com/watch?v=fIxvO4ue4Ow"},
                        'las causas del cambio climatico' : {1 : "Si bien, la evolución y variabilidad del clima históricamente proviene de un proceso natural, actualmente el cambio climático proviene de causas sociales. La masiva emisión de gases de invernadero (CO2, metano, oxido de nitrógeno) y sobre todo a la combustión de energía fósil desde el inicio de la industrialización.El efecto invernadero proviene de las fuentes de energía actual (fósiles), ya que tanto como el desarrollo industrial y social se basan en un modelo energético de fósiles.Además, hay que atribuir la responsabilidad al aumento del consumo energético mundial ya que creció en un 30% entre los ‘80 y los ’00 donde se prevé que para el 2030 se aumente un 53% (mirando desde los años ’00), y cabe resaltar, que también el 40% de la población mundial aun no tiene acceso a la electricidad y necesitan la quema de leña para calefacción y la cocina.", 2 : "En este link se encuentra un cuadro de resumen del tema, ¡Espero que te ayude! \n | https://imgur.com/nDNkpCN", 3 : "Te dejo estos videos relacionados con tu consulta, ¡Espero que te ayuden! \n | https://www.youtube.com/watch?v=KFmlogPvVoY \n | https://www.youtube.com/watch?v=XZ0PsFo9rCo"},
                        'el impacto social del cambio climatico' : {1 : "El cambio climático es un hecho social, las personas que componen esas sociedades, quienes finalmente van a sufrir sus consecuencias directa o indirectamente a través del cambio del medio biogeofísico. el cambio climático afecta a la globalidad del planeta: a todos sus ecosistemas y a todas sus sociedades, incluyendo las generaciones futuras. Por esta razón, las soluciones parciales únicamente suponen un alivio momentáneo para la crisis general. Gran parte del problema del denominado cambio climático, se está produciendo por la fuerte velocidad del cambio social en las sociedades contemporáneas (el aumento de la demanda de energía y de recursos básicos, por ejemplo). las consecuencias sociales serán —están siendo— diferentes según sean las características concretas de las distintas sociedades. En algunos casos, el mismo tipo de cambio biogeofísico puede producir consecuencias sociales negativas en unos lugares y positivas en otros (más horas solares, por ejemplo, permiten producir energía solar). Los impactos reales sobre la salud de la población van a estar muy determinados por las condiciones ambientales locales y también por las circunstancias socioeconómicas de esa población. ", 2 : "En este link se encuentra un cuadro de resumen del tema, ¡Espero que te ayude! \n | https://imgur.com/BzYkJdv", 3 : "Te dejo este video relacionado con tu consulta, ¡Espero que te ayude! \n | https://www.youtube.com/watch?v=GQdx0OKuEKw"},
                        'el impacto del cambio climatico en la salud' : {1 : "El cambio climático puede llegar a perjudicar de muchas maneras la salud humana, aunque también beneficiarla en algunos lugares, según las circunstancias. Los efectos que el cambio climático que esta trayendo un impacto al ser humano son: Las olas de calor, el esparcimiento de enfermedades infecciosas (por ejemplo, la diarrea), el aumento del cáncer de piel, lesiones oculares, problemas respiratorios y por último, desnutrición. Pero no todo es desfavorable, el cambio climático también producirá algunas mejoras: inviernos menos fríos en algunas regiones (el frío es un factor de riesgo para la salud humana), y el calentamiento y las sequías que en algunas zonas pueden disminuir el ciclo vital de los mosquitos y su periodo de transmisión.", 2 : "En este link se encuentra un cuadro de resumen del tema, ¡Espero que te ayude! \n | https://imgur.com/33bcdvm", 3 : "Te dejo estos videos relacionados con tu consulta, ¡Espero que te ayuden! \n | https://www.youtube.com/watch?v=XPVuEZlscf4 \n | https://www.youtube.com/watch?v=e_pkGReTvZ4"},
                        'el impacto demografico del cambio climatico' : {1 : "Las migraciones internacionales han aumentado considerablemente en las últimas décadas, debido a las tasas demográficas (alta tasa de fecundidad en los países empobrecidos y baja en los económicamente desarrollados); la presión migratoria desde los países del norte de África hacia los del sur de Europa, desde Latinoamérica hacia Estados Unidos, desde el este y el suroeste asiático hacia Norteamérica y tal vez hacia Japón, y desde algunas de las antiguas repúblicas soviéticas hacia Rusia. Pero los movimientos migratorios también tienen lugar dentro de los propios países. En Estados Unidos, los desplazamientos hacia las zonas costeras del Pacífico. En China desde las zonas más áridas y pobres del interior a las provincias del litoral. En España ocurre algo similar hacia el litoral mediterráneo. Con mucho, el fenómeno que se repite en todas las partes del mundo es la emigración de las zonas rurales a las áreas metropolitanas, así como la expansión de éstas. ", 2 : "En este link se encuentra un cuadro de resumen del tema, ¡Espero que te ayude! \n | https://imgur.com/QALMpBJ", 3 : "Te dejo este video relacionado con tu consulta, ¡Espero que te ayude! \n | https://www.youtube.com/watch?v=Xe_k3_Ia93o"},
                        'el impacto economico del cambio climatico' : {1 : "Los asentamientos humanos, están siendo afectados por razón de: Cambios en la productividad, Cambios en las infraestructuras, cambios indirectos sociodemográficos.El riesgo directo que afecta en más partes del mundo a los asentamientos humanos es el de inundaciones y movimientos de tierra: en las zonas costeras, por la subida del nivel del mar y mayor número e intensidad de temporales y huracanes. Este riesgo es mayor para las poblaciones con menos recursos. La población a tenido numerosas pérdidas económicas a razón de la agravación de temperatura, las inundaciones provocadas por lluvia y fenómenos naturales, además de la urbanización que se llevo a cabo en zonas costeras provoco que haya muchas perdidas en el ámbito económico por culpa de los fenómenos naturales como ciclones, tsunamis, terremotos. La sobreexplotación de la pesca a provocado también que haya proliferaciones de medusas en distintas áreas del océano, generando daños por ejemplo en el turismo, que genera daños económicos a las ciudades y/o países que las playas son su mayor fuerte de turismo.", 2 : "En este link se encuentra un cuadro de resumen del tema, ¡Espero que te ayude! \n | https://imgur.com/Joe3cq2", 3 : "Te dejo estos videos relacionados con tu consulta, ¡Espero que te ayuden! \n | https://www.youtube.com/watch?v=XVYt-Ssr_8E \n | https://www.youtube.com/watch?v=SoqWiCPploI"},
                        'el impacto en la organizacion de la sociedad' : {1 : "El cambio climático está produciendo un impacto destacable en diversos aspectos de la organización social, así como en las normas y valores sociales, incluyendo la gobernabilidad de las sociedades y el desarrollo de los sistemas de democracia. ). Los riesgos biogeofísicos que conllevan el cambio climático afectan en mayor medida a los sectores más vulnerables de todas las sociedades (los pobres, los ancianos, los niños, las mujeres, los más débiles…) ya que cuentan con menos recursos no sólo económicos, sino también de información, de educación e incluso del necesario ánimo y autoestima para prevenir y mitigar los efectos del cambio climático. En cuanto a las normas y valores sociales, como instrumentos de adaptación social que son, son susceptibles de ser modificados por las mismas sociedades para preparar la acción social a los cambios necesarios. El Protocolo de Kioto para luchar contra el cambio climático, por ejemplo, es de los pocos acuerdos mundiales existentes (firmado por más de 150 países) aun conllevando importantes compromisos económicos, este protocolo nació para poder reducir las emisiones de gases contaminantes en 5% en un periodo entre 2008 y 2012. Por otra parte, una consecuencia del cambio climático está siendo la participación de nuevos actores sociales en el proceso de discurso y legitimación, destacando la creciente importancia del movimiento ecologista como actor social y una de las posibles consecuencias del cambio climático es la ya visible tendencia a la privatización de los bienes comunes (el aire, por ejemplo).", 2 : "En este link se encuentra un cuadro de resumen del tema, ¡Espero que te ayude! \n | https://imgur.com/7L520XK", 3 : "Te dejo este video relacionado con tu consulta, ¡Espero que te ayude! \n | https://www.youtube.com/watch?v=85u07bxPrEs "},
                        'la solucion al cambio climatico' : {1 : "El cambio en el modelo energético hegemónico basado en combustibles fósiles contaminantes está en el centro de las soluciones, dirigidas a la construcción de otro modelo en donde las energías renovables (solar, eólica, biomasa), limpias y sostenibles en el tiempo, tengan un papel protagonista. También buscar el cumplimiento de los tratados y protocolos que se establecieron (por ejemplo el protocolo de Kioto) para que se pueda ir disminuyendo el daño que le hacemos al ambiente y así generando que el cambio climático no sea tan severo como viene siendo en los últimos 70 años por la urbanización.", 2 : "En este link se encuentra un cuadro de resumen del tema, ¡Espero que te ayude! \n | https://imgur.com/2DA57dO", 3 : "Te dejo este video relacionado con tu consulta, ¡Espero que te ayude! \n | https://www.youtube.com/watch?v=0XZoz3J8jvQ"}
                      }

CANTIDAD_PREGUNTAS_EXAMEN = 8
CANTIDAD_PREGUNTAS_EXAMEN_TEMA = 3

def agregarAlumno(alumnoNuevo) :
    perfilNuevo = {
                    'cantidadConsultas' : 0, 
                    'ultimaConsulta' : None,
                    'cantidad el problema del cambio climatico' : 0,
                    'cantidad las causas del cambio climatico' : 0,
                    'cantidad el impacto social del cambio climatico' : 0,
                    'cantidad el impacto del cambio climatico en la salud' : 0, 
                    'cantidad el impacto demografico del cambio climatico' : 0, 
                    'cantidad el impacto economico del cambio climatico' : 0,
                    'cantidad el impacto en la organizacion de la sociedad' : 0,
                    'cantidad la solucion al cambio climatico' : 0,
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
                                    'alternativa2' : "Un nuevo factor asociado al cambio climático seria…"
                                  },
                    'pregunta7' : {
                                    'alternativa0' : "¿Que cambio en el modelo energetico hegemonico seria propicio como solucion al cambio climatico?",
                                    'alternativa1' : "¿Cuál es un acuerdo mundial para la lucha del cambio climático?", 
                                    'alternativa2' : "¿Cuántos países firmaron el acuerdo mundial para la lucha del cambio climático?"
                                  },
                    'pregunta8' : {
                                    'alternativa0' : "¿Cuál sería una posible ayuda al problema?",
                                    'alternativa1' : "Según El Libro Verde sobre la Energía de la Unión Europea (2006) documenta que se podría ahorrar energía. ¿Cuánto seria considerando el tipo de energía mencionado en el item 21?", 
                                    'alternativa2' : "Una solución al problema del cambio climático, seria cumplir con los objetivos que se tasaron en el protocolo de Kioto. ¿Qué país no lo cumplió?"
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
                                    'alternativa1' : {'opcionA' : "< 30%", 'opcionB' : "30%", 'opcionC' : "> 30%"}, 
                                    'alternativa2' : {'opcionA' : "< 53%", 'opcionB' : "53%", 'opcionC' : "> 53%"}
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
                                    'alternativa0' : {'opcionA' : "Inundaciones y movimientos de tierra", 'opcionB' : "Terremotos y tsunamis", 'opcionC' : "Erupciones y hambruna"}, 
                                    'alternativa1' : {'opcionA' : "Aquellos con poca diversificacion economica", 'opcionB' : "Aquellos con economias diversificadas", 'opcionC' : "Aquellos con poca diversificación económica, y en los que un elevado porcentaje de la renta proviene del sector primario sensible al clima"}, 
                                    'alternativa2' : {'opcionA' : "La proliferación de hippocampus", 'opcionB' : "La proliferación de cangrejos", 'opcionC' : "La proliferación de medusas"}
                                  },
                    'pregunta7' : {
                                    'alternativa0' : {'opcionA' : "Continuar utilizando combustibles fosiles", 'opcionB' : "Aun no se conoce ningun modelo alternativo que no contribuya al cambio climatico", 'opcionC' : "Cambiar a un modelo donde las energias renovables, limpias, y sostenidas sean protagonistas"}, 
                                    'alternativa1' : {'opcionA' : "El Protocolo de Kioto", 'opcionB' : "El Protocolo Kansai", 'opcionC' : "El Protocolo Kisawa"}, 
                                    'alternativa2' : {'opcionA' : "50", 'opcionB' : "150", 'opcionC' : "Mas de 150"}
                                  },
                    'pregunta8' : {
                                    'alternativa0' : {'opcionA' : "Energias renovables", 'opcionB' : "Energia no renovables", 'opcionC' : "Ninguna de las anteriores"}, 
                                    'alternativa1' : {'opcionA' : "20 % del consumo de energía actual.", 'opcionB' : "10% del consumo de energía actual.", 'opcionC' : "30 % del consumo de energía actual."}, 
                                    'alternativa2' : {'opcionA' : "Estados Unidos y España", 'opcionB' : "Canadá y Japón", 'opcionC' : "Todas las anteriores"}
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
                                        'alternativa1' : "> 30%", 
                                        'alternativa2' : "53%"
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
                                        'alternativa0' : "Inundaciones y movimientos de tierra", 
                                        'alternativa1' : "Aquellos con poca diversificación económica, y en los que un elevado porcentaje de la renta proviene del sector primario sensible al clima", 
                                        'alternativa2' : "La proliferación de medusas"
                                      },
                        'pregunta7' : {
                                        'alternativa0' : "Cambiar a un modelo donde las energias renovables, limpias, y sostenidas sean protagonistas", 
                                        'alternativa1' : "El Protocolo Kioto", 
                                        'alternativa2' : "Mas de 150"
                                      },
                        'pregunta8' : {
                                        'alternativa0' : "Energias renovables", 
                                        'alternativa1' : "20 % del consumo de energía actual.", 
                                        'alternativa2' : "Todas las anteriores"
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
    p8 = random.choice(list(preguntasExamen['pregunta8'].keys()))
    return {
                'pregunta1' : {'pregunta' : preguntasExamen['pregunta1'][p1], 'opciones' : opcionesExamen['pregunta1'][p1], 'respuesta' : respuestasExamen['pregunta1'][p1]}, 
                'pregunta2' : {'pregunta' : preguntasExamen['pregunta2'][p2], 'opciones' : opcionesExamen['pregunta2'][p2], 'respuesta' : respuestasExamen['pregunta2'][p2]}, 
                'pregunta3' : {'pregunta' : preguntasExamen['pregunta3'][p3], 'opciones' : opcionesExamen['pregunta3'][p3], 'respuesta' : respuestasExamen['pregunta3'][p3]}, 
                'pregunta4' : {'pregunta' : preguntasExamen['pregunta4'][p4], 'opciones' : opcionesExamen['pregunta4'][p4], 'respuesta' : respuestasExamen['pregunta4'][p4]}, 
                'pregunta5' : {'pregunta' : preguntasExamen['pregunta5'][p5], 'opciones' : opcionesExamen['pregunta5'][p5], 'respuesta' : respuestasExamen['pregunta5'][p5]}, 
                'pregunta6' : {'pregunta' : preguntasExamen['pregunta6'][p6], 'opciones' : opcionesExamen['pregunta6'][p6], 'respuesta' : respuestasExamen['pregunta6'][p6]},
                'pregunta7' : {'pregunta' : preguntasExamen['pregunta7'][p7], 'opciones' : opcionesExamen['pregunta7'][p7], 'respuesta' : respuestasExamen['pregunta7'][p7]},
                'pregunta8' : {'pregunta' : preguntasExamen['pregunta8'][p8], 'opciones' : opcionesExamen['pregunta8'][p8], 'respuesta' : respuestasExamen['pregunta8'][p8]}
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
    
def corregirEvaluacion(alum, examen, rta1, rta2, rta3, rta4, rta5, rta6, rta7, rta8): 
    correccion = corregirRespuestas([rta1, rta2, rta3, rta4, rta5, rta6, rta7, rta8], examen)
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
    if tema == 'el problema del cambio climatico':
        llave = 'pregunta1'
    if tema == 'las causas del cambio climatico':
        llave = 'pregunta2'
    if tema == 'el impacto social del cambio climatico':
        llave = 'pregunta3'
    if tema == 'el impacto del cambio climatico en la salud':
        llave = 'pregunta4'
    if tema == 'el impacto demografico del cambio climatico':
        llave = 'pregunta5'
    if tema == 'el impacto economico del cambio climatico':
        llave = 'pregunta6'
    if tema == 'el impacto en la organizacion de la sociedad':
        llave = 'pregunta7'
    if tema == 'la solucion al cambio climatico':
        llave = 'pregunta8'
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
        return {'message' : alum + ", la ultima vez consultaste sobre: " +  alumnos[alum]['ultimaConsulta']}
    else:
        return {'message' : alum + ", aun no has realizado ninguna consulta en esta clase"}

def temas():
    return {'message' : materia['temas_materia']}

def consulta(alum, llaveConsulta, tipoConsulta, contador):
    alumnos[alum]['cantidadConsultas'] += 1
    alumnos[alum][llaveConsulta] += 1
    if alumnos[alum]['ultimaConsulta'] == tipoConsulta:
        if contador >= 1 and contador <= 3:
            respuesta = {'message' : respuestasConsultas[tipoConsulta][contador], "entiende" : contador}
        elif contador > 3:
            respuesta = {'message' : "Vas a tener que seguir estudiando " + alum + ", te recomiendo revisar la bibliografia del curso: \n" + materia['bibliografia']}
    else:
        alumnos[alum]['ultimaConsulta'] = tipoConsulta
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
            return generarEvaluacionTema(dict['tipoConsulta'])
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
            correccion = corregirEvaluacion(dict['nombre'], dict['examen'], dict['rta1'], dict['rta2'], dict['rta3'], dict['rta4'], dict['rta5'], dict['rta6'], dict['rta7'], dict['rta8'])
            return {'message' : correccion['pregunta1'] + "\n" + correccion['pregunta2'] + "\n" + correccion['pregunta3'] + "\n" + correccion['pregunta4'] + "\n" + correccion['pregunta5'] + "\n" + correccion['pregunta6'] + "\n" + correccion['pregunta7'] + "\n" + correccion['pregunta8'] + "\n"+ correccion['devolucion']}