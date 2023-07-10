#!/usr/bin/bash

#Finds the directory of the shell script.
directory_of_the_script=$(dirname $0)
#Changes the current directory of the shell script in order to locate the 'file_name'
cd $directory_of_the_script

#The below 2 are variables given in the homework.
file_name='git_address.txt'
line_break='=============='

#The below for loop iterates the lines of the given file.
for line in $(cat $file_name)
do
    #Seperates the lines with Internal Field Seperator defined as comma, and then puts them into an array named parts. '${parts[0]}' will include the url and '${parts[1]}' will include the path.
    IFS=',' read -a parts
    
    #If the path is a relative directory from the directory of the script, it will update the path. If the path is an absolute directory from the directory of the script, it will update the path.
    if [ -d ${parts[1]} ]
    then
        #Sets the current working directory as the folder path we want to update by pulling.
        cd ${parts[1]}
        #Updates the repository.
        git pull ${parts[0]}
        #Lists all the contents of the folder path.
        ls -la
        #Resets the working directory to directory of the script for the next iteration.
        cd $directory_of_the_script 

    #If the path doesn't exist, it will clone the repository to the given path relative to the script's directory or to the absolute path given.
    else
        #Creates a folder for the given path. (Maybe, the below 'mkdir' line is unnecessary.)
        mkdir ${parts[1]} $directory_of_the_script
        #Clones the repository to the path.
        git clone ${parts[0]} ${parts[1]}
        #Lists all the contents of the folder path.
        ls -la ${parts[1]}
        #Resets the working directory to directory of the script for the next iteration.
        cd $directory_of_the_script 
    
    fi

#Prints the line break at the end of each iteration of for loop.
echo $line_break

done < $file_name