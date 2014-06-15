var page = require('webpage').create(),
system = require('system');
if (system.args.length < 2 || system.args.length > 2) {
    console.log('Usage: dl.js URL');
    phantom.exit(1);
}
else{ 
    var url=system.args[1];
    page.open(url,
	      function (status) {
		  if (status !== 'success') {
		      console.log('Unable to access network');
		  } else {
		      window.setTimeout(function(){
			  steps = page.content;
			  console.log(steps);
                       	  phantom.exit();
		      },10000);
	      }; 
});
}
