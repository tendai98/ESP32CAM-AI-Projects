# ESP32 Camera Computer Vision Projects

This repository contains two projects that leverage the ESP32 Camera module for computer vision applications. These projects use a machine learning model to detect specific objects (containers or faces) and trigger an ESP-01 relay over a WiFi network. Here's an overview of the two projects:

## Container Detector

### Project Structure

- **CameraWebServer**
  - `app_httpd.cpp`: Handles the web server application for camera control.
  - `camera_pins.h`: Contains pin configuration for the camera module.
  - `CameraWebServer.ino`: The main Arduino sketch for the project.

- **Container-Detector**
  - `main.py`: The primary Python script for object detection.
  - `ml.py`: Contains machine learning-related functions.
  - `model`: A directory that holds the trained machine learning model.
  - `net.py`: Provides network-related functions.
  
- **ControlRelay**
  - `ControlRelay.ino`: An Arduino sketch that controls the ESP-01 relay module based on input.

This project is designed to detect containers using the ESP32 Camera module and trigger an ESP-01 relay when specific objects (containers) are detected. The object detection is driven by a machine learning model implemented in Python.

## Face Detector

### Project Structure

- **CameraWebServer**
  - `app_httpd.cpp`: Manages the web server for camera control.
  - `camera_pins.h`: Contains pin configuration for the camera module.
  - `CameraWebServer.ino`: The primary Arduino sketch for the project.

- **ControlRelay**
  - `ControlRelay.ino`: An Arduino sketch responsible for controlling the ESP-01 relay module.

- **Face-Detector**
  - `ai.py`: Contains functions for  the facial recognition model.
  - `enroll_face.py`: Handles the enrollment process for new faces.
  - `facial.bin`: The trained facial recognition model.
  - `main.py`: The main Python script for facial detection and recognition.
  - `net.py`: Provides network-related functions.

This project is focused on facial detection and recognition using the ESP32 Camera module. It employs a machine learning model to identify faces and can trigger an ESP-01 relay based on detected faces.

## Usage

Both projects involve the following key steps:

1. Set up the ESP32 Camera module for capturing images or video.
2. Utilize a machine learning model (likely a pre-trained model) for object or facial recognition.
3. Control an ESP-01 relay module based on the detection results.
4. Implement a web server for remote control
