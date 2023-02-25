import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://live-attendance-system-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
        "2017666":
            {
                "name": "Saumya Deep Rawat",
                "father name":"Dhan Singh Rawat",
                #"D.O.B":"2002-08-02",
                "major": "Computer science",
                "Enroll No":"GE-202017666",
                "starting_year": 2020,
                "CGPA":"8.92",
                "total_attendance": 7,
                "year": 3,
                "last_attendance_time": "2022-12-11 00:54:34"
            },
        "2017651":
                {
                    "name": "Lakshay Sharma",
                    "father name":"Sandeep Kumar Sharma",
                    "DOB": "2003-01-10",
                    "major": "Computer science",
                    "Enroll No":"GE-202017651",
                    "starting_year": 2020,
                    "CGPA":"9.23",
                    "total_attendance": 7,
                    "year": 3,
                    "last_attendance_time": "2022-12-11 00:54:34"
                },
        "2017639":
                {
                    "name": "Ayush Rawat",
                    "father name":"Surendra Singh Rawat",
                    "DOB":"2002-05-01",
                    "major": "Computer science",
                    "Enroll No":"GE-202017639",
                    "starting_year": 2020,
                    "CGPA":"9.01",
                    "total_attendance": 7,
                    "year": 3,
                    "last_attendance_time": "2022-12-11 00:54:34"
                },
        "2017662":
                {
                    "name": "Raju",
                    "father name":"",
                    "DOB":"2002-05-01",
                    "major": "Computer science",
                    "Enroll No":"GE-202017639",
                    "starting_year": 2020,
                    "CGPA":"9.01",
                    "total_attendance": 7,
                    "year": 3,
                    "last_attendance_time": "2022-12-11 00:54:34"
                }
}

for key, value in data.items():
    ref.child(key).set(value)