$("#id_password1").keyup(function () {
    validate();
});

$("#id_password2").keyup(function (){
    validate();
});

function validate(){
    var pass = $("#id_password1");
    var pass_confirm = $("#id_password2");
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