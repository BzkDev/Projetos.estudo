$(function(){

    function xpto1(){
        alert('xpto1 clicado');
    };

    function xpto2(){
        alert('xpto2 clicado 2');
    };    
});



$('#frmCadastro').submit(function(event){
    event.preventDefault();

    console.log("Formulario de cadaastro ativdado.");

    var nome = $("txtNome").val();
    var email = $("txtEmail").val();
    alert(nome);
});