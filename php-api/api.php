<?php
# bro is speaking facts not gonna lie
$q = $_GET['q'] ?? die('Missing q parameter')
echo file_get_contents('<put your cloudflare worker link here smartypants>' . substr(str_shuffle('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'), 0, 24) . "?q=" . urlencode($q)) ?? die('Roboworks failed to respond.');
?>
