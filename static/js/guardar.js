const form = document.forms['registro'];

const user={};
Array.from(from.elements).forEach(elements=>{
     if(elements.name)user[element.name]=element.value
})