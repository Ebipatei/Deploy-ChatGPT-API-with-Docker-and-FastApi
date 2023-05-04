# Deploy-ChatGPT-API-with-Docker-and-FastApi
Guide to deploy ChatGPT with Docker and FastApi

A Python FastAPI application that runs ChatGPT on Docker.

For several reasons you might not want to run your application locally. Following this repo, you can deploy your app on any cloud platform of your choice using a Docker container.


## Usage Description
- main.py: is the FastApi application
- requirements.txt: contains the required dependencies for the application to run
- Dockerfile: contains the commands required to build the Docker image

Make sure you have python>=3.8 and docker installed.

To use, clone this repo with:
```
git clone https://github.com/Ebipatei/Deploy-ChatGPT-API-with-Docker-and-FastApi.git
```

Navigate into the directory:

```
cd Deploy-ChatGPT-API-with-Docker-and-FastApi
```
From inside the directory you can then run the following Docker commands:
```
docker build -t chatgptapi .            #to build the image
docker run -p 8000:8000 chatgptapi      #to run the container on default port 8000 (you can choose any port number of your choice)
```
If you'd rather run it locally, just run this in your terminal after installing the necessary dependencies:
```
uvicorn main:app --reload    #the reload makes makes it so that you don't have to manually restart the application everytime you make changes
```

The app should now be running on http://127.0.0.1:8000/
And you can send post requests to it using:
```
import requests

prompt = {"prompt": "When was github created?"}
response = requests.post('http://localhost:8000/generate', json=prompt)
print(response.text)
```
That's it! If you're feeling motivated you can build a user interface to interact with the API.
