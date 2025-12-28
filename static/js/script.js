const events = [
    {
        title: "Wedding Ceremony",
        date: "2025-03-10",
        place: "Hyderabad",
        flow: [
            "Venue decoration and stage setup",
            "Bride & Groom entry",
            "Traditional rituals and ceremonies",
            "Photography & videography",
            "Lunch/Dinner arrangement for guests"
        ]
    },
    {
        title: "Birthday Party",
        date: "2025-04-05",
        place: "Bangalore",
        flow: [
            "Theme-based decoration",
            "Cake cutting ceremony",
            "Games and entertainment for kids",
            "Magic show / cartoon characters",
            "Snacks and return gifts"
        ]
    },
    {
        title: "Corporate Conference",
        date: "2025-05-20",
        place: "Chennai",
        flow: [
            "Conference hall setup",
            "Welcome speech and keynote sessions",
            "Product presentations",
            "Lunch and networking",
            "Closing ceremony"
        ]
    }
];

// 🔹 Book Event → user booking page
function bookEvent(eventTitle) {
    if (!eventTitle) {
        alert("Event not found");
        return;
    }
    window.location.href = `/bookings?event=${encodeURIComponent(eventTitle)}`;
}

// 🔹 View Bookings → admin page
function viewAdminBookings() {
    window.location.href = `/admin/bookings`;
}

const container = document.getElementById("event-container");

events.forEach(event => {
    const row = document.createElement("div");
    row.className = "event-row";

    row.innerHTML = `
        <div class="event-card">
            <h3>${event.title}</h3>
            <p><b>Date:</b> ${event.date}</p>
            <p><b>Location:</b> ${event.place}</p>
        </div>

        <div class="event-details">
            <h4>What will happen in this event?</h4>
            <ul>
                ${event.flow.map(step => `<li>${step}</li>`).join("")}
            </ul>

            <button onclick="bookEvent('${event.title}')">
                Book Event
            </button>

           
        </div>
    `;

    container.appendChild(row);
});
