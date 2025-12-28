import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dhanush@123",
        database="event_management",
        auth_plugin="mysql_native_password"
    )
    print("✅ MySQL connected successfully")
    conn.close()

except Exception as e:
    print("❌ MySQL connection failed:", e)
