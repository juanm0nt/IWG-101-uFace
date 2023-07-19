import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("/Users/juanmonteverde/juanm0nt.dev/myProjects/uFace/serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL":"https://sistema-de-asistencia-dbed3-default-rtdb.firebaseio.com/"})


ref = db.reference("Students")

data = {
    "21833550-0":
        {
            "nombre": "Jorge Padilla",
            "carrera": "Telematica",
            "iniciante_year": 2023,
            "asistencia_total":0,
            "calidad_estudiante": "B",
            "year": 1,
            "fecha_ultima_asistencia": "2022-12-11 00:12:33"
        },
        "24450382-9":
        {
            "nombre": "Juan Monteverde",
            "carrera": "Telematica",
            "iniciante_year": 2023,
            "asistencia_total":0,
            "calidad_estudiante": "A",
            "year": 1,
            "fecha_ultima_asistencia": "2022-12-11 00:10:00"
        },
        "26385232-k":
        {
            "nombre": "Elon Musk",
            "carrera": "Fisica",
            "iniciante_year": 2023,
            "asistencia_total":0,
            "calidad_estudiante": "A+",
            "year": 1,
            "fecha_ultima_asistencia": "2022-12-11 00:12:33"
        },
        "18456739-3":
        {
            "nombre": "Nicolas Torres",
            "carrera": "Telematica",
            "iniciante_year": 2023,
            "asistencia_total":0,
            "calidad_estudiante": "A++",
            "year": 1,
            "fecha_ultima_asistencia": "2022-12-11 00:12:33"
        },
        "21453654-3":
        {
            "nombre": "Tomas Salinas",
            "carrera": "Telematica",
            "iniciante_year": 2023,
            "asistencia_total":0,
            "calidad_estudiante": "A",
            "year": 1,
            "fecha_ultima_asistencia": "2022-12-11 00:10:00"
        },
        "23564335-7":
        {
            "nombre": "Sebastian Orellana",
            "carrera": "Fisica",
            "iniciante_year": 2023,
            "asistencia_total":0,
            "calidad_estudiante": "C",
            "year": 1,
            "fecha_ultima_asistencia": "2022-12-11 00:12:33"
        },
        "21760484-2":
        {
            "nombre": "Nicolas Sepulveda",
            "carrera": "Telematica",
            "iniciante_year": 2023,
            "asistencia_total":0,
            "calidad_estudiante": "A+",
            "year": 1,
            "fecha_ultima_asistencia": "2022-12-11 00:12:33"
        },
        "21803608-2":
        {
            "nombre": "Enrique Manzano",
            "carrera": "Telematica",
            "iniciante_year": 2023,
            "asistencia_total":0,
            "calidad_estudiante": "A++",
            "year": 1,
            "fecha_ultima_asistencia": "2022-12-11 00:12:33"
        },
        "21634403-0":
        {
            "nombre": "Diego Villanueva",
            "carrera": "Telematica",
            "iniciante_year": 2023,
            "asistencia_total":0,
            "calidad_estudiante": "A++",
            "year": 1,
            "fecha_ultima_asistencia": "2022-12-11 00:10:00"
        },
        "21792548-7":
        {
            "nombre": "Gonzalo Valdivia",
            "carrera": "Fisica",
            "iniciante_year": 2023,
            "asistencia_total":0,
            "calidad_estudiante": "F",
            "year": 1,
            "fecha_ultima_asistencia": "2022-12-11 00:12:33"
        }
}

for key,value in data.items():
    ref.child(key).set(value)
    print("Datos Agregados")