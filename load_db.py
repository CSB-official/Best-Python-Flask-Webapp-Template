from models import *

# DATA LOADERS
#############################################################################

# Creates a new local database if it doesnt already exist
def create_db():
    db.create_all()
    db.session.commit()
    return "load successful"

# Creates DB structure from models.py
def load_tasks():

    from time import time
    from app import db
    
    print('')
    print('')
    print('')
    print('********************* STARTING SPECIFIED LOAD TASKS *********************')

    t = time()
    
    db.drop_all()
    db.session.commit()
    create_db()
    db.session.close()


    print('********************* LOAD TASKS COMPLETE *********************')
    print("Total elapsed time: " + str(time() - t) + " s.")
    print('')
    print('')
    print('')
