function validar(){
 var nombre,apellido,usuario,contraseña,expresion,contraseña2;
 nombre=document.getElementById("nombre").value;
 apellido=document.getElementById("apellido").value;
 usuario=document.getElementById("usuario").value;
 contraseña=document.getElementById("contraseña").value;
 contraseña2=document.getElementById("contraseña2").value;
if(nombre==""|| apellido==""||usuario==""||contraseña=="")
{
    alert("todos los campos son obligatorios");
    return false;
}
if (contraseña != contraseña2) {
    alert("Las passwords deben de coincidir");
    return false;

  } else {
    alert("Todo esta correcto");
    return false; 
  }
}