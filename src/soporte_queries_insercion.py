query_carga_comunidades = """
INSERT INTO comunidades (id_ccaa, nombre) VALUES (%s, %s)""" # insertar valores %s es como un formato. como un argumento

query_carga_demanda = """INSERT INTO demanda 
                        (id_ccaa,
                        anio,
                        mes,
                        valor) 
                        VALUES (%s, %s, %s, %s)""" 


query_carga_energia = """
INSERT INTO energia (id_energia, nombre) VALUES (%s, %s)"""


query_carga_generacion = """INSERT INTO generacion 
                        (id_ccaa,
                        anio,
                        mes,
                        id_energia,
                        porcentaje,
                        valor) 
                        VALUES (%s, %s, %s, %s, %s, %s)""" 

query_carga_edades = """
INSERT INTO edades (id_edad, nombre) VALUES (%s, %s)"""

query_carga_ramas = """
INSERT INTO ramas (id_rama, nombre) VALUES (%s, %s)"""

query_carga_pib_total = """INSERT INTO pib_total 
                        (id_provincia,
                        actividad,
                        anio,
                        total) 
                        VALUES (%s, %s, %s, %s)""" 

query_carga_pib_ramas = """INSERT INTO pib_ramas
                        (id_provincia,
                        id_rama,
                        anio,
                        total) 
                        VALUES (%s, %s, %s, %s)""" 

query_carga_poblacion = """INSERT INTO poblacion
                        (id_provincia,
                        id_edad,
                        espaniol_extranjero,
                        sexo,
                        anio,
                        total) 
                        VALUES (%s, %s, %s, %s, %s, %s)""" 