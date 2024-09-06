import uuid
import bcrypt
import sqlite3

def get_number_users():
    conn = connect_users_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    number_users = cursor.fetchone()[0]
    conn.close()
    return number_users

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def generate_unique_uuid(cursor):
    while True:
        new_uuid = str(uuid.uuid4())
        cursor.execute("SELECT 1 FROM users WHERE userId = ?", (new_uuid,))
        if not cursor.fetchone():
            return new_uuid

def connect_users_db():
    conn = sqlite3.connect('users.db')
    return conn

def connect(uuid):
    conn = sqlite3.connect('tables/' + uuid + '.db')
    return conn

def insert_user(username, password):
    # THIS FUNCTION IS FOR THE CREATION OF A NEW SQLITE DATABASE INSTANCE FOR EACH USER
    # PLEASE DO NOT ATTEMPT TO EXPLIOT THIS FUNCTION. IT IS NOT RELATED TO THE CHALLENGE.
    
    usersDb = connect_users_db()
    cursor = usersDb.cursor()

    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        return False, ("Username already taken",)
    uuid = generate_unique_uuid(cursor)
    hashed_password = hash_password(password)
    cursor.execute("INSERT INTO users (uuid, username, password) VALUES (?, ?, ?)", (uuid, username, hashed_password))
    user_id = cursor.lastrowid
    usersDb.commit()
    usersDb.close()

    return True, (user_id,uuid,username)
    
def create_user(user,password):
    # THIS FUNCTION IS FOR THE CREATION OF A NEW SQLITE DATABASE INSTANCE FOR EACH USER
    # PLEASE DO NOT ATTEMPT TO EXPLIOT THIS FUNCTION. IT IS NOT RELATED TO THE CHALLENGE.
    
    success, data = insert_user(user,password)
    if not success:
        return False,data
    user_id,uuid,user = data
    sqlFile = open('sql/create_table.sql', 'r')
    sql = sqlFile.read()
    sqlFile.close()
    conn = connect(uuid)
    conn.executescript(sql)
    sql = "INSERT INTO users (userId,username) VALUES (?,?)"
    conn.execute(sql,(user_id,user))
    conn.commit()
    conn.close()
    return True, (user_id,uuid,user)

def getForms(uuid):
    conn = connect(uuid)
    cursor = conn.cursor()
    cursor.execute("SELECT `formId`,`formName`,`formDescription`,`formLink`,`username` FROM forms LEFT JOIN users ON forms.creatorId = users.userId")
    forms = cursor.fetchall()
    conn.close()
    return forms

def getUserIfExists(username,password):
    usersDb = connect_users_db()
    cursor = usersDb.cursor()
    cursor.execute("SELECT userId,uuid,password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if not result:
        return (False,("User not found",))
    userId,uuid,password = result
    usersDb.close()
    if not bcrypt.checkpw(password, password):
        return (False,("Invalid password",))
    return (True,(userId,uuid,username))

def getUserByUserId(userId):
    usersDb = connect_users_db()
    cursor = usersDb.cursor()
    cursor.execute("SELECT uuid,username FROM users WHERE userId = ?", (userId,))
    result = cursor.fetchone()
    if not result:
        return (False,("User not found",))
    uuid,username = result
    usersDb.close()
    return (True,(userId,uuid,username))