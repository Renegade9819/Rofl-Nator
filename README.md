# Rofl-Nator

A website which detects faces in images and replaces them with 'rofl' emoji. Python and Flask as backend.

It's just a little project I made in order to learn Flask and how to use python as a backend in web development, with a little dash of Machine Learning

## What does it do?

* User uploads an image on the website.
* The image is sent to the server for processing.
* The server detects faces using MTCNN (Tensorflow 2.0 model), and replaces the detected faces with rofl-emoji.
* The server then sends the processed image back to the website and displays it.

## Technologies Used

* TensorFlow 2.0, install guide [here](https://www.tensorflow.org/install/pip)
* MTCNN Model `pip install mtcnn`

## Demo
![](https://media.giphy.com/media/JqDbSmI5cgQBaK2j95/giphy.gif)

### Known issues

* The upload button doesn't work if the filename contains spaces, or if the name is way too huge. (It's because I haven't implemented file name formatting)
* The size and position of the emoji after processing becomes inaccurate if the uploaded image has a very high resolution.
