var myform = $("form#portContactForm");
myform.submit(function(event){
	event.preventDefault();

  // Change to your service ID, or keep using the default service
  var service_id = "default_service";
  var template_id = "portfolio_contact_form";

  myform.find("button").text("Sending...");
  emailjs.sendForm(service_id,template_id,"portContactForm")
  	.then(function(){ 
        $(".contact-tagline").html("Sent! Thank you!");
        myform.find("button").text("Send");
    }, function(err) {
        $(".contact-tagline").html("Yikes...Send email failed!\r\n Response:\n " + JSON.stringify(err));
        myform.find("button").text("Send");
    });
  return false;
});


<form id="portContactForm" method="post">
            <div class="name-email">
                <input type="text" name="from_name" placeholder="Name" required/>
                <input type="email" name="from_email" placeholder="Email" required/>
            </div>
            <textarea name="message_html" id="messageBox" cols="20" rows="5" placeholder="Message" required></textarea>
            <button class="send">Send</button>
        </form>