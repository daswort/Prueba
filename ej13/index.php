<?php
  
  $url = "https://www.thecocktaildb.com/api/json/v1/1/random.php";
  $cocktailDetail = "";

  try {

    $cocktailDetail = file_get_contents($url);    
    $cocktailDecoded = json_decode($cocktailDetail);
    $cocktail = $cocktailDecoded->drinks[0];

  } catch (Exception $e) {

      $cocktailDetail = 'API no responde';
  }


?>

<!doctype html>
<html lang="en" class="h-100">
  <head>
    <meta charset="utf-8">
    <title>Cocktail</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/cover/">

    
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

    
    <link href="cover.css" rel="stylesheet">
  </head>
  <body class="d-flex h-100 text-center text-white bg-dark">
    
<div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
  <header class="mb-auto">
    <div>
      
    </div>
  </header>

  <main class="px-3">
    <h1><?=$cocktail->strDrink?></h1>
    <h4><?=$cocktail->strCategory?></h4>
    <p class="lead"><?=$cocktail->strInstructions?></p>
    <p class="lead">
      <img src="<?=$cocktail->strDrinkThumb?>" class="img-thumbnail" />
    </p>
  </main>

  
</div>


    
  </body>
</html>
