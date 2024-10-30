query_creation_comunidades = """
create table if not exists comunidades (
    id_ccaa INT primary key,
    nombre VARCHAR(300) unique not null
);
"""

query_creation_demanda = """
create table if not exists demanda (
    id_demanda serial primary key,
    id_ccaa INT not null,
    anio int not null,
    mes varchar(50) not null,
    valor float,
    foreign key (id_ccaa) references comunidades(id_ccaa) on delete restrict on update cascade
);
"""

query_creation_energia = """
create table if not exists energia (
    id_energia INT primary key,
    nombre VARCHAR(300) unique not null
);
"""

query_creation_generacion = """
create table if not exists generacion (
    id_generacion SERIAL primary key,
    id_ccaa INT not null,
    anio int not null,
    mes varchar(50) not null,
    id_energia INT not null,
    porcentaje float,
    valor float,
    foreign key (id_ccaa) references comunidades(id_ccaa) on delete restrict on update cascade,
    foreign key (id_energia) references energia(id_energia) on delete restrict on update cascade
);"""

query_creation_provincia = """
create table if not exists provincia (
    id_provincia INT primary key,
    nombre VARCHAR(300) unique not null,
    id_ccaa int not null,
    foreign key (id_ccaa) references comunidades(id_ccaa) on delete restrict on update cascade
);
"""

query_creation_edades = """
create table if not exists edades (
    id_edad INT primary key,
    nombre VARCHAR(300) unique not null
);
"""

query_creation_ramas = """
create table if not exists ramas (
    id_rama INT primary key,
    nombre VARCHAR(300) unique not null
);
"""

query_creation_pib_total = """
create table if not exists pib_total (
    id_pib_total SERIAL primary key,
    id_provincia INT not null,
    actividad varchar(50) not null,
    anio int not null,
    total float,
    foreign key (id_provincia) references provincia(id_provincia) on delete restrict on update cascade
);"""


query_creation_pib_ramas = """
create table if not exists pib_ramas (
    id_pib_rama SERIAL primary key,
    id_provincia INT not null,
    id_rama INT not null,
    anio int not null,
    total float,
    foreign key (id_provincia) references provincia(id_provincia) on delete restrict on update cascade,
    foreign key (id_rama) references ramas(id_rama) on delete restrict on update cascade
);"""

query_creation_poblacion = """
create table if not exists poblacion (
    id_poblacion SERIAL primary key,
    id_provincia INT not null,
    id_edad INT not null,
    espaniol_extranjero varchar(200) not null,
    sexo varchar(100) not null,
    anio int not null,
    total float,
    foreign key (id_provincia) references provincia(id_provincia) on delete restrict on update cascade,
    foreign key (id_edad) references edades(id_edad) on delete restrict on update cascade
);"""