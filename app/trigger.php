<?php

$method = $_SERVER['REQUEST_METHOD'];

switch ($method) {
    case 'GET':
        $id= $_GET["id"];
        $sh = shell_exec("python3 get.py $id");
        echo($sh);
        break;
    case 'POST':
        $command= "bash audio_encoding.sh";
        $sh = shell_exec($command);
        echo($sh);
        break;
    case 'PUT':
        $raw=file_get_contents('php://input');
        $json=json_decode($raw,true); 
        $id=$json['id'];
        if ($id != NULL ){
            $sh = shell_exec("python3 put.py $id");
            echo($sh);
            #echo("Audio ($id) Has Been Updated");
        }else{
            $sh = shell_exec("python3 put_all.py");
            echo($sh);
            #echo("All NULL audio has been transcribed");
        }
        break;
    case 'DELETE':
        $raw=file_get_contents('php://input');
        $json=json_decode($raw,true); 
        $id=$json['id'];
        if ($id != NULL ){
            $sh = shell_exec("python3 delete.py $id");
            echo($sh);
        }else{
            echo("Enter a valid id");
        }
        break;
    default:
        $message = "Error send a server method";
        echo($message);
        break;
}



?>
