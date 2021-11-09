(function ($) {
	var doc = $(document).ready(function () {
		doc.on("click", function () {
			wash();
		});
	});
})(jQuery);

var cardslist = [];

function wash() {
	$(".board").each(function (index) {
		$(this)
			.find(".board-row")
			.each(function (index) {
				/*remove all into a list*/
				$(this)
					.children("div")
					.each(function (index) {
						var links = $(this);
						//console.log(links);
						cardslist.push(links);
						$(this).remove();
					});
			});
	});

	//console.log(cardslist);
	//cdl = cardslist.length;
	//console.log(cdl);
	$(".board-row").each(function (index, element) {
		//console.log($(this));
		while (cardslist.length > 0) {
			cdl = cardslist.length;
			idx = Math.floor(Math.random() * cdl);
			console.log(cdl + " " + idx);
			delgrp = cardslist.splice(idx, 1);
			$(element).append(delgrp[0]);
			if ((cdl - 1) % 13 == 0) break;
		}
	});
}