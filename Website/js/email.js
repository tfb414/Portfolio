var myform = $("#contactForm");
myform.submit(function(event){
    console.log('did we make it?')
	event.preventDefault();

  // Change to your service ID, or keep using the default service
  var service_id = "default_service";
  var template_id = "temp_1";

  emailjs.sendForm(service_id,template_id, "contactForm")
  	.then(function(){ 
        $("#sendmessage").css("display", "block");
        // myform.find("button").text("Send");
        $('[data-target="emailForm"]').trigger("reset");
        
    }, function(err) {
        $("#sendmessage").css("display", "block");
        $("#sendmessage").html("oopsie poopsie, it didn't work");
        $("#sendmessage").css("display", "inline");
        
    });
  return false;
});


