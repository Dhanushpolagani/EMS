import pymysql

print("🔍 Testing PyMySQL connection...")

try:
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="Dhanush@123",
        database="event_management",
        port=3306
    )
    print("✅ PyMySQL connected successfully")
    conn.close()
except Exception as e:
    print("❌ PyMySQL error:", e)
