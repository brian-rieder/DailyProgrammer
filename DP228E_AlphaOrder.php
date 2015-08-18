<?php
  $orig=$splitup=str_split(fgets(STDIN));
  array_pop($orig); array_pop($splitup);
  sort($splitup);
  echo implode($orig).($splitup != $orig ? " NOT" : "")." IN ORDER";
?>
