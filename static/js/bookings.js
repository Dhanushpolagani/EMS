// ✅ Confirm that booking.js is loaded
//alert("ookings page loaded successfully");

// Get event name from URL
const params = new URLSearchParams(window.location.search);
const eventName = params.get("event");

// Show event name on booking page
const eventTitleElement = document.getElementById("eventName");
if (eventTitleElement && eventName) {
    eventTitleElement.innerText = "Booking for: " + eventName;
}

// Handle form submission
const bookingForm = document.getElementById("bookingForm");

if (!bookingForm) {
    console.error("❌ bookingForm not found in HTML");
} else {
    bookingForm.addEventListener("submit", function (e) {
        e.preventDefault();

        console.log("✅ Booking form submitted");

        // Collect form data
        const bookingData = {
            event: eventName || "Unknown Event",
            name: document.getElementById("name").value,
            email: document.getElementById("email").value,
            phone: document.getElementById("phone").value,
            date: document.getElementById("date").value
        };

        console.log("📦 Sending booking data:", bookingData);

        // Send data to backend
        fetch("http://127.0.0.1:5000/book-event", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(bookingData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error! Status: " + response.status);
            }
            return response.json();
        })
        
            .then(data => {
    alert("✅ Booking successful!");
    
    // ✅ Redirect to Flask route (NOT HTML file)
    window.location.href = "/bookings";
})

        
        .catch(error => {
            console.error("❌ Error sending booking:", error);
            alert("❌ Booking failed. Please try again.");
        });
    });
    // Function to submit booking
function submitBooking() {

    const eventName = document.getElementById("eventName").value;
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const date = document.getElementById("date").value;

    // 🔴 Basic Validation
    if (!name || !email || !phone || !date) {
        alert("Please fill all fields");
        return;
    }

    if (phone.length < 10) {
        alert("Enter valid phone number");
        return;
    }

    const bookingData = {
        event: eventName,
        name: name,
        email: email,
        phone: phone,
        date: date
    };

    fetch("/book-event", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(bookingData)
    })
    .then(response => response.json())
    .then(result => {
        alert(result.message);

        // Clear form after success
        document.getElementById("bookingForm").reset();
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Booking failed. Try again.");
    });
}
   function submitBooking() {
    console.log("🚀 submitBooking() called");

    const data = {
        event: document.getElementById("eventName").value,
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        date: document.getElementById("date").value
    };

    console.log("📤 Sending data:", data);

    fetch("/book-event", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        console.log("✅ Server response:", result);
        alert(result.message);
    })
    .catch(err => {
        console.error("❌ Fetch error:", err);
    });
 }
 
}
