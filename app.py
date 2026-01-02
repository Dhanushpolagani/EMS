from flask import Flask, jsonify, redirect, render_template, request
from flask_cors import CORS

from db import get_connection, fetch_all_bookings

# 1️⃣ CREATE APP FIRST
app = Flask(__name__)
CORS(app)

# 2️⃣ HOME ROUTE

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

# 3️⃣ BOOK EVENT API
@app.route("/book-event", methods=["POST"])
def book_event():
    data = request.get_json()
    print("📦 Booking received:", data)

    try:
        phone = data["phone"].replace(" ", "")

        conn = get_connection()
        cursor = conn.cursor()

        # 1️⃣ Insert booking
        cursor.execute("""
            INSERT INTO bookings
            (event_name, customer_name, email, phone, event_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            data["event"],
            data["name"],
            data["email"],
            phone,
            data["date"]
        ))

        # 2️⃣ Insert admin notification
        message = f"New booking: {data['name']} booked {data['event']} on {data['date']}"

        cursor.execute("""
            INSERT INTO notifications (message)
            VALUES (%s)
        """, (message,))

        conn.commit()
        cursor.close()
        conn.close()

        print("🔔 Admin notified")
        return jsonify({"message": "Booking successful"})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": "Server error"}), 500
@app.route("/admin/notifications")
def admin_notifications():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM notifications
        ORDER BY created_at DESC
    """)
    notifications = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("admin_notifications.html", notifications=notifications)
@app.route("/admin/notifications/read/<int:notification_id>")
def mark_notification_read(notification_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE notifications SET is_read = TRUE WHERE notification_id = %s",
        (notification_id,)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("/admin/notifications")


@app.route("/bookings")
def bookings_page():
    event_name = request.args.get("event", "Unknown Event")
    return render_template("bookings.html", event_name=event_name)

@app.route("/admin/bookings")
def admin_bookings():
    bookings = fetch_all_bookings()
    return render_template("admin_bookings.html", bookings=bookings)
@app.route("/admin/notifications/unread-count")
def unread_notification_count():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM notifications WHERE is_read = FALSE"
        )
        count = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return jsonify({"count": count})

    except Exception as e:
        print("❌ ERROR in unread-count:", e)
        return jsonify({"count": 0})


# 6️⃣ RUN APP LAST
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
