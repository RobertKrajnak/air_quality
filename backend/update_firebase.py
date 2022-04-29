import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("air-quality-87493-firebase-adminsdk-4p59b-4a668c76cb.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://air-quality-87493.firebaseio.com/'
})

def update_firebase_skeleton():
    db.reference('record/push_9').update(db.reference('record/push_8').get())
    db.reference('record/push_8').update(db.reference('record/push_7').get())
    db.reference('record/push_7').update(db.reference('record/push_6').get())
    db.reference('record/push_6').update(db.reference('record/push_5').get())
    db.reference('record/push_5').update(db.reference('record/push_4').get())
    db.reference('record/push_4').update(db.reference('record/push_3').get())
    db.reference('record/push_3').update(db.reference('record/push_2').get())
    db.reference('record/push_2').update(db.reference('record/push_1').get())
    db.reference('record/push_1').update(db.reference('record/push_0').get())