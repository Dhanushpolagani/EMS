from flask import Flask, jsonify, render_template, request
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
    print("🔥 POST /book-event HIT")

    try:
        data = request.get_json(force=True)
        print("📦 Data received:", data)

        phone = data["phone"].replace(" ", "")

        conn = get_connection()
        cursor = conn.cursor()

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

        conn.commit()
        cursor.close()
        conn.close()

        print("✅ BOOKING INSERTED")
        return jsonify({"message": "Booking saved successfully"})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": "Server error"}), 500

@app.route("/bookings")
def bookings_page():
    event_name = request.args.get("event", "Unknown Event")
    return render_template("bookings.html", event_name=event_name)

@app.route("/admin/bookings")
def admin_bookings():
    bookings = fetch_all_bookings()
    return render_template("admin_bookings.html", bookings=bookings)


# 6️⃣ RUN APP LAST
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
