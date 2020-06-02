<?php

session_start();
include "supload.php";

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Sample</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <nav class="navbar navbar-dark bg-dark">
        <span class="navbar-brand-center mb-0 h1">Automation-MobSF</span>
    </nav>

    <div class="alert alert-dark" role="alert">
        <?php
            if ( isset ($_SESSION['upload_message']) ){
                $uploaded = $_SESSION['upload_message'];
                $upload_msg - $name . " " . $uploaded;
                echo "$upload_msg";
            } elseif( isset ($_SESSION['error_message']) ){
                $error = $_SESSION['error_message'];
            } else{
                echo "";
            }
        ?>
    </div>

    <form action="" method="POST" enctype="multipart/form-data">
            <input type="file" name="sample">
            <p>Drag your files here or click in this area.</p>
            <button type="submit" name="submit">UPLOAD</button>
    </form>

    <footer id="sticky-footer" class="py-4 bg-secondary text-white-50">
            <div class="container text-center">
                <small>Automation-MobSF - Upload Sample & Analyze</small>
            </div>
    </footer>

    <script>
        $(document).ready(function(){
            $('form input').change(function (){
                $('form p').text(this.files.length + " file(s) selected");
            });
        });
    </script>
</body>
</html>