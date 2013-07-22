$(document).ready(function() {
	var $countdown = $('#countdown');
	if ($countdown.length) {
		var timerId = countdown(
			new Date(2013, 8, 4, 8, 35, 0, 0),
			function(ts) {
				s = ts.toHTML("strong");

				$countdown.html(s);
			},
			countdown.MONTHS | countdown.DAYS|countdown.HOURS|countdown.MINUTES|countdown.SECONDS
		)
	}
});