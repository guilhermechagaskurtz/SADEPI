function mostra_esconde_empresa_instituicao(){
    if($('#id_programa').val()){
        $.ajax({
            type: 'POST',
            url: $("#url_ajax_regra_campo_empresa_instituicao").val(),
            data: {
                'programa_id': $('#id_programa').val()
            },
            success: function (resposta) {
                if(resposta.obriga_empresa){
                    $('#area_empresa').fadeIn();
                }else{
                    $('#area_empresa').fadeOut();
                    $('#id_nome_empresa').val('');
                    $('#id_contato_empresa').val('');
                }

                if(resposta.obriga_instituicao){
                    $('#area_instituicao_beneficiada').fadeIn();
                }else{
                    $('#area_instituicao_beneficiada').fadeOut();
                    $('#id_nome_instituicao_beneficiada').val('');
                    $('#id_programa_extensao').val('');
                    $('#id_contato_instituicao_beneficiada').val('');
                    $('#id_cnpj_instituicao_beneficiada').val('');
                }
            },
            error: function (resposta) {
                alert(resposta.responseJSON.erro);
            }
        });
    }
}

$(document).ready(function() {
    mostra_esconde_empresa_instituicao();

    $('#id_programa').on('change', function () {
        mostra_esconde_empresa_instituicao();
    });
});