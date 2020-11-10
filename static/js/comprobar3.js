document.getElementById("registrar").addEventListener('click',comprobar);
function comprobar(){
    fetch(/src/usuario.json)
    .then(function(res){
        console.log(res);
            return res.json();
    })
    .then(function(data){
        let html ='';
        data.forEach(function(usuario)
        {
         html+=`
         <li>${usuario.nombre}${usuario.apellido}${usuario.usuario} ${usuario.contrasena}</li>
         `;   
        });
        document.getElementById('resultado').innerHTML=html;
    })
}
