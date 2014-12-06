$("#password").keyup(function () {
    validate();
});

$("#password_confirmation").keyup(function (){
    validate();
});

function validate(){
    var pass = $("#password");
    var pass_confirm = $("#password_confirmation");
    if (pass_confirm.val() != pass.val()) {
        pass.removeClass("correct-password");
        pass_confirm.removeClass("correct-password");
        pass.addClass("incorrect-password");
        pass_confirm.addClass("incorrect-password");
        $(".pass-are-different").css("visibility", "visible");
    }
    else {
        pass.removeClass("incorrect-password");
        pass_confirm.removeClass("incorrect-password");
        pass.addClass("correct-password");
        pass_confirm.addClass("correct-password");
        $(".pass-are-different").css("visibility", "hidden");
    }
}