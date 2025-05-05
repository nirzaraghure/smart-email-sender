document.getElementById("emailForm").addEventListener("submit", async (e) => {
    e.preventDefault();  // Prevents the default form submission behavior

    // Get form field values
    const to = document.getElementById("to").value;
    const subject = document.getElementById("subject").value;
    const message = document.getElementById("message").value;

    // Update status to indicate email is being sent
    document.getElementById("status").innerText = "Sending like a human...";

    try {
        // ✅ Update the backend URL to your deployed Render backend
        const response = await fetch("https://smart-email-backend-qtel.onrender.com/send", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ to, subject, message }) // Sending the data
        });

        const result = await response.json();

        if (result.status === "sent") {
            document.getElementById("status").innerText = "Email sent successfully!";
        } else {
            document.getElementById("status").innerText = "Failed to send email.";
        }
    } catch (error) {
        document.getElementById("status").innerText = "Error sending email. Please try again.";
        console.error("Error:", error);
    }
});
