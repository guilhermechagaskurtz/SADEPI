function carrega_select_programas(){
    if($('#id_edital').val()){
        $.ajax({
            type: 'POST',
            url: $("#url_ajax_carrega_select_programas").val(),
            data: {
                'edital_id': $('#id_edital').val()
            },
            success: function (resposta) {
                if(resposta.obriga_bolsista){
                    $('#area_bolsista').fadeIn();
                }else{
                    $('#area_bolsista').fadeOut();
                }
                $("#id_programa").find('option').remove();
                $.each(resposta.programas, function(key, programa){
                    $("#id_programa").append('<option value=' + programa.id + '>' + programa.sigla + '</option>');
                });
                let id_programa_inicial = $('#id_programa_inicial').val();
                if(id_programa_inicial){
                    $("#id_programa").val(id_programa_inicial);
                }
            },
            error: function (resposta) {
                alert(resposta.responseJSON.erro);
            }
        });
    }
}

$(document).ready(function() {
    carrega_select_programas();

    $('#id_edital').on('change', function () {
        carrega_select_programas();
    });
});