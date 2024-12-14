import sqlite3
import time

def get_connection():
    """Returns a new connection to the SQLite database."""
    return sqlite3.connect('skillmatch.db')

def connect_db():
    """Returns a new connection to the SQLite database (same as get_connection)."""
    return sqlite3.connect('skillmatch.db')

def get_profiles_by_skill_tag(skill_tag):
    """Fetches user profiles based on a selected skill tag (specialty)."""
    connection = get_connection()
    cursor = connection.cursor()
    # Query to find users who match the skill tag (specialty)
    cursor.execute(''' 
        SELECT * FROM users WHERE specialty = ? 
    ''', (skill_tag,))
    profiles = cursor.fetchall()
    connection.close()
    
    # Convert each profile tuple to a dictionary for easier access
    profiles_dict = []
    for profile in profiles:
        profiles_dict.append({
            'id': profile[0],
            'first_name': profile[1],
            'last_name': profile[2],
            'specialty': profile[3],
            'skills': profile[4],
            'skill_level': profile[5],
            'username': profile[6],
            'password': profile[7],
            'credits': profile[8]
        })
    return profiles_dict

def create_tables():
    """Creates necessary tables in the database if they don't already exist."""
    connection = get_connection()
    cursor = connection.cursor()
    
    # Create the 'users' table if it doesn't already exist
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            specialty TEXT NOT NULL,
            skills TEXT NOT NULL,
            skill_level TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            credits INTEGER DEFAULT 0
        )
    ''')

def get_all_transactions():
    """Fetches all transaction records from the database, including user details."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(''' 
        SELECT st.transaction_id, st.user_id, st.traded_skill, st.transaction_date, u.first_name, u.last_name 
        FROM skills_transactions st 
        JOIN users u ON st.user_id = u.id
    ''')
    transactions = cursor.fetchall()
    connection.close()
    return transactions

def register_user(first_name, last_name, specialty, skill, skill_level, username, password):
    """Registers a new user in the database."""
    conn = sqlite3.connect('skillmatch.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute(''' 
            INSERT INTO users (first_name, last_name, specialty, skills, skill_level, username, password) 
            VALUES (?, ?, ?, ?, ?, ?, ?) 
        ''', (first_name, last_name, specialty, skill, skill_level, username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"Error: Username {username} already exists.")
        return False
    finally:
        conn.close()

def delete_all_users():
    """Deletes all users from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM users")
        conn.commit()
        print("All users have been deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting all users: {e}")
    finally:
        conn.close()

def authenticate_user(username, password):
    """Authenticates a user by checking their username and password."""
    conn = sqlite3.connect('skillmatch.db')
    cursor = conn.cursor()
    cursor.execute(''' 
        SELECT * FROM users WHERE username = ? AND password = ? 
    ''', (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return {
            'id': user[0],
            'first_name': user[1],
            'last_name': user[2],
            'specialty': user[3],
            'skills': user[4],
            'username': user[5],
            'password': user[6],
            'skill_level': user[7],
            'credits': user[8]
        }
    return None

def get_all_users():
    """Fetches all users from the database."""
    connection = sqlite3.connect('skillmatch.db')
    cursor = connection.cursor()
    
    # Execute SQL query to get all users
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()
    
    # Close the connection
    connection.close()
    return all_users

logged_in_user = None  # Global variable to store logged-in user info

def delete_user(user_id):
    """Deletes a user by their ID from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        # Delete by user_id to ensure uniqueness
        cursor.execute('''DELETE FROM users WHERE id = ?''', (user_id,))
        conn.commit()
        
        # Verify the deletion
        cursor.execute('''SELECT * FROM users WHERE id = ?''', (user_id,))
        user = cursor.fetchone()
        
        if user is None:
            print(f"User with ID {user_id} has been deleted.")
        else:
            print(f"Error: User with ID {user_id} still exists.")
        
        # Reset the logged-in user after deletion
        global logged_in_user
        logged_in_user = None  # Reset the logged-in user
        
    except sqlite3.Error as e:
        print(f"Error deleting user with ID {user_id}: {e}")
    finally:
        conn.close()

def get_users_by_criterion(self, criterion, value):
    """Fetches users based on a specific criterion (e.g., specialty, username)."""
    query = f"SELECT * FROM users WHERE {criterion} = ?"
    params = (value,)
    self.cursor.execute(query, params)
    return self.cursor.fetchall()

def update_credits(user_id, credits):
    """Updates the user's credits in the database."""
    connection = get_connection()
    cursor = connection.cursor()
    try:
        # Update the credits in the database
        cursor.execute("UPDATE users SET credits = ? WHERE id = ?", (credits, user_id))
        connection.commit()  # Ensure the update is committed

        # Fetch and print the updated credits to confirm the change
        cursor.execute("SELECT credits FROM users WHERE id = ?", (user_id,))
        updated_credits = cursor.fetchone()
        print(f"Updated credits: {updated_credits[0]}")  # Print the updated credits value
        
    except sqlite3.Error as e:
        print(f"Error updating credits: {e}")
    finally:
        connection.close()
