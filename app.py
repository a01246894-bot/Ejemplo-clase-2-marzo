function onFormSubmit(e)
{
var respuestas = e.response.getItemResponses();
var nombre = respuestas[0].getResponse(); //Primer campo
var apellido = respuestas[1].getResponse(); //Segundo campo
var data = {
nombre: nombre, //Base de Datos : variable JS
apellido: apellido
};
var options = {
method: "post",
contentType: "application/json",
payload: JSON.stringify(data)
};
UrlFetchApp.fetch(
"https://api/formulario", //URL de la API a generar. Se puede dejar
);
}
