$(inicio);

function inicio () {
	
	var banner1 = $('#Banner1');
	var banner2 = $('#Banner2');
	var banner3 = $('#Banner3');
	
	$('#Filtro-palabra-clave input').val("");
	$('#Filtro-palabra-clave input').keyup(buscar);

	banner2.css( 'left' , '100%' );
	banner3.css( 'left' , '200%' );

}

function ver_descripcion () {
	$(this).siblings('.info-adicional').slideToggle();
}

function buscar () {

	palabras_clave = $('#Filtro-palabra-clave input').val();
	comunidad = $('#Filtro-comunidad input').val();
	
	if (palabras_clave == "") palabras_clave = "_";
	if (comunidad == "") comunidad = "Cualquiera";

	console.log("palabra clave:" + palabras_clave);
	
	url = "busqueda/" + comunidad + "/" + palabras_clave;

	$.ajax({
		url: url
	})
	.done( respuesta );

}

function respuesta (data) {

	html = "";

	if (data.clientes.length == 0) {
		html += "<h3 id='Sin-resultados'>No hay resultados</h3>";
	}
	else {
		for (var c = 0; c < data.clientes.length; c++) {

			html += "<article class='resultado'>";
			html += "<div class='resultado-informacion'>";
			html += "<h3 class='resultado-nombre'>" + data.clientes[c].razon_social + "</h3><span class='comunidad'>" + data.clientes[c].comunidad + "</span><br>";
			
			if(data.clientes[c].telefono){
				html += "<h3 class='resultado-telefono'><span class='icon-phone-outline'></span> " + data.clientes[c].telefono + "</h3>";
			}

			if(data.clientes[c].celular){
				html += "<h3 class='resultado-celular'>/<span class='icon-device-phone'></span> " + data.clientes[c].celular + "</h3>";
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

			html += "<p class='ver-mas'>Mas informacion</p>";
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


				html += "<p class='resultado-horario info-adicional' >Horario de atencion: " + data.clientes[c].inicio_horario_atencion + prefijo_horario_inicio + " - " + data.clientes[c].fin_horario_atencion + prefijo_horario_fin + "</p>";
			}

			html += "</div></div>";
			html += "<div class='resultado-logo'><img src='" + data.clientes[c].logo + "' /></div>";
			html += "</article>";

		}
	}

	$('#Resultados').html(html);
	$('.ver-mas').on('click', ver_descripcion);
}
