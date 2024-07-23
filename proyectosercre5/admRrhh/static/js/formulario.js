const formularios = {
    formulario1: {
        expresiones: {
            nombre: /^[a-zA-ZÀ-ÿ\s]{1,20}$/
        },
        campos: {
            nombre: false
        }
    },
    formulario2: {
        expresiones: {
            nombre: /^[a-zA-ZÀ-ÿ\s]{1,20}$/,
            apellidoP: /^[a-zA-ZÀ-ÿ\s]{1,20}$/,
            telefono: /^\d{1,8}$/
        },
        campos: {
            nombre: false,
            apellidoP: false,
            telefono: false
        }
    },
    formulario3: {
        expresiones: {
            nombre: /^[a-zA-ZÀ-ÿ\s]{1,20}$/,
            apellidoP: /^[a-zA-ZÀ-ÿ\s]{1,20}$/
        },
        campos: {
            nombre: false,
            apellidoP: false
        }
    },
    formulario4: {
        expresiones: {
            nombre: /^[a-zA-ZÀ-ÿ\s]{1,20}$/,
            apellidoP: /^[a-zA-ZÀ-ÿ\s]{1,20}$/,
            apellidoM: /^[a-zA-ZÀ-ÿ\s]{0,20}$/, 
            telefono: /^\d{1,8}$/,
            documento: /^[a-zA-Z\d-]{0,9}$/,
            direccion: /^.{0,100}$/ 
        },
        campos: {
            nombre: false,
            apellidoP: false,
            apellidoM: true,
            telefono: false,
            documento: false,
            direccion: false
        }
    },
    formulario5: {
        expresiones: {
            
            hijo: /^\d{1}$/,
            ctbanco: /^\d{1,8}$/,
            nua: /^\d{1,8}$/,
            seguro: /^\d{1,8}$/,
            sueldo: /^\d{1,6}$/
        },
        campos: {
            hijo: false,
            ctbanco: true,
            nua: true,
            seguro: true,
            sueldo: false
        }
    },
    formulario6: {
        expresiones: {
            nota: /^([a-zA-Z0-9ñÑ.-]{1,70})?$/
            
        },
        campos: {
            nota: true,
            
        }
    },
    formulario7: {
        expresiones: {
            proyecto:/^[a-zA-Z0-9.-]{1,11}$/,
            grafo: /^\d{1,8}$/,
            trafo: /^[a-zA-Z0-9-]{1,14}$/,
            direccion: /^[a-zA-Z\d\s#_-]{0,100}$/
        },
        campos: {
            proyecto: false,
            grafo: false,
            trafo: false,
            direccion: false
        }
    },
    formulario8: {
        expresiones: {
            nombre: /^[a-zA-ZÀ-ÿ\s]{1,20}$/,
            apellidoP: /^[a-zA-ZÀ-ÿ\s]{1,20}$/
        },
        campos: {
            nombre: false,
            apellidoP: false
        }
    },
    formulario9: {
        expresiones: {
            rol:/^[a-zA-Z0-9_]{1,20}$/,
            
        },
        campos: {
            rol: false,
            
        }
    },
    formulario10: {
        expresiones: {
            usuario:/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
           
            
        },
        campos: {
            usuario: false,
            
        }
    },
    formulario11: {
        expresiones: {
            nombre:/^[a-zA-Z0-9()\-_".,\s]{1,20}$/,
           
            
        },
        campos: {
            nombre: false
            
        }
    },
};

const campos = {};

const validarFormulario = (e) => {
    const formularioActual = e.target.form.id;
    const campo = e.target.id;
    const expresion = formularios[formularioActual].expresiones[campo];
    if (expresion) {
        validarCampo(expresion, e.target, campo);
    }
};

const validarCampo = (expresion, input, campo) => {
    if (expresion.test(input.value.trim())) {
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
};

const inicializarValidacion = (formularioId) => {
    const inputs = document.querySelectorAll(`#${formularioId} input`);
    inputs.forEach((input) => {
        input.addEventListener('keyup', validarFormulario);
        input.addEventListener('blur', validarFormulario);
        validarFormulario({ target: input });
    });
};

document.addEventListener('DOMContentLoaded', () => {
    Object.keys(formularios).forEach((formularioId) => {
        inicializarValidacion(formularioId);
    });
});

document.querySelectorAll('form').forEach((form) => {
    form.addEventListener('submit', (e) => {
        e.preventDefault(); // Evita el envío automático del formulario

        const formularioActual = e.target.id;
        let formularioValido = true; // Bandera para verificar si el formulario es válido

        // Verifica la validación de cada campo en el formulario actual
        Object.keys(formularios[formularioActual].campos).forEach((campo) => {
            if (!campos[campo]) {
                formularioValido = false;
            }
        });

        if (formularioValido) {
            e.target.submit();
        } else {
            document.getElementById(`${formularioActual}__mensaje`).classList.add('formulario__mensaje-activo');
        }
    });
});
