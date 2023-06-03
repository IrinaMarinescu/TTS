# TTS
Text-to-speech recognition system

# Docker

Make sure to first have Docker Desktop installed. Then, run the Docker daemon.

### To build and generate the image: 

`docker build -t <myimage> .`

### To run and generate the container: 
`docker run -d --name <mycontainer> -p 8080:8080 <myimage>`
