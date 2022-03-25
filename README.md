## 🎯 Goal

A modular batch application that extracts, transcodes, and transforms the properties of audio files, transcribes audio to text, and stores the final conversion into a relational database.

---

## 📜 Main Use Case

-   Transcribe voicemails into text.

---

## 🦄 Features

-   Intake a single audio file or a directory of audio files
-   Able to use different languages with Google APIs - default is English  

---

## 🧰 Prerequisites

#### Source Code
- Clone [repository](https://github.com/lcubestudios/slingshot-api) (run the following command inside the terminal)
    ```sh
    git clone https://github.com/lcubestudios/slingshot-api.git
    cd slingshot-api
    ```
    > Keep this terminal active, this is where you will be required to run the commands stated below

#### Postman
- [Download](https://www.postman.com/) Postman
- Follow [How to Guide](https://www.postman.com/collections/eeda3ef277fca5943050) to Import Postman [Collection](https://www.postman.com/collections/66e38d8752042b4b1f4a)

#### Google API Key
- Follow [How to Guide](https://cloud.google.com/speech-to-text/docs/libraries#setting_up_authentication) to set up authentication
- Rename API key file to `key.json`
- Store key file for later use

---

## 📚 Additional Links

-   [Docker Hub](https://www.docker.com/products/docker-hub)
-   [Postman Importing Data](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/)
-   [Google Speech-to-Text Product Information](https://cloud.google.com/speech-to-text)

---

## 🏃Running the Solution
- **OPTION 1** - Docker
- **OPTION 2** - Building from source
--- 

## OPTION 1 – 🐳 Docker 
> *Make sure you have completed the tasks mentioned in the [Prerequisites](#-prerequisites) section above before proceeding
> Setup time 15 min

🎥 [Demo Video](https://link.us1.storjshare.io/jxvsrbj5le6lz7wgeqtsot2xs6aa/lcubestudios%2FClients%20recordings%2FSlingshot%2FLCube-Slingshot-Docker.mp4)

This method allows the application to easily be installed and deployed in a Docker container.

The application can be deployed in a local machine or directly on a Linux server. By default, the Docker will expose ports 80, 8080, 3306 - this can be changed within the .env if necessary. When ready, simply use Docker compose to build the image.

#### Before you Start:

##### Git
Make sure you are on the **master** branch (run the following command inside the terminal)
```sh
git checkout master
```
    
##### Docker
- Make sure there are no other containers using the same server ports. (Stop running any existing container or change the default application port (.env file)
- Delete any old version of the image & volume.
- Check your internet connection.

#### Step 1: Install Docker

1) Follow [this link](https://hub.docker.com/) to install Docker on your environment

#### Step 2: Set up environment

1. Move the Google API Key file `key.json` to the `/app` directory
2. Duplicate the `.env.sample` file and rename it to `.env`
3. Update `.env` variables
    > For this option **ONLY** update the following variables

    ```
    ## DATABASE ##
    DATABASE_HOST=“YOUR_DB_IP”
    DATABASE_NAME=“YOUR_DB_NAME”
    DATABASE_USER=“YOUR_DB_USERNAME”
    DATABASE_USER_PASSWORD=“YOUR_DB_PASSWORD”
    DATABASE_PORT=YOUR_PORT
    ```
    
    **IF** you want to run a test database uncomment `PMA_PORT` and update the following variables:
    
    ```
    DATABASE_HOST=“db”
    DATABASE_NAME=“audio_recognition”
    ```

4. Open `docker-compose.yml` and uncomment `lines 5 - 31`
    > **ONLY** do this step if want to run the test database

 
#### Step 3: Initialize Docker

1. Start Docker Service/Application
2. Run the following command inside the terminal in the project root directory
    > This will create the Slingshot image and pull in the necessary dependencies.

    If this is your first time running Docker run:
    ```sh
    docker compose up -d
    ``` 
    Otherwise run:
    ```
    docker compose up -d –-build
    ```


2. Verify containers are runing (run the following command inside the terminal)

    ```sh
    docker ps -a
    ```

#### Step 4: Test endpoints
1. Verify the deployment by navigating to your server address in your preferred browser
    > **IF** you are running the test database, navigate to `localhost:8080`
2. In **POSTMAN** Update `server` variable in the collection to your server address
    > **IF** you are running the test database, skip this step
3. Test CRUD commands in **POSTMAN** collection: `GET`, `PUT`, `POST`, `DELETE`

#### 🎉 DONE

To terminate Docker run the following command inside the terminal:

```sh
docker compose down 
```

---

## OPTION 2 - Building from source
> *Make sure you have completed the tasks mentioned in the [Prerequisites](#-prerequisites) section above before proceeding
> Setup time 15 min

🎥 [Demo Video](https://link.us1.storjshare.io/jwett4vprqdewetmw7vmvptq6wea/lcubestudios%2FClients%20recordings%2FSlingshot%2FLCube-Slignshot-Git.mp4)

#### Before you Start:

##### Git
Make sure you are on the **dev** branch (run the following command inside the terminal)
```sh
git checkout dev
```

#### Step 1: Install Server Requirements
> You can use `apt-get` or `homebrew`
- python3
- pip3
- PHP 7.4
- Bash
- apache2
- ffmpeg

#### Step 2: Install the Dependencies 
Run the following command inside the terminal:
```
pip install -r requirements.txt
```

#### Step 3: Set up environment

1. Move the Google API Key file `key.json` to the root directory
2. Duplicate the `.env.sample` file and rename it to `.env`
3. Update `.env` variables
    > For this option **ONLY** update the following variables

    ```
    ## DATABASE ##
    DATABASE_HOST=“YOUR_DB_IP”
    DATABASE_NAME=“YOUR_DB_NAME”
    DATABASE_USER=“YOUR_DB_USERNAME”
    DATABASE_USER_PASSWORD=“YOUR_DB_PASSWORD”
    DATABASE_PORT=YOUR_PORT

    ## PROJECT ROOT ##
    REPO_DIRECTORY="PATH/TO/PROJECT/DIRECTORY"
    
    ## GOOGLE KEY ##
    GOOGLE_APPLICATION_CREDENTIALS=PATH/TO/PROJECT/DIRECTORY/key.json
    ```

#### Step 4: Update database

Run the following command inside _Mysql_ or _PHPMyAdmin_

```sql
ALTER TABLE `ast_voicemessages` ADD `audioname` VARCHAR(80) NOT NULL AFTER `flag`, ADD `lastmodify` TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) AFTER `audioname`;
```

#### Step 5: Test endpoints
1. In **POSTMAN** Update `server` variable in the collection to your server address
2. Test CRUD commands in **POSTMAN** collection: `GET`, `PUT`, `POST`, `DELETE`

#### 🎉 DONE

---

## How to use the solution

#### GET
> Load udio by ID

##### Endpoint: 
`{{ server url }}/trigger.php?id={{ msg id }}`

##### Query Parameters: 
- id : message id

##### Example:

**GET**localhost/trigger.php?id=1
**response**

```json
{
    "success": "true", 
    "status": 200,
    "message": "Record Found.", 
    "results": {
        "msg_id": 1,
        "audioname": "audio.wav",
        "txtrecording": "Lorem ipsum",
        "more_data": "..."
    }
}
```

#### POST
> Transcribe all audio files from a folder

##### Endpoint: 
`{{ server url }}/trigger.php`

##### Example:

**POST**/localhost/trigger.php
**response**

```json
{
    "success": "true", 
    "status": 200,
    "message": "X record(s) has been added.", 
    "results": [{
        "audioname": "audio.wav",
        "dir": "/path/to/audio/",
        "duration": "in seconds",
        "txtrecording": "Lorem ipsum",
    }, { "more_data": "..." }]
}
```

#### PUT (Single)
> Transcribe Audio by ID

##### Endpoint: 
`{{ server url }}/trigger.php?id={{ msg id }}`

##### Example:

**PUT**/localhost/trigger.php?id=1
**response**

```json
{
    "success": "true", 
    "status": 200,
    "message": "Record has been updated.", 
    "results": {
        "msg_id": 1,
        "audioname": "audio.wav",
        "duration": "in seconds",
        "txtrecording": "Lorem ipsum",
    }
}
```

#### PUT (All)
> Transcribe all audios with no transcript

##### Endpoint: 
`{{ server url }}/trigger.php`

##### Example:

**PUT**/localhost/trigger.php
**response**

```json
{
    "success": "true", 
    "status": 200,
    "message": "X record(s) has been updated.", 
    "results": [{
        "msg_id": 1,
        "audioname": "audio.wav",
        "duration": "in seconds",
        "txtrecording": "Lorem ipsum",
    }, { "more_data": "..." }]
}
```

#### DELETE
> Delete record by ID

##### Endpoint: 
`{{ server url }}/trigger.php?id={{ msg_id }}`

##### Example:

**DELETE**/localhost/trigger.php?id=1
**response**

```json
{
    "success": "true", 
    "status": 200,
    "message": "Record has been deleted.", 
    "results": {
        "msg_id": 1
    }
}
```

---

## 👋 Meet the Authors

### Luis Muñoz

- [LinkedIn](https://www.linkedin.com/in/lmunoz0806/)
- [Github](https://github.com/lmunoz0806)

### Dennys Cedeño

- [LinkedIn](https://www.linkedin.com/in/dcedenor/)
- [Github](https://github.com/dennys9415)

## 📣 Connect with LCube Studios
- 🌎 [Website](https://Lcubestudios.io)
- ✉️ [Contact Us]("mailto:Contact@lcubestudios.io")
- 📅 [Let's Meet](https://calendly.com/lcubestudios/30min)
#### Follow Us
- [LinkedIn](https://www.linkedin.com/company/lcubestudios/)
- [Instagram](https://www.instagram.com/lcubestudios)
- [Facebook](https://www.facebook.com/lcubestudiosnyc/)
- [Twitter](https://www.twitter.com/lcubestudios/)
- [Discord](https://discord.com/invite/6Ud9x23zaK)
- [Github](https://github.com/lcubestudios)

## 💡 Let's make your FrameWork 



