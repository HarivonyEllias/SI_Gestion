CREATE  database si_gestion;
\c si_gestion;

CREATE TABLE infosociete (
    idsociete serial primary key,
    nom VARCHAR(255),
    objet VARCHAR(255),
    siege VARCHAR(255),
    adresse_exploitation VARCHAR(255),
    dirigeant VARCHAR(255),
    date_creation DATE,
    identite_fiscale VARCHAR(255),
    numero_statistique VARCHAR(255),
    numero_registre_commerce VARCHAR(255),
    status VARCHAR(255),
    devise_compte VARCHAR(255)
);

