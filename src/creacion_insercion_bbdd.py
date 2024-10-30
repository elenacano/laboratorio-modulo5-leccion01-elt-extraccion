import psycopg2
from psycopg2 import OperationalError, errorcodes, errors

def establecer_conn(database_name, usuario, password, host="localhost"):
    """
    Establece una conexión a una base de datos de PostgreSQL.

    Params:
        - database_name (str): El nombre de la base de datos a la que conectarse.
        - postgres_pass (str): La contraseña del usuario de PostgreSQL.
        - usuario (str): El nombre del usuario de PostgreSQL.
        - host (str, opcional): La dirección del servidor PostgreSQL. Por defecto es "localhost".

    Returns:
        psycopg2.extensions.connection: La conexión establecida a la base de datos PostgreSQL.

    """

    # Crear la conexión a la base de datos PostgreSQL
    try:  
        conexion = psycopg2.connect(
            database = database_name,
            user = usuario,
            password = password,
            host = host,
            port = "5432")

        # Establecer la conexión en modo autocommit
        conexion.autocommit = True # No hace necesario el uso del commit al final de cada sentencia de insert, delete, etc.
        
        return conexion

    except OperationalError as e:
        if e.pgcode == errorcodes.INVALID_PASSWORD:
            print("La contraseña es erronea")
        elif e.pgcode == errorcodes.CONNECTION_EXCEPTION:
            print("Error de conexion")
        else:
            print(f"Ocurrió el error {e}")



def crear_db(database_name, usuario, password):
    # conexion a postgres
    conn = establecer_conn("postgres", usuario, password) # Nos conectamos a la base de datos de postgres por defecto para poder crear la nueva base de datos
    
    # creamos un cursor con la conexion que acabamos de crear
    cur = conn.cursor()
    
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (database_name,))
    
    # Almacenamos en una variable el resultado del fetchone. Si existe tendrá una fila sino será None
    bbdd_existe = cur.fetchone()
    
    # Si bbdd_existe es None, creamos la base de datos
    if not bbdd_existe:
        cur.execute(f"CREATE DATABASE {database_name};")
        print(f"Base de datos {database_name} creada con éxito")
    else:
        print(f"La base de datos ya existe")
        
    # Cerramos el cursor y la conexion
    cur.close()
    conn.close()


def dbeaver_commitmany(conexion, query, values):
    """
    Ejecuta múltiples consultas y realiza un commit de los cambios.

    Args:
        conexion (connection): Un objeto de conexión a la base de datos.
        query (str): La consulta SQL a ejecutar.
        *values: Los valores a incluir en la consulta.

    Returns:
        str: Un mensaje de confirmación después del commit.
    """
    cursor = conexion.cursor()
    cursor.executemany(query, values)
    conexion.commit()