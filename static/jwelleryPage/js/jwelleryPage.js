var navFix=(function(){
	var fixed=false;
	$(window).on('scroll',function(){
		var top=$("body").scrollTop();
		var box=$(".box");
		if(top>=50 && !fixed)
		{
			fixed=true;
			box.css({"margin-top":"95px"});
		}

		else if(top<50 && fixed)
		{
			fixed=false;
			box.css({"margin-top":"5px"});
		}
	});
})();