## 🎯 Goal
The Slingshot VoIP team will receive a modular batch application that extracts, transcodes, and transforms the properties of audio files, transcribes audio to text, and stores the final conversion into a relational database.

---

## 📜 Main Use Case
-   Transcribe voicemails into text.

---

## 🦄 Features
-   Application can be fed a single or a directory of audios 
-   Ability to use different languages with Google APIs - default is English  

---

## 🎥 Demo Videos
-   [Docker](https://link.us1.storjshare.io/jxvsrbj5le6lz7wgeqtsot2xs6aa/lcubestudios%2FClients%20recordings%2FSlingshot%2FLCube-Slingshot-Docker.mp4)
-   [AWS AMI](https://link.us1.storjshare.io/jwuaf7btqiyvvdt3x3hxxj5bdoba/lcubestudios%2FClients%20recordings%2FSlingshot%2FLCube-Slingshot-AMI.mp4)
-   [Bitbucket/GitHub](https://link.us1.storjshare.io/jwett4vprqdewetmw7vmvptq6wea/lcubestudios%2FClients%20recordings%2FSlingshot%2FLCube-Slignshot-Git.mp4)
---

## 📚 Extra Documentantion
-   [Share an AMI with specific organizations or organizational units](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/share-amis-with-organizations-and-OUs.html)
-   [Docker Hub](https://www.docker.com/products/docker-hub)
-   [Postman Importing Data](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/)
---

## 🧰 Prerequisites
- [Download Postman](https://www.postman.com/)
- [Import Postman Collection](https://www.postman.com/collections/eeda3ef277fca5943050)
- [Google Quick Start Guide](https://cloud.google.com/speech-to-text/docs/libraries)
- [Google SpeechToText Product Information](https://cloud.google.com/speech-to-text)
---

## 🏃Running the Solution (select an option)
1. Using Docker
2. Starting a new server of an AMI (Amazon Web Services Image)
3. Building from source
--- 

## Option 1 – 🐳 Docker 
> Setup time 15 min

The application can easily be installed and deployed in a Docker container.

The application can be deployed in a local machine or directly into a Linux server. (Please refer to the Docker setup video outlined in Demo Videos for guidance.) By default, the Docker will expose ports 80, 8080, 3306 - this can be changed within the .env if necessary. When ready, simply use Docker compose to build the image.

Images used (docker hub):

-   [PHP:7.4-apache](https://hub.docker.com/_/php)
-   [MYSQL](https://hub.docker.com/_/mysql)
-   [PhpMyAdmin](https://hub.docker.com/_/phpmyadmin)

Step 1: Follow the Steps Outlined in Prerequisites 

Step 2:  Update Configurations (.env File)

-   ✅ [Clone Code](https://github.com/lcubestudios/slignshot-api.git) 
-   ✅ Database Credentials
-   ✅ Database Ports
-   ✅ PhpMyAdmin Ports
-   ✅ Google Key
-   ✅ Drop the key file into the application directory

 
Step 3: Start Docker

-   ✅ Run the Docker-compose file 
```sh
docker compose up -d –build
```

This will create the Slingshot image and pull in the necessary dependencies.

-   ✅ Verify containers are running 

```sh
docker ps -a
```

 
Step 4: Test the Endpoints

Verify the deployment by navigating to your server address in your preferred browser

-   ✅ Update {{server}} variable in the collection to your server address
-   ✅ GET, PUT, POST, DELETE  

Step 5: Terminate Docker Container

Inside the terminal run. 

```sh
docker compose down 
```

Troubleshooting:

-   Make sure there are no other containers using the same server ports. (Stop running any existing container or change the default application port (.env file).)
-   Delete any old version of the image & volume.
-   Check your internet connection.

---
## Option 2 – AMI (Amazon Web Services)
> Setup time 15 - 20 min

Please refer to the AMI setup video outlined in Demo Videos for guidance. By default, the Docker will expose ports 80, 8080, 3306 - this can be changed within the .env if necessary. When ready, simply use Docker compose to build the image.

Step 1:

- ✅ Search & Run AMI (ami-0dd0e30901f7aaf62)

Step 2: Update Configurations 

-   ✅ Database Credentials
-   ✅ Database Ports
-   ✅ PhpMyAdmin Ports
-   ✅ Google Key

Step 3: Start Docker

-   ✅ Run the Docker-compose file 

```sh
docker-compose up -d
```

-   ✅ Verify containers are running 

```sh
docker ps -a
```

Step 4: Test the Endpoints

Verify the deployment by navigating to your server address in your preferred browser.

-   ✅ Update {{server}} variable in the collection to your Server address
-   ✅ GET, PUT, POST, DELETE  

Step 5: Terminate Docker Container

Inside the terminal run. 

```sh
docker-compose down 
```

---

## Option 3 - Building from source
> Setup time 15 min

#### Bitbucket/GitHub
Step 1: Follow the Steps Outlined in Prerequisites

Step 2: Install Server Requirements

-   ✅ python3
-   ✅ pip3
-   ✅ PHP 7.4
-   ✅ Bash
-   ✅ apache2
-   ✅ ffmpeg

Step 3: Install the Dependencies 

-   ✅ [Clone Code](https://github.com/lcubestudios/slignshot-api.git) 
-   ✅ Change Git branch to dev
```sh
git checkout dev
```
-   ✅ pip install -r requirements.txt

Step 4: Update Configurations

Update .env file inside the app folder, comment on any variable(s) you don’t plan to use.

-   ✅ Database Credentials
-   ✅ Database Ports
-   ✅ PhpMyAdmin Ports
-   ✅ Google Key

Step 5: Update existing database

Run the following command inside Mysql or PHPMyAdmin

```sh
ALTER TABLE `ast_voicemessages` ADD `audioname` VARCHAR(80) NOT NULL AFTER `flag`, ADD `lastmodify` TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) AFTER `audioname`;
```

Step 6: Test the Endpoints

Verify the deployment by navigating to your server address in your preferred browser.

-   ✅ Update {{server}} variable in the collection to your Server address
-   ✅ GET, PUT, POST, DELETE  

---

## How to use the solution

(Endpoint documentation also available inside Postman Collection.)

#### GET (Load Single Audio Values) 
- Endpoint: localhost/trigger.php/?id=1234567890
- Query Params: id=number
- You can send the ID in the URL
- No JSON data is needed

#### POST (Transcribe audio(s) from a folder)
- Endpoint: localhost/trigger.php
- Transcribes audio to text from a directory. No parameters are needed.
- The directory path needs to be specified at the .env level.

#### PUT (Transcribe Existing Audio)
- Endpoint: localhost/trigger.php/
- Send ID as JSON
- Ex: { "id": 1234567890}

#### PUT (Transcribe All existing Audios)
- Endpoint: localhost/trigger.php
- Transcribes all voicemails where text_adudio is NULL.
- No ID or JSON data is needed

#### DELETE (Delete a Record)
- Delete a record from the database.
- JSON data is expected.
- Ex: {"id": 1642295310}

---

## 📣 Join our Community 
-   [Discord](https://discord.com/invite/6Ud9x23zaK)
-   [Instagram](https://www.instagram.com/lcubestudios)
-   [Twitter](https://www.twitter.com/lcubestudios/)
-   [Calendly](https://calendly.com/lcubestudios/30min)
-   [LCubestudios.io](https://Lcubestudios.io)
-   [Contact@lcubestudios.io]("mailto:Contact@lcubestudios.io")
---

## 👋 Meet the Authors on LinkedIn
-   [LCube Studios](https://www.linkedin.com/company/lcubestudios/)
-   [Luis Muñoz](https://www.linkedin.com/in/lmunoz0806/)
-   [Dennys Cedeño​](https://www.linkedin.com/in/dcedenor/)
---
 
## 🧑🏼‍💻 Follow the Authors on GitHub
-   [LCube Studios](https://github.com/lcubestudios)
-   [Luis Muñoz](https://github.com/lmunoz0806)
-   [Dennys Cedeño​](https://github.com/dennys9415)
