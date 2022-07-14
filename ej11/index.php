<?php

	function generateString($length = 10) {
    	return substr(
    		str_shuffle(
    			str_repeat(
    				$x='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 
    				ceil($length / strlen($x))
    			)
    		),
    		1,
    		$length
    	);
	}
	
	$menuLen = 8;
	$menuArray = array();

	for ($i = 0; $i < $menuLen; $i++) {
		$menuObj = new stdClass;
		$menuObj->name = generateString(5);
		$menuObj->position = $i+1;
		array_push($menuArray, $menuObj);
	}

	//print_r($menuArray);
?>
<!doctype html>
<html lang="en">
 	<head>
    	<meta charset="utf-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1">
    	<title>Menu</title>

    	<link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/navbars/">
		<link href="assets/dist/css/bootstrap.min.css" rel="stylesheet">
    	<style>
      		.bd-placeholder-img {
        		font-size: 1.125rem;
        		text-anchor: middle;
        		-webkit-user-select: none;
        		-moz-user-select: none;
        		user-select: none;
      		}

      		@media (min-width: 768px) {
        		.bd-placeholder-img-lg {
          			font-size: 3.5rem;
        		}
      		}
    	</style>
    	<!-- Custom styles for this template -->
    	<link href="navbar.css" rel="stylesheet">
  	</head>
  	<body>
		<main>
  			<nav class="navbar navbar-expand-sm navbar-dark bg-dark" aria-label="Third navbar example">
    			<div class="container-fluid">
      				<a class="navbar-brand" href="#">Expand at sm</a>
      				<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample03" aria-controls="navbarsExample03" aria-expanded="false" aria-label="Toggle navigation">
        				<span class="navbar-toggler-icon"></span>
      				</button>

      			<div class="collapse navbar-collapse" id="navbarsExample03">
      				<ul class="navbar-nav me-auto mb-2 mb-sm-0">
        				<?php foreach ($menuArray as $key => $value) { ?>
        					<li class="nav-item">
        						<a class="nav-link" aria-current="page" href="#"><?=$value->name?></a>
        					</li>
        				<?php } ?>
        			</ul>
        			<form>
          				<input class="form-control" type="text" placeholder="Search" aria-label="Search">
        			</form>
      			</div>
  			</nav>
		</main>
    	<script src="assets/dist/js/bootstrap.bundle.min.js"></script>
  	</body>
</html>
