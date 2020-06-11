"use strict";


var AgreeCalle = function () {

    var _initialize = function () {
        $("#filter_municipios").on("keyup", function() {
            var value = $(this).val().toLowerCase();
                $("#id_municipios span").filter(function() {
                $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
        });
        $("#check_all_municipios").on("click", function(){
            if ($("#check_all_municipios").prop('checked'))
                $("input[name='municipios']").attr('checked', true);
            else
                $("input[name='municipios']").attr('checked', false);
        });
        $('#form_calle').on('submit', function(event){
            event.preventDefault();
            //console.log("form submitted!")  // sanity check
            if (!$('#form_calle').valid())
                return;
            create_post();
        });

        // This function gets cookie with a given name
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');

        /*
        The functions below will create a header with csrftoken
        */

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        function sameOrigin(url) {
            // test that a given url is a same-origin URL
            // url could be relative or scheme relative or absolute
            var host = document.location.host; // host + port
            var protocol = document.location.protocol;
            var sr_origin = '//' + host;
            var origin = protocol + sr_origin;
            // Allow absolute or scheme relative URLs to same origin
            return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                // or any other URL that isn't scheme relative or absolute i.e relative.
                !(/^(\/\/|http:|https:).*/.test(url));
        }

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                    // Send the token to same-origin, relative URLs only.
                    // Send the token only if the method warrants CSRF protection
                    // Using the CSRFToken value acquired earlier
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        function create_post() {

            let form_data = $("#form_calle").serialize();
            $.ajax({
                url : "/nomenclador/new_calle/", // the endpoint
                type : "POST", // http method
                data : form_data,
                success : function(json) {
                    $('#id_nombre').val(''); // remove the value from the input
                    let id_select_element = $("#selected[type='hidden']").val();
                    //console.log("success"); // another sanity check
                    let mun_select = $(':not(#form_calle) select[id$=municipio]');
                    //console.log(mun_select);
                    mun_select[0].selectize.setValue(mun_select[0].selectize.getValue());
                    $("#"+id_select_element)[0].selectize.on('load', function() {
                        $("#"+id_select_element)[0].selectize.setValue(json.id);
                    });
                    //setTimeout( function () {$("#"+id_select_element)[0].selectize.setValue(json.id);}, 1500);
                    $('#close_md').click();
                },
                error : function(xhr,errmsg,err) {
                    $('#results').html("<div class='alert-box alert radius' data-alert>Oops! Hemos encontrado un error: "+errmsg+
                        " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                      console.log(xhr);
                    toastr.error(xhr.responseJSON.errmsg.nombre[0], '<h3>Error</h3>');
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });

        }
    };
    return {
        init: function () {
            _initialize();
        }
    }
}();
$(document).ready(function(){

});

