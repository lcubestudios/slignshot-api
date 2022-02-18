#!/bin/bash

#.env file source
. ./.env
#NOTE: the env file has to be in the same directory with the bash script

#General Variables
DEFAULT_AUDIO_EXTENSION=$DEFAULT_AUDIO_EXTENSION  #The desire extension to convert 'cause of the google api
PYTHON_SCRIPT=$PYTHON_SCRIPT  #The Python Script

##Function to get the filename
GetName(){
     filename=$(basename "$file" ."$ext")
}
##Function to convert from an extension to another
ConvertToWav(){
    (ffmpeg -n -i $SOURCE_DIRECTORY/$file $WORKING_DIRECTORY/$filename.$DEFAULT_AUDIO_EXTENSION)
}
##Function to Run python script while passing variable
SendToMysql(){
    cd $WORKING_DIRECTORY
    for file in *; do 
        python3 $PYTHON_SCRIPT $file $WORKING_DIRECTORY
    done
}

##Function to converto to a wav file 
AudioConvertion(){
    cd $SOURCE_DIRECTORY
    if [ ! -d $WORKING_DIRECTORY ]; then
    mkdir -p $WORKING_DIRECTORY;
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



