import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('eucalyptus-73f89-firebase-adminsdk-oxqlt-26fb5c04cb.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred,
                            {'databaseURL': "https://eucalyptus-73f89-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference('/eucalyptus')


def update_load(spring_name: str, new_count: int):
    ref = db.reference(f'/eucalyptus/springs/{spring_name}')
    ref.update({'load_level': new_count})

def get_loads(spring_name: str):
    ref = db.reference(f'/eucalyptus/springs/{spring_name}/load_level')
    return ref.get()

def get_location(spring_name: str):
    ref = db.reference(f'/eucalyptus/springs/{spring_name}/location')
    return ref.get()

print(get_location("lifta"))


