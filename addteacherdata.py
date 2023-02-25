import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://live-attendance-system-default-rtdb.firebaseio.com/"
})

ref = db.reference('Teachers')

data = {
    "2017666":
        {
            "name": "Saumya deep rawat",
            "major": "Computer science",
            "uid":"2017666",
            "Course":"601",
            "starting_year": 2020,
            "Experience": 7,
        },
"2017636":
        {
            "name": "Arunima",
            "major": "Computer science",
            "uid":"2017636",
            "Course":"602",
            "starting_year": 2020,
            "Experience": 7,
        },
"2017631":
        {
            "name": "Aarti",
            "major": "Computer science",
            "uid":"2017631",
            "Course":"603",
            "starting_year": 2020,
            "Experience": 7,
        },
"2017970":
        {
            "name": "Shruti",
            "major": "Computer science",
            "uid":"2017970",
            "Course":"604",
            "starting_year": 2020,
            "Experience": 7,
        }
}

for key, value in data.items():
    ref.child(key).set(value)