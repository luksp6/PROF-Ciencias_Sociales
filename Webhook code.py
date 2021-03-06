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
                'temas_materia' : "Los temas de nuestra clase son: \n | El problema del cambio clim??tico. \n | Las causas del cambio clim??tico. \n | El impacto social del cambio clim??tico. \n | El impacto en la salud humana del cambio clim??tico. \n | El impacto demogr??fico del cambio clim??tico. \n | El impacto econ??mico del cambio clim??tico. \n | El impacto en la organizacion social del cambio climatico \n | Las soluciones al problema del cambio clim??tico. ", 
                'bibliografia' : "| Fuente: Pardo Buend??a, M. (2007). El impacto social del cambio clim??tico. \n | Link: https://e-archivo.uc3m.es/bitstream/handle/10016/10448/impacto_pardo_2007.pdf?sequence=1&isAllowed=y"
          }

respuestasConsultas = { 
                        'el problema del cambio climatico' : {1 : "Hay dos caracter??sticas del cambio clim??tico actual que hace que los impactos biof??sicos y sociales globales asociados sean ??nicos en la historia del planeta: la rapidez e intensidad con la que este cambio est?? teniendo lugar.El aumento de la concentraci??n del CO2 (gas de efecto invernadero) y crece muy r??pidamente, La concentraci??n del metano sucede lo mismo, en poco tiempo aumento su concentraci??n y su crecimiento es elevado. Aunque hoy mismo dejemos de emitir estos gases tardar??a la atm??sfera centenares de a??os (si no m??s, pues hay incertidumbre al respecto) en volver a los niveles previos a la industrializaci??n. Como resultado de ello, la temperatura global de la Tierra ha aumentado ya 0, 7?? C en el ??ltimo siglo, y se asume (IPCC, 2007) como bastante inevitable un incremento de 2?? C a final de siglo.A este ritmo y la suba promedio de 2?? C tendr?? consecuencias, en algunas partes del planeta se elevar?? la temperatura hasta cifras alarmantes, y en otras por el contrario pudieran llegar a bajar hasta convertirlas en fr??os polares, tambi??n significa un aumento considerable de los episodios catastr??ficos de huracanes, inundaciones, sequ??as, aumento del nivel del mar. El hurac??n 'Mitch', 'Katrina', el fen??meno el 'Ni??o'   ", 2 : "En este link se encuentra un cuadro de resumen del tema, ??Espero que te ayude! \n | https://imgur.com/ecmNey1", 3 : "Te dejo este video relacionado con tu consulta, ??Espero que te ayude! \n | https://www.youtube.com/watch?v=fIxvO4ue4Ow"},
                        'las causas del cambio climatico' : {1 : "Si bien, la evoluci??n y variabilidad del clima hist??ricamente proviene de un proceso natural, actualmente el cambio clim??tico proviene de causas sociales. La masiva emisi??n de gases de invernadero (CO2, metano, oxido de nitr??geno) y sobre todo a la combusti??n de energ??a f??sil desde el inicio de la industrializaci??n.El efecto invernadero proviene de las fuentes de energ??a actual (f??siles), ya que tanto como el desarrollo industrial y social se basan en un modelo energ??tico de f??siles.Adem??s, hay que atribuir la responsabilidad al aumento del consumo energ??tico mundial ya que creci?? en un 30% entre los ???80 y los ???00 donde se prev?? que para el 2030 se aumente un 53% (mirando desde los a??os ???00), y cabe resaltar, que tambi??n el 40% de la poblaci??n mundial aun no tiene acceso a la electricidad y necesitan la quema de le??a para calefacci??n y la cocina.", 2 : "En este link se encuentra un cuadro de resumen del tema, ??Espero que te ayude! \n | https://imgur.com/nDNkpCN", 3 : "Te dejo estos videos relacionados con tu consulta, ??Espero que te ayuden! \n | https://www.youtube.com/watch?v=KFmlogPvVoY \n | https://www.youtube.com/watch?v=XZ0PsFo9rCo"},
                        'el impacto social del cambio climatico' : {1 : "El cambio clim??tico es un hecho social, las personas que componen esas sociedades, quienes finalmente van a sufrir sus consecuencias directa o indirectamente a trav??s del cambio del medio biogeof??sico. el cambio clim??tico afecta a la globalidad del planeta: a todos sus ecosistemas y a todas sus sociedades, incluyendo las generaciones futuras. Por esta raz??n, las soluciones parciales ??nicamente suponen un alivio moment??neo para la crisis general. Gran parte del problema del denominado cambio clim??tico, se est?? produciendo por la fuerte velocidad del cambio social en las sociedades contempor??neas (el aumento de la demanda de energ??a y de recursos b??sicos, por ejemplo). las consecuencias sociales ser??n ???est??n siendo??? diferentes seg??n sean las caracter??sticas concretas de las distintas sociedades. En algunos casos, el mismo tipo de cambio biogeof??sico puede producir consecuencias sociales negativas en unos lugares y positivas en otros (m??s horas solares, por ejemplo, permiten producir energ??a solar). Los impactos reales sobre la salud de la poblaci??n van a estar muy determinados por las condiciones ambientales locales y tambi??n por las circunstancias socioecon??micas de esa poblaci??n. ", 2 : "En este link se encuentra un cuadro de resumen del tema, ??Espero que te ayude! \n | https://imgur.com/BzYkJdv", 3 : "Te dejo este video relacionado con tu consulta, ??Espero que te ayude! \n | https://www.youtube.com/watch?v=GQdx0OKuEKw"},
                        'el impacto del cambio climatico en la salud' : {1 : "El cambio clim??tico puede llegar a perjudicar de muchas maneras la salud humana, aunque tambi??n beneficiarla en algunos lugares, seg??n las circunstancias. Los efectos que el cambio clim??tico que esta trayendo un impacto al ser humano son: Las olas de calor, el esparcimiento de enfermedades infecciosas (por ejemplo, la diarrea), el aumento del c??ncer de piel, lesiones oculares, problemas respiratorios y por ??ltimo, desnutrici??n. Pero no todo es desfavorable, el cambio clim??tico tambi??n producir?? algunas mejoras: inviernos menos fr??os en algunas regiones (el fr??o es un factor de riesgo para la salud humana), y el calentamiento y las sequ??as que en algunas zonas pueden disminuir el ciclo vital de los mosquitos y su periodo de transmisi??n.", 2 : "En este link se encuentra un cuadro de resumen del tema, ??Espero que te ayude! \n | https://imgur.com/33bcdvm", 3 : "Te dejo estos videos relacionados con tu consulta, ??Espero que te ayuden! \n | https://www.youtube.com/watch?v=XPVuEZlscf4 \n | https://www.youtube.com/watch?v=e_pkGReTvZ4"},
                        'el impacto demografico del cambio climatico' : {1 : "Las migraciones internacionales han aumentado considerablemente en las ??ltimas d??cadas, debido a las tasas demogr??ficas (alta tasa de fecundidad en los pa??ses empobrecidos y baja en los econ??micamente desarrollados); la presi??n migratoria desde los pa??ses del norte de ??frica hacia los del sur de Europa, desde Latinoam??rica hacia Estados Unidos, desde el este y el suroeste asi??tico hacia Norteam??rica y tal vez hacia Jap??n, y desde algunas de las antiguas rep??blicas sovi??ticas hacia Rusia. Pero los movimientos migratorios tambi??n tienen lugar dentro de los propios pa??ses. En Estados Unidos, los desplazamientos hacia las zonas costeras del Pac??fico. En China desde las zonas m??s ??ridas y pobres del interior a las provincias del litoral. En Espa??a ocurre algo similar hacia el litoral mediterr??neo. Con mucho, el fen??meno que se repite en todas las partes del mundo es la emigraci??n de las zonas rurales a las ??reas metropolitanas, as?? como la expansi??n de ??stas. ", 2 : "En este link se encuentra un cuadro de resumen del tema, ??Espero que te ayude! \n | https://imgur.com/QALMpBJ", 3 : "Te dejo este video relacionado con tu consulta, ??Espero que te ayude! \n | https://www.youtube.com/watch?v=Xe_k3_Ia93o"},
                        'el impacto economico del cambio climatico' : {1 : "Los asentamientos humanos, est??n siendo afectados por raz??n de: Cambios en la productividad, Cambios en las infraestructuras, cambios indirectos sociodemogr??ficos.El riesgo directo que afecta en m??s partes del mundo a los asentamientos humanos es el de inundaciones y movimientos de tierra: en las zonas costeras, por la subida del nivel del mar y mayor n??mero e intensidad de temporales y huracanes. Este riesgo es mayor para las poblaciones con menos recursos. La poblaci??n a tenido numerosas p??rdidas econ??micas a raz??n de la agravaci??n de temperatura, las inundaciones provocadas por lluvia y fen??menos naturales, adem??s de la urbanizaci??n que se llevo a cabo en zonas costeras provoco que haya muchas perdidas en el ??mbito econ??mico por culpa de los fen??menos naturales como ciclones, tsunamis, terremotos. La sobreexplotaci??n de la pesca a provocado tambi??n que haya proliferaciones de medusas en distintas ??reas del oc??ano, generando da??os por ejemplo en el turismo, que genera da??os econ??micos a las ciudades y/o pa??ses que las playas son su mayor fuerte de turismo.", 2 : "En este link se encuentra un cuadro de resumen del tema, ??Espero que te ayude! \n | https://imgur.com/Joe3cq2", 3 : "Te dejo estos videos relacionados con tu consulta, ??Espero que te ayuden! \n | https://www.youtube.com/watch?v=XVYt-Ssr_8E \n | https://www.youtube.com/watch?v=SoqWiCPploI"},
                        'el impacto en la organizacion de la sociedad' : {1 : "El cambio clim??tico est?? produciendo un impacto destacable en diversos aspectos de la organizaci??n social, as?? como en las normas y valores sociales, incluyendo la gobernabilidad de las sociedades y el desarrollo de los sistemas de democracia. ). Los riesgos biogeof??sicos que conllevan el cambio clim??tico afectan en mayor medida a los sectores m??s vulnerables de todas las sociedades (los pobres, los ancianos, los ni??os, las mujeres, los m??s d??biles???) ya que cuentan con menos recursos no s??lo econ??micos, sino tambi??n de informaci??n, de educaci??n e incluso del necesario ??nimo y autoestima para prevenir y mitigar los efectos del cambio clim??tico. En cuanto a las normas y valores sociales, como instrumentos de adaptaci??n social que son, son susceptibles de ser modificados por las mismas sociedades para preparar la acci??n social a los cambios necesarios. El Protocolo de Kioto para luchar contra el cambio clim??tico, por ejemplo, es de los pocos acuerdos mundiales existentes (firmado por m??s de 150 pa??ses) aun conllevando importantes compromisos econ??micos, este protocolo naci?? para poder reducir las emisiones de gases contaminantes en 5% en un periodo entre 2008 y 2012. Por otra parte, una consecuencia del cambio clim??tico est?? siendo la participaci??n de nuevos actores sociales en el proceso de discurso y legitimaci??n, destacando la creciente importancia del movimiento ecologista como actor social y una de las posibles consecuencias del cambio clim??tico es la ya visible tendencia a la privatizaci??n de los bienes comunes (el aire, por ejemplo).", 2 : "En este link se encuentra un cuadro de resumen del tema, ??Espero que te ayude! \n | https://imgur.com/7L520XK", 3 : "Te dejo este video relacionado con tu consulta, ??Espero que te ayude! \n | https://www.youtube.com/watch?v=85u07bxPrEs "},
                        'la solucion al cambio climatico' : {1 : "El cambio en el modelo energ??tico hegem??nico basado en combustibles f??siles contaminantes est?? en el centro de las soluciones, dirigidas a la construcci??n de otro modelo en donde las energ??as renovables (solar, e??lica, biomasa), limpias y sostenibles en el tiempo, tengan un papel protagonista. Tambi??n buscar el cumplimiento de los tratados y protocolos que se establecieron (por ejemplo el protocolo de Kioto) para que se pueda ir disminuyendo el da??o que le hacemos al ambiente y as?? generando que el cambio clim??tico no sea tan severo como viene siendo en los ??ltimos 70 a??os por la urbanizaci??n.", 2 : "En este link se encuentra un cuadro de resumen del tema, ??Espero que te ayude! \n | https://imgur.com/2DA57dO", 3 : "Te dejo este video relacionado con tu consulta, ??Espero que te ayude! \n | https://www.youtube.com/watch?v=0XZoz3J8jvQ"}
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
                                    'alternativa0' : "Hay dos caracter??sticas del cambio clim??tico actual que hace que los impactos biof??sicos y sociales globales asociados sean ??nicos en la historia del planeta", 
                                    'alternativa1' : "??Cu??les son los gases de efecto invernadero?", 
                                    'alternativa2' : "??Cu??nto aumento la temperatura global de la tierra debido al efecto invernadero en el ??ltimo siglo?"
                                  }, 
                    'pregunta2' : {
                                    'alternativa0' : "??Cu??les son las causantes del efecto invernadero?", 
                                    'alternativa1' : "??Cu??nto creci?? el consumo energ??tico mundial en las 2 ??ltimas d??cadas?", 
                                    'alternativa2' : "??Cu??nto se prev?? que aumentara el consumo energ??tico de aqu?? al 2030?"
                                  }, 
                    'pregunta3' : {
                                    'alternativa0' : "El cambio clim??tico es:", 
                                    'alternativa1' : "El cambio clim??tico afecta a???", 
                                    'alternativa2' : "??El cambio clim??tico tambi??n es consecuencia de la velocidad del cambio social en las sociedades contempor??neas que afecta?"
                                  }, 
                    'pregunta4' : {
                                    'alternativa0' : "El cambio clim??tico, ??perjudica y/o beneficia la salud humana?", 
                                    'alternativa1' : "Adem??s de olas de calor, las cuales provocaron la muerte de muchas personas. ??Que otras consecuencias hubo por el cambio clim??tico?", 
                                    'alternativa2' : "Potenciales beneficios para la salud causados por el cambio climatico: "
                                  }, 
                    'pregunta5' : {
                                    'alternativa0' : "Las migraciones internacionales:", 
                                    'alternativa1' : "Las migraciones dentro de un pais", 
                                    'alternativa2' : "El/los impactos inmediatos de las migraciones se manifiestan en:"
                                  }, 
                    'pregunta6' : {
                                    'alternativa0' : "La r??pida urbanizaci??n de zonas bajas costeras, tanto en el mundo econ??micamente desarrollado como en el mundo empobrecido, est?? produciendo:", 
                                    'alternativa1' : "??Que asentamientos humanos son mas vulnerables a los impactos del cambio climatico?",
                                    'alternativa2' : "Un nuevo factor asociado al cambio clim??tico seria???"
                                  },
                    'pregunta7' : {
                                    'alternativa0' : "??Que cambio en el modelo energetico hegemonico seria propicio como solucion al cambio climatico?",
                                    'alternativa1' : "??Cu??l es un acuerdo mundial para la lucha del cambio clim??tico?", 
                                    'alternativa2' : "??Cu??ntos pa??ses firmaron el acuerdo mundial para la lucha del cambio clim??tico?"
                                  },
                    'pregunta8' : {
                                    'alternativa0' : "??Cu??l ser??a una posible ayuda al problema?",
                                    'alternativa1' : "Seg??n El Libro Verde sobre la Energ??a de la Uni??n Europea (2006) documenta que se podr??a ahorrar energ??a. ??Cu??nto seria considerando el tipo de energ??a mencionado en el item 21?", 
                                    'alternativa2' : "Una soluci??n al problema del cambio clim??tico, seria cumplir con los objetivos que se tasaron en el protocolo de Kioto. ??Qu?? pa??s no lo cumpli???"
                                  }              
                  }
                  
opcionesExamen = {
                    'pregunta1' : {
                                    'alternativa0' : {'opcionA' : "Pasividad y debilidad", 'opcionB' : "Rapidez e intensidad", 'opcionC' : "Lento e intenso"}, 
                                    'alternativa1' : {'opcionA' : "Di??xido de carbono, Metano y ??xidos de nitr??geno", 'opcionB' : "Amoniaco, Benceno y ne??n", 'opcionC' : "Sulfuro de hidr??geno, Mon??xido de carbono"}, 
                                    'alternativa2' : {'opcionA' : "0, 5?? C", 'opcionB' : "0, 7?? C", 'opcionC' : "0, 9?? C"}
                                  }, 
                    'pregunta2' : {
                                    'alternativa0' : {'opcionA' : "El petr??leo, el gas natural y el carb??n", 'opcionB' : "El petroleo y el gas natural", 'opcionC' : "El carbon y el petroleo"}, 
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
                                    'alternativa1' : {'opcionA' : "Diseminaci??n de enfermedades y problemas respiratorios", 'opcionB' : "Aumento de c??ncer en la piel y lesiones oculares", 'opcionC' : "Todos los mencionados, entre otros"}, 
                                    'alternativa2' : {'opcionA' : "Inviernos menos fr??os en algunas regiones y el calentamiento y las sequ??as que en algunas zonas pueden disminuir el ciclo vital de los mosquitos y su periodo de transmisi??n", 'opcionB' : "Inviernos menos fr??os en algunas regiones", 'opcionC' : "El calentamiento y las sequ??as que en algunas zonas pueden disminuir el ciclo vital de los mosquitos y su periodo de transmisi??n"}
                                  }, 
                    'pregunta5' : {
                                    'alternativa0' : {'opcionA' : "Aumentaron", 'opcionB' : "Disminuyeron", 'opcionC' : "No se vieron afectadas"}, 
                                    'alternativa1' : {'opcionA' : "Aumentaron", 'opcionB' : "Disminuyeron", 'opcionC' : "No se vieron afectadas"}, 
                                    'alternativa2' : {'opcionA' : "La esfera econ??mica, las relaciones sociales, la cultura, la pol??tica nacional y las relaciones internacionales", 'opcionB' : "La esfera econ??mica", 'opcionC' : "La esfera econ??mica, las relaciones sociales y la cultura"}
                                  }, 
                    'pregunta6' : {
                                    'alternativa0' : {'opcionA' : "Inundaciones y movimientos de tierra", 'opcionB' : "Terremotos y tsunamis", 'opcionC' : "Erupciones y hambruna"}, 
                                    'alternativa1' : {'opcionA' : "Aquellos con poca diversificacion economica", 'opcionB' : "Aquellos con economias diversificadas", 'opcionC' : "Aquellos con poca diversificaci??n econ??mica, y en los que un elevado porcentaje de la renta proviene del sector primario sensible al clima"}, 
                                    'alternativa2' : {'opcionA' : "La proliferaci??n de hippocampus", 'opcionB' : "La proliferaci??n de cangrejos", 'opcionC' : "La proliferaci??n de medusas"}
                                  },
                    'pregunta7' : {
                                    'alternativa0' : {'opcionA' : "Continuar utilizando combustibles fosiles", 'opcionB' : "Aun no se conoce ningun modelo alternativo que no contribuya al cambio climatico", 'opcionC' : "Cambiar a un modelo donde las energias renovables, limpias, y sostenidas sean protagonistas"}, 
                                    'alternativa1' : {'opcionA' : "El Protocolo de Kioto", 'opcionB' : "El Protocolo Kansai", 'opcionC' : "El Protocolo Kisawa"}, 
                                    'alternativa2' : {'opcionA' : "50", 'opcionB' : "150", 'opcionC' : "Mas de 150"}
                                  },
                    'pregunta8' : {
                                    'alternativa0' : {'opcionA' : "Energias renovables", 'opcionB' : "Energia no renovables", 'opcionC' : "Ninguna de las anteriores"}, 
                                    'alternativa1' : {'opcionA' : "20 % del consumo de energ??a actual.", 'opcionB' : "10% del consumo de energ??a actual.", 'opcionC' : "30 % del consumo de energ??a actual."}, 
                                    'alternativa2' : {'opcionA' : "Estados Unidos y Espa??a", 'opcionB' : "Canad?? y Jap??n", 'opcionC' : "Todas las anteriores"}
                                  }              
                 }
respuestasExamen = {
                        'pregunta1' : {
                                        'alternativa0' : "Rapidez e intensidad", 
                                        'alternativa1' : "Di??xido de carbono, Metano y ??xidos de nitr??geno", 
                                        'alternativa2' : "0, 7?? C"
                                      }, 
                        'pregunta2' : {
                                        'alternativa0' : "El petr??leo, el gas natural y el carb??n", 
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
                                        'alternativa2' : "Inviernos menos fr??os en algunas regiones y el calentamiento y las sequ??as que en algunas zonas pueden disminuir el ciclo vital de los mosquitos y su periodo de transmisi??n"
                                      }, 
                        'pregunta5' : {
                                        'alternativa0' : "Aumentaron", 
                                        'alternativa1' : "Disminuyeron", 
                                        'alternativa2' : "La esfera econ??mica, las relaciones sociales, la cultura, la pol??tica nacional y las relaciones internacionales"
                                      }, 
                        'pregunta6' : {
                                        'alternativa0' : "Inundaciones y movimientos de tierra", 
                                        'alternativa1' : "Aquellos con poca diversificaci??n econ??mica, y en los que un elevado porcentaje de la renta proviene del sector primario sensible al clima", 
                                        'alternativa2' : "La proliferaci??n de medusas"
                                      },
                        'pregunta7' : {
                                        'alternativa0' : "Cambiar a un modelo donde las energias renovables, limpias, y sostenidas sean protagonistas", 
                                        'alternativa1' : "El Protocolo Kioto", 
                                        'alternativa2' : "Mas de 150"
                                      },
                        'pregunta8' : {
                                        'alternativa0' : "Energias renovables", 
                                        'alternativa1' : "20 % del consumo de energ??a actual.", 
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
             correccion['devolucion'] = "??Felicitaciones " + alum + "! ??Aprobaste la evaluacion!" + " Pero ojo pero un punto fue de concepto, por tu participacion, ??a estudiar un poco mas!"
       else:
            if correccion['cont'] == CANTIDAD_PREGUNTAS_EXAMEN-2 and buenConcepto(alum) == False:
              correccion['devolucion'] = "No te desanimes " + alum + ", a seguir estudiando."
            else:
                if correccion['cont'] >= CANTIDAD_PREGUNTAS_EXAMEN-1: 
                   alumnos[alum]['examenes aprobados'] += 1
                   correccion['devolucion'] = "??Felicitaciones " + alum + "! ??Aprobaste la evaluacion!"
    alumnos[alum]['promedio errores examen'] += ((CANTIDAD_PREGUNTAS_EXAMEN - correccion['cont']) / (alumnos[alum]['examenes intentados'] + (alumnos[alum]['examenes intentados'] - 1)))
    return correccion

def corregirEvaluacionTema(alum, examen, rta1, rta2, rta3):
    correccion = corregirRespuestas([rta1, rta2, rta3], examen)
    if correccion['cont'] == CANTIDAD_PREGUNTAS_EXAMEN_TEMA:
        correccion['devolucion'] = "??Felicitaciones " + alum + "! ??Aprobaste la mini evaluacion!"
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
    return {'message' : "??Un gusto " +  alum + "!"}

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