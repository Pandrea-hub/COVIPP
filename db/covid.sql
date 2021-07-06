INSERT INTO rol_rol (id,name,editList) VALUES
(1, 'Enfermero', 1),
(2, 'Administrador', 1),
(3, 'Paciente', 0);

INSERT INTO type_place_typeplace (id,name) VALUES
(1,'Vaccination'),
(2,'Test_covid');

INSERT INTO place_place (id,title,draggable, fragment,longitude,latitude,type_place_id) VALUES
(1,'CC santa fe','0','Secretaria punto vacunacion','4.65156','-74.07454',1),
(2,'Parque colina','0','Secretaria punto vacunacion','4.72638','-74.06073',1),
(3,'Plaza americas','0','Secretaria punto vacunacion','4.61870','-74.13522',1),
(4,'Mallplaza NQS','0','Secretaria punto vacunacion','4.61922','-74.08651',1),
(5,'CC Paseo villa del rio','0','Secretaria punto vacunacion','4.59828','-74.15332',1),
(6,'CC bulevar niza','0','Secretaria punto vacunacion','4.71254','-74.07140',1),
(7,'CC dorado plaza','0','Secretaria punto vacunacion','4.6761485666017295', '-74.11964418008802',1),
(8,'CC avenida chile','0','Secretaria punto vacunacion','4.65788', '-74.05821',1),
(9,'CC metropolis','0','Secretaria punto vacunacion','4.68022', '-74.08217',1),
(10,'Biblioteca tintal','0','Secretaria punto vacunacion','4.6430946941687115', '-74.15496656632426',1),
(11,'CC BIMA','0','Secretaria punto vacunacion','4.806979767815015', '-74.03924502516671',1),
(12,'Plaza de los artesanos','0','Secretaria punto vacunacion','4.664120092116737', '-74.0859651184579',1),
(13,'CM ciudadela','0','colsubsidio punto vacunacion','4.72061532191227', '-74.11487415092404',1),
(14,'CM calle 26','0','colsubsidio punto vacunacion','4.6228402879687955', '-74.07768823714187',1),
(15,'CM plaza central','0','colsubsidio punto vacunacion','4.633064367939316', '-74.11546735191817',1),
(16,'Cafam floresta','0','colsubsidio test covid','4.684463799779508', '-74.07833257114834',2),
(17,'CC unicentro de occidente','0','colsubsidio test covid','4.723492006449618', '-74.11424951917326',2);


INSERT INTO contagion_type_contagiontype (id,name) VALUES
(1,'Case symptom'),
(2,'Case infection');



INSERT INTO gender_gender (id,name) VALUES
(1,'Male'),
(2,'Female'),
(3,'Other');


INSERT INTO vaccine_vaccine (id,name,days, number_doses) VALUES
(1,'Sinovac',28,2),
(2,'Pfizer',21,2),
(3,'Astrazeneca',90,2),
(4,'Janssen',0,1),
(5,'Moderna',28,2),
(6,'Sputnik V',90,2),
(7,'Sinopharm',0,1),
(8,'Novavax',28,2);

INSERT INTO vw_list_information


CREATE VIEW vw_list_information AS
SELECT
  DISTINCT
    LT.id AS id,
    PR.user_id AS user_id;
    V.days AS days,
    LT.date AS first_dose_date,
    DATE_ADD(LT.date ,INTERVAL 21 DAY) AS second_dose_date,
    U.first_name AS first_name,
    U.last_name AS last_name,
    TIMESTAMPDIFF(YEAR, PR.birth_date, CURDATE()) AS age,
    V.name AS vaccine_name,
    V.number_doses AS number_doses,
    LT.applied_doses AS applied_doses,
    P.title AS name_place
FROM
  list_information_listinformation AS LT
  JOIN vaccine_vaccine AS V ON V.id = LT.vaccine_id
  JOIN place_place AS P ON P.id = LT.place_id
  JOIN person_person AS PR ON PR.user_id = LT.person_id
  JOIN auth_user AS U ON U.id = PR.user_id
  JOIN gender_gender AS G ON G.id = PR.gender_id


CREATE VIEW vw_symptom_cases AS
SELECT
    DISTINCT
        PS.user_id AS id,
        CS.date AS first_day,
        DATE_SUB(CS.date, INTERVAL 6 DAY) AS contagion_day,
        DATE_ADD(CS.date,INTERVAL 8 DAY) AS not_contagion_day,
        DATE_ADD(CS.date, INTERVAL 14 DAY) AS not_covid,
        US.first_name AS first_name,
        US.last_name AS last_name
FROM cases_cases AS CS
    JOIN person_person AS PS ON PS.user_id = CS.person_id
    JOIN auth_user AS US ON US.id = PS.user_id
WHERE CS.contagion_type_id = 1



CREATE VIEW  vw_contagion_cases AS
SELECT
    DISTINCT
        PE.user_id AS id,
        CA.date AS firsts_day,
        DATE_ADD(CS.date, INTERVAL 4 DAY) AS infectious_day,
        DATE_ADD(CS.date,INTERVAL 6 DAY) AS symptom_day,
        DATE_ADD(CS.date, INTERVAL 13 DAY) AS not_infectious_day,
        DATE_ADD(CS.date, INTERVAL 26 DAY) AS free_covid,
        UR.first_name AS first_name,
        UR.last_name AS last_name
FROM cases_cases AS CA
    JOIN person_person AS PE ON PE.user_id = CA.person_id
    JOIN auth_user AS UR ON UR.id = PE.user_id
WHERE CA.contagion_type_id = 2



'id',
'days',
'first_dose_date',
'second_dose_date',
'first_name',
'last_name',
'age',
'vaccine_name',
'number_doses',
'applied_doses',
'name_place'