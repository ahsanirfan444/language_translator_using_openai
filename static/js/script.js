$(document).ready(function() {


    $("#SubmitForm").submit(function(e) {
        e.preventDefault();

        const fromText = $(".from-text").val();
        
        const fromLanguage = $(".from-language").val();
        const toLanguage = $(".to-language").val();

        if (fromText != ""){
            $.ajax({
                url: post_data_request,
                type: 'post',
                dataType: 'json',
                data:{
                    "csrfmiddlewaretoken": csrf_token,
                    "fromText":fromText,
                    "fromLanguage":fromLanguage,
                    "toLanguage":toLanguage
    
                },
                success: function(response) {
                    $("#output_text").text(response.data);
                }
            });

        }




       
    });

    const selectTags = document.querySelectorAll("select");

    selectTags.forEach((tag, id) => {
        for (let country_code in countries) {
            let selected = (id === 0 && country_code === "en-GB") || (id === 1 && country_code === "ur-PK") ? "selected" : "";
            let option = `<option ${selected} value="${country_code}">${countries[country_code]}</option>`;
            tag.insertAdjacentHTML("beforeend", option);
        }
    });
});
