--==============================================================
-- DBMS name:      ANSI Level 2
-- Created on:     7/01/2024 5:10:18 p.�m.
--==============================================================

--==============================================================
-- Table: eventos
--==============================================================
create table eventos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre                 varchar(200)         not null,
puntos               numeric(12,2)        not null default 0,
descripcion          varchar(1000)        not null
);

--==============================================================
-- Table: rangos
--==============================================================
create table rangos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre               varchar(200)         not null,
control              integer              not null,
descripcion          varchar(1000)        not null
);

--==============================================================
-- Table: integrantes
--==============================================================
create table integrantes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre               varchar(200)         not null,
rango_id             integer              default null,
principal_id         integer              default null,
fechacreacion        date                 not null,
fechamodificacion    date                 default null,
foreign key (rango_id) references rangos (id) ON DELETE SET DEFAULT
);

--==============================================================
-- Table: asistencias
--==============================================================
create table asistencias (
id INTEGER PRIMARY KEY AUTOINCREMENT,
integrante_id       integer              not null,
evento_id           integer              default null,
fecha               date                 not null,
foreign key (integrante_id) references integrantes (id) ON DELETE CASCADE,
foreign key (evento_id) references eventos (id) ON DELETE SET DEFAULT
);

