#!/bin/bash

#.env file source
. ./.env
#NOTE: the env file has to be in the same directory with the bash script

#General Variables
DEFAULT_AUDIO_EXTENSION="wav"  

##Function to get the filename
GetName(){
     filename=$(basename "$file" ."$ext")
}
##Function to convert from an extension to another
ConvertToWav(){
    (ffmpeg -y -hide_banner -loglevel error -i $AUDIO_SOURCE_DIRECTORY/$file $AUDIO_DESTINATION_DIRECTORY/$filename.$DEFAULT_AUDIO_EXTENSION)
}
##Function to Run python script while passing variable
SendToMysql(){
    cd $AUDIO_DESTINATION_DIRECTORY
    for file in *; do 
        python3 $PYTHON_SCRIPT $file $AUDIO_DESTINATION_DIRECTORY
    done
}

##Function to converto to a wav file 
AudioConvertion(){
    cd $AUDIO_SOURCE_DIRECTORY
    if [ ! -d $AUDIO_DESTINATION_DIRECTORY ]; then
    mkdir -p $AUDIO_DESTINATION_DIRECTORY;
    fi
    for file in *; do 
        ext="${file##*.}"
        GetName
        ConvertToWav
    done
}
##MAIN RUNING FUNCTIONS
AudioConvertion
SendToMysql



