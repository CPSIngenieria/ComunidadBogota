$(inicio);

function inicio () {

	$('.ruperton_Cerrado').children('.sorteo').slideUp();	

	$('.encabezado_ruperton').on('click', function () {
		$(this).siblings('.sorteo').slideToggle();
	});
}