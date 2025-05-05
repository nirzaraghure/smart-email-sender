document.getElementById("emailForm").addEventListener("submit", async (e) => {
    e.preventDefault();  // Prevents the default form submission behavior
  
    // Get form field values
    const to = document.getElementById("to").value;
    const subject = document.getElementById("subject").value;
    const message = document.getElementById("message").value;
  
    // Update status to indicate email is being sent
    document.getElementById("status").innerText = "Sending like a human...";

    try {
        // Make the POST request to the backend
        const response = await fetch("http://127.0.0.1:5000/send", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ to, subject, message }) // Sending the data
        });
    
        // Parse the JSON response
        const result = await response.json();

        // Check if email was sent successfully
        if (result.status === "sent") {
            document.getElementById("status").innerText = "Email sent successfully!";
        } else {
            document.getElementById("status").innerText = "Failed to send email.";
        }
    } catch (error) {
        // Handle errors, such as network issues
        document.getElementById("status").innerText = "Error sending email. Please try again.";
        console.error("Error:", error);
    }
});
