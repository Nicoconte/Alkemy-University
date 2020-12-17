const hideError = () => {
    if($("#span-error-msg").text() != "") {
        setTimeout(() => {
            $("#span-error-msg").fadeOut("slow", () => {
                $("#span-error-msg").text("")
            })
        }, 1000)    
    }
}

const hideAlertMessage = () => {
    setTimeout(() => {
        $("#alert-message").fadeOut("slow");
    }, 1000)
}

const toggleNavbar = () => {
    
    toggleAction = 1

    $("#burguer-btn").click(() => {
        if (toggleAction % 2) {
            $(".dashboard-lat-container").css("width", "5%")
            $(".dashboard-content-container").css("width", "95%");

            setTimeout(() => {
                $(".text-button").css("display", "none")
                $(".button-icon").css("width", "100%")
            }, 200)


        } else {
            $(".dashboard-lat-container").css("width", "17%")
            $(".dashboard-content-container").css("width", "83%")

            setTimeout(() => {
                $(".text-button").css("display", "flex")
                $(".button-icon").css("width", "30%")
            }, 200)

        }
        toggleAction++;
        console.log("click")
    })

}

const initTooltip = () => {
    $('[data-toggle="tooltip"]').tooltip()
}

$(document).ready(() => {
    console.log("Esto funciona");
    hideError();
    hideAlertMessage();
    toggleNavbar();
    initTooltip();
});