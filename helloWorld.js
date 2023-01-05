//Ejemplo de codigo Javascirpt para mi pagina web
var my_name = "Nicolas";
var apellido = "Aragon";

alert("Hola " + my_name + apellido);


var tweet = prompt("Compose your tweet");

var my_nameLength = my_name.length;

my_name.slice(0,1); // getting the first charachter of my_name

// getting the my_name from the prompt and capitalize the first letter
var my_name = prompt('What is you my_name?');
var first_char = my_name.slice(0,1);
var first_char_upper = first_char.toUpperCase();
var rest_of_name = my_name.slice(1, my_name.length);
var capitalize_name = first_char_upper + rest_of_name
alert('Hello ' + capitalize_name)


//defining the function
function getMilk{
    alert('Going to get milk')
    //console log for developers to debug the code
    console.log('Going to get milk') 
};
// calling the function
getMillk();