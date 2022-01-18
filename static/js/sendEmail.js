/* Email sent to website developer's Gmail account
and page refreshes once email has been sent */
function sendMail(contactForm) {
    emailjs.send("service_d29ijgj","template_lbx3fth", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "gin_booking": contactForm.ginbooking.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
}