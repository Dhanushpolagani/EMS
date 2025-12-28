import pymysql

def get_connection():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="Dhanush@123",
        database="event_management",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
def fetch_all_bookings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings ORDER BY created_at DESC")
    bookings = cursor.fetchall()
    cursor.close()
    conn.close()
    return bookings
