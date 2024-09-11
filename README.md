Human Verification through Eye Blinks
Project Overview
This project uses a webcam feed to detect human faces and eyes. It tracks eye movements and blinks in real-time to verify if a person is human. The verification process is based on detecting at least two consecutive eye blinks using OpenCV's Haar cascades for face and eye detection.
This system can be used as a simple human verification mechanism, where the user is verified as human based on their natural eye blink patterns.

Features
Real-time face and eye detection using OpenCV.
Blink detection to verify if the person is human.
Displays visual feedback through a webcam window, highlighting faces and eyes.
Notifies if the person is verified as human after detecting a sufficient number of blinks.

How It Works
Face and Eye Detection: The system uses OpenCV's pre-trained Haar cascades to detect faces and eyes within the webcam feed.
Blink Detection: By monitoring the presence or absence of eyes between frames, the system counts blinks.
Human Verification: Once two or more blinks are detected, the system displays a "Human Verified" message.
Visual Output: Rectangles are drawn around detected faces and eyes, and the verification status is displayed on the webcam feed.

Technologies Used
OpenCV: For computer vision tasks such as face and eye detection.
Haar Cascades: Pre-trained models for detecting faces and eyes.
Python: The programming language used for the entire project
