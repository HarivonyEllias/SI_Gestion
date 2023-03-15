create table societe(
    id serial primary key,
    nom varchar(30),
    mdp varchar(30),
    directeur varchar(100),
    add_exploitation varchar(20),
    date_creation date,
    numero_fiscal varchar(9),
    numero_statistique varchar(9),
    numero_registre_commercial varchar(20),
    status varchar(20) 
);

create table codeJournal(
    id serial primary key,
    code varchar(10),
    nom varchar(20) 
);

create table compteGeneral(
    id serial primary key,
    numero_compte varchar(20),
    libelle varchar(20)
);

create table compteTier(
    id serial primary key,
    nom varchar(30),
    type varchar(30)
);

create table devise(
    id serial primary key,
    type varchar(20)
);