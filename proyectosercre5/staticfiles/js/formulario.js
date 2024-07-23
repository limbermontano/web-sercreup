const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,20}$/,
    nombreP: /^[a-zA-ZÀ-ÿ\s]{1,20}$/,
    nombreF: /^[a-zA-ZÀ-ÿ\s]{1,20}$/,
    nombreFa: /^[a-zA-ZÀ-ÿ\s]{1,20}$/,
    apellidoP: /^[a-zA-ZÀ-ÿ\s]{1,20}$/,
    apellidoM: /^[a-zA-ZÀ-ÿ\s]{1,20}$/,
    
    documP: /^\d{1,7}$/,
    grafo: /^\d{1,7}$/,
    telefono: /^\d{1,8}$/,
    proyecto: /^[a-zA-Z0-9\.]{1,11}$/,
    trafo: /^[a-zA-Z0-9\_\-]{1,16}$/,

    hijo: /^\d{1,1}$/,
    nua: /^\d{1,8}$/,
    ctbanco: /^\d{1,10}$/,
    seguro: /^\d{1,8}$/,
    sueldo: /^\d{1,5}$/,
}

const campos = {
    nombre: false,
    nombreP: false,
    nombreF: false,
    nombreFa: false,
    
    apellidoP: false,
    apellidoM: false,
    documP: false,
    grafo: false,
    telefono: false,
    proyecto: false,
    trafo: false,
    

    hijo: false,
    nua: false,
    ctbanco: false,
    seguro: false,
    sueldo: false,
}

const validarFormulario = (e) => {
	switch (e.target.id) {

		case "nombre":

			validarCampo(expresiones.nombre, e.target, 'nombre');
		break;
		case "nombreP":

			validarCampo(expresiones.nombreP, e.target, 'nombreP');
		break;
		case "nombreF":

			validarCampo(expresiones.nombreF, e.target, 'nombreF');
		break;
		case "nombreFa":

			validarCampo(expresiones.nombreFa, e.target, 'nombreFa');
		break;

		case "documP":

			validarCampo(expresiones.documP, e.target, 'documP');
		break;
		case "apellidoP":

			validarCampo(expresiones.apellidoP, e.target, 'apellidoP');
		break;
		case "apellidoM":

			validarCampo(expresiones.apellidoM, e.target, 'apellidoM');
		break;
		case "grafo":

			validarCampo(expresiones.grafo, e.target, 'grafo');
		break;
		case "telefono":

			validarCampo(expresiones.telefono, e.target, 'telefono');
		break;
		case "proyecto":

			validarCampo(expresiones.proyecto, e.target, 'proyecto');
		break;
		case "trafo":

			validarCampo(expresiones.trafo, e.target, 'trafo');
		break;
	
		case "hijo":

			validarCampo(expresiones.hijo, e.target, 'hijo');
		break;
		case "nua":

			validarCampo(expresiones.nua, e.target, 'nua');
		break;
		case "ctbanco":

			validarCampo(expresiones.ctbanco, e.target, 'ctbanco');
		break;
		case "seguro":

			validarCampo(expresiones.seguro, e.target, 'seguro');
		break;
		case "sueldo":

			validarCampo(expresiones.sueldo, e.target, 'sueldo');
		break;

	}
}
const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');

		campos[campo] = false;
	}
}



inputs.forEach((input) => {
	
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e) => {
	if(campos.nombre ){
		formulario.submit();
		
	} else {
		e.preventDefault();
		document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
	}
	
	if(campos.nombreF && campos.apellidoP){
		formulario.submit();
		
	} else {
		e.preventDefault();
		document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
	}
	if(campos.proyecto && campos.grafo && campos.trafo){
		formulario.submit();
		
	} else {
		e.preventDefault();
		document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
	}
	if(campos.nombreP && campos.apellidoP && campos.apellidoM && campos.telefono && campos.documP){
		formulario.submit();
		
	} else {
		e.preventDefault();
		document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
	}	
	if(campos.nombreFa && campos.apellidoP && campos.telefono){
		formulario.submit();
		
	} else {
		e.preventDefault();
		document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
	}
});