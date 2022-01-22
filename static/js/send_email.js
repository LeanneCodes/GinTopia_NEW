// Email sent to developer's Gmail account using EmailJs
function sendMail(contactForm) {
    emailjs.send("service_d29ijgj","template_lbx3fth", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "gin_booking": contactForm.ginbooking.value
    })
    .then(
        function(response) {
            alert('Enquiry has been submitted!');
            console.log("SUCCESS", response);
        },
        function(error) {
            alert('Enquiry has failed to send. Check all fields have valid inputs.');
            console.log("FAILED", error);
        }
    );
    return false;
}