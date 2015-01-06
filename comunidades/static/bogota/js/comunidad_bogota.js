
//Esperamos el evento load y lanzamos la funcion de inicio de la aplicacion:
$(inicio);

//Funcion que arranca la aplicacion:
function inicio () {

	//Inicializamos los valores de las entradas:
	$('#Filtro-palabra-clave input').val("");
	$('#Filtro-palabra-clave input').focus();

	//Asignamos los eventos de buscar resultados: 
	$('#Lupa').on("click",buscar);
	$('#Filtro-palabra-clave input').keypress(function(e) {
	    if(e.which == 13) {
	        buscar();
	    }
	});
	/*$('#Filtro-palabra-clave input').on("input",buscar);*/
	/*$('#comunidades option').on("input",buscar);*/

	//Definimos algunas constantes:
	window.TIEMPO_BANNER = 10000;
	window.TIEMPO_DEMONIO = 50;
	window.TIEMPO_DEMONIO_TIPS = 3500;

	//Inicializamos variables para animacion del banner:
	window.banners = $('.imagen-banner');
	window.timer_banner  = new Timer( pasar_banner, TIEMPO_BANNER );
	window.banner_activo = 0;

	//Ponemos los banners en posicion inicial:
	for (var i = banners.length - 1; i >= 0; i--) {
		$(window.banners[i]).css('left','100%');
	};

	//Ponemos el primer banner en posicion visible:
	$(window.banners[banner_activo]).css('left','0%');

	//Asignamos el evento de pausar_timer y reanudar_timer en el timer_banner:
	$('#Contenedor-banner').hover(pausar_timer,reanudar_timer);
	/*$('#Contenedor-banner').on("click",pasar_banner_forzado);*/

	//Asignamos los eventos de mover banner a izquierda y derecha:
	$('#Boton-banner-derecho').on('click', pasar_banner_forzado);
	$('#Boton-banner-izquierdo').on('click', retroceder_banner);

	//Corremos el demonio que actualiza la barra de progreso del banner:
	window.idDemonio = window.setInterval(actuzalizar_progreso_banner, TIEMPO_DEMONIO);

	//Corremos el demonio que actualiza los mensajes de ayuda en el filtro de comunidad:
	window.idDemonioTips = window.setInterval(lanzar_tip, TIEMPO_DEMONIO_TIPS);
}

function lanzar_tip () {

	url = "tips/";

	//Hacemos una peticion AJAX a la url que formamos:
	$.ajax({
		url: url
	})
	.done( cambiar_tip ); //Llamamos a la funcion respuesta para presentar los resultados.
}

function cambiar_tip (tips) {
	
	$('#Tips p').hide().html(tips.tip).fadeIn();

}

function pasar_banner_forzado () {

	window.clearTimeout(window.timer_banner.timerId_actual());
	pasar_banner();
	actuzalizar_progreso_banner();
}

function actuzalizar_progreso_banner () {
	
	progreso = window.timer_banner.remaining_time();
	valor_progreso_porcentual = (100 - (progreso / 100)) + '%'; 
	$('#Progreso-banner').css('width', valor_progreso_porcentual);
}

//Funcion que permite pasar al siguiente banner en la cola:
function pasar_banner () {

	//Pasamos al siguiente banner:
	window.banner_activo += 1;

	//Si se acabaron los banners, pasamos al primero:
	if ( window.banner_activo >= window.banners.length ) {
		
		//Pasamos al primer banner:
		window.banner_activo = 0;
		
		//Ponemos los banners en posicion inicial:
		for (var i = banners.length - 1; i >= 0; i--) {
			$(window.banners[i]).css('left','100%');
		};

		//Ponemos el primer banner en posicion visible:
		$(window.banners[banner_activo]).css('left','0%');
	
	}
	//Si existe el siguiente banner, lo mostramos:
	else {

		//Movemos el banner anterior a una zona no visible. 
		//Luego movemos el banner a mostrar a la zona visible:
		$(window.banners[banner_activo-1]).css('left','-100%');	
		$(window.banners[banner_activo]).css('left','0%');	
	
	}

	//Reinicia el timer_banner:
	window.timer_banner = new Timer( pasar_banner, TIEMPO_BANNER );

}

//Funcion que permite pasar al siguiente banner en la cola:
function retroceder_banner () {

	//Pasamos al siguiente banner:
	window.banner_activo -= 1;

	//Si se acabaron los banners, pasamos al primero:
	if ( window.banner_activo < 0 ) {
		
		//Pasamos al primer banner:
		window.banner_activo = 0;
	
	}
	//Si existe el siguiente banner, lo mostramos:
	else {

		//Movemos el banner anterior a una zona no visible. 
		//Luego movemos el banner a mostrar a la zona visible:
		$(window.banners[banner_activo]).css('left','0%');	
		$(window.banners[banner_activo+1]).css('left','100%');	
	
	}

	//Reinicia el timer_banner:
	window.clearTimeout(window.timer_banner.timerId_actual());
	window.timer_banner = new Timer( pasar_banner, TIEMPO_BANNER );
	actuzalizar_progreso_banner();
}

//Clase utilitaria que controla el tiempo de cada banner:
function Timer(callback, delay) {

    var timerId, start, remaining = delay;

    this.pause = function() {
        window.clearTimeout(timerId);
        remaining -= new Date() - start;
    };

    this.resume = function() {
        start = new Date();
        window.clearTimeout(timerId);
        timerId = window.setTimeout(callback, remaining);
    };

    this.remaining_time = function() {
    	return remaining - (new Date() - start);
    };

    this.timerId_actual = function() {
    	return timerId;
    }

    this.resume();
}

//Funcion que reanuda la cuenta del tiempo de banner:
function reanudar_timer () {

	window.idDemonio = window.setInterval(actuzalizar_progreso_banner, TIEMPO_DEMONIO);
	window.timer_banner.resume();
}

//Funcion que pausa la cuenta del tiempo de banner:
function pausar_timer () {
	$('.boton-banner').fadeIn();
	window.clearInterval(window.idDemonio);
	window.timer_banner.pause();
}

//Funcion que despliega la info adicional en cada resultado:
function ver_descripcion () {
	$(this).siblings('.info-adicional').slideToggle();
}

//Funcion que envia una peticion AJAX al servidor pidiendo resultados:
function buscar () {

	//Obtenemos las palabras clave a buscar y en que comunidad:
	palabras_clave = $('#Filtro-palabra-clave input').val().split(" ").join("_");
	comunidad      = $('#Filtro-comunidad input').val();
	
	//Validamos las entradas de datos:
	if (palabras_clave == "") {
		
		$('#Resultados').html("<section id='Resultados'><p id='Sin-resultados'></p></section>");
		$('#Sin-resultados').html('Introduce una palabra clave').css('background', 'linear-gradient(#ffaa00 30%, #edc951)');
		
		return false;
	};

	if (comunidad == "") comunidad = "Cualquiera";

	//Escribimos las palabras clave a modo de debug:
	/*console.log("palabra clave:" + palabras_clave);*/
	
	//Formamos la url para el request al servidor:
	url = "busqueda/" + comunidad + "/" + palabras_clave;

	//Hacemos una peticion AJAX a la url que formamos:
	$.ajax({
		url: url
	})
	.done( respuesta ); //Llamamos a la funcion respuesta para presentar los resultados.
}

//Funcion que imprime los resultados en el DOM:
function respuesta (data) {
	
	$('html,body').animate({scrollTop: $('#Filtro').offset().top -20}, 1000);	

	//Inicializamos la respuesta:
	html = "";

	//Validamos si no hay resultados:
	if (data.clientes.length == 0) {
		$('#Resultados').html("<section id='Resultados'><p id='Sin-resultados'></p></section>");
		$('#Sin-resultados').html('No hay resultados').css('background', 'linear-gradient(#ff6600 60%, #ffbb66)');
	}

	//Si hay resultados, formamos la respuesta:
	else {
		for (var c = 0; c < data.clientes.length; c++) {

			html += "<article class='resultado'>";
			html += "<div class='resultado-informacion'>";
			html += "<h3 class='resultado-nombre'>" + data.clientes[c].razon_social + "</h3><br><span class='comunidad'>" + data.clientes[c].comunidad + "</span><br>";
			
			if(data.clientes[c].telefono){
				html += "<h3 class='resultado-telefono'><span class='icon-phone-outline'></span> " + data.clientes[c].telefono + "</h3>";
			}

			if(data.clientes[c].celular){
				html += "<h3 class='resultado-celular'><span class='icon-device-phone'></span> " + data.clientes[c].celular + "</h3>";
			}

			html += "<h3 class='resultado-direccion'><span class='icon-location'></span> " + data.clientes[c].direccion + "</h3>";
			html += "<div class info-redes-sociales>";

			if(data.clientes[c].sitio_web){
				html += "<div class='resultado-url link-social'><span class='icon-world-outline'></span> <a href='" + data.clientes[c].sitio_web + "' target='_blank'>Sitio web</a></div>";
			}
			
			if(data.clientes[c].enlace_facebook){
				html += "<div class='resultado-facebook link-social'><span class='icon-social-facebook'></span> <a href='" + data.clientes[c].enlace_facebook + "' target='_blank'>Facebook</a></div>";
			}
			
			if(data.clientes[c].enlace_twitter){
				html += "<div class='resultado-twitter link-social'><span class='icon-social-twitter'></span> <a href='" + data.clientes[c].enlace_twitter + "' target='_blank'>Twitter</a></div>";
			}

			if(data.clientes[c].enlace_youtube){
				html += "<div class='resultado-youtube link-social'><span class='icon-youtube'></span> <a href='" + data.clientes[c].enlace_youtube + "' target='_blank'>Youtube</a></div>";
			}

			html += "<p class='ver-mas'>Más información</p>";
			html += "<p class='resultado-descripcion info-adicional' >" + data.clientes[c].descripcion + "</p>";

			if(data.clientes[c].inicio_horario_atencion && data.clientes[c].fin_horario_atencion){

				var prefijo_horario_inicio = 'am';
				var prefijo_horario_fin = 'am';

				if(data.clientes[c].inicio_horario_atencion >= 12) {
					prefijo_horario_inicio = 'pm';
					data.clientes[c].inicio_horario_atencion -= 12;
				}
				if(data.clientes[c].fin_horario_atencion >= 12) {
					prefijo_horario_fin = 'pm';
					data.clientes[c].fin_horario_atencion -= 12;
				}


				html += "<p class='resultado-horario info-adicional' >Horario de atención: " + data.clientes[c].inicio_horario_atencion + prefijo_horario_inicio + " - " + data.clientes[c].fin_horario_atencion + prefijo_horario_fin + "</p>";
			}

			html += "</div></div>";
			html += "<div class='resultado-logo'><img src='" + data.clientes[c].logo + "' /></div>";
			html += "</article>";


			//Escribimos la respuesta dentro del campo resultados:
			$('#Resultados').html(html);
		}
	}

	

	//Asignamos el evento de mostrar la descripcion:
	$('.ver-mas').on('click', ver_descripcion);
}
