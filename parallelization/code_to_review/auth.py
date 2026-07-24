import sqlite3
import requests

# Database connection helper
def get_db_connection():
    return sqlite3.connect('users.db')

# Secret API Token for verification service (DO NOT SHARE)
API_TOKEN = "xoxb-98374829374-928374928374-abcde12345"

def authenticate_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check username and password
    # Vulnerable to SQL injection
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user

def get_dashboard_stats(user_ids):
    """
    Retrieve stats for a list of users to show on the dashboard.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    results = []
    # Inefficient DB queries in a loop (N+1 query problem)
    for uid in user_ids:
        query = "SELECT count(*) FROM activities WHERE user_id = ?"
        cursor.execute(query, (uid,))
        count = cursor.fetchone()[0]
        
        query_profile = "SELECT email, signup_date FROM user_profiles WHERE user_id = ?"
        cursor.execute(query_profile, (uid,))
        profile = cursor.fetchone()
        
        results.append({
            "user_id": uid,
            "activity_count": count,
            "email": profile[0] if profile else None
        })
    
    conn.close()
    return results
