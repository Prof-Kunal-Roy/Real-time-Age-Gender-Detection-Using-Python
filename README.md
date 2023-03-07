# Real-time-Age-Gender-Detection-Using-Python
Real-time Age Gender Detection Using Python, OpenCV and Deep Learning is a system capable of detecting age and gender from images or videos. It uses a combination of Python, OpenCV and Deep Learning to detect age and gender from a person's face.
# Steps
## Step 1: Importing the libraries
1. Opencv
2. Math
3. Time
4. Argparse

## Step 2: Create getFaceBox
We will create a function named getFaceBox to preprocess the image, generate a blob of the picture (to pay greater attention to key features), and locate the faces using pre-trained models such as opencv_face_detector_uint8.pb. If a face is detected (which can only occur if the probability is higher than the conf_threshold), we will draw a box around it with the cv2.rectangle() function, and it will be able to detect multiple faces.

## Step 3: Models and Variables
We are using **caffe-models** for age and gender detection and also defining variables for age and gender values.

## Step 4: Load and Start
We will load the network by using **cv2.dnn.readNet** to load the pre-trained models of age,gender and face . We will be Using the webcam of your system by using cv2.VideoCapture(0).

## Step 5: Read, Resize and Detect
Have a look at the frame, adjust the size to increase accuracy (not all of us have a GPU). Utilize getFaceBox to detect the faces and boxes, then generate a new blob with dimensions of (227,227) for easier processing by the model. Apply the pretrained models to the blob and print the probabilities. Utilize cv2.imshow() to view the result in real time, and there you have it, a functioning age-gender detector from Codeven (terrible pun, I know)!

# Conclusion 

Real-Time Age Gender Detection using OpenCV is a powerful and efficient method for accurately detecting age and gender from images and videos. It takes advantage of deep learning and the OpenCV library to quickly and accurately identify age and gender from faces. The results are reliable and accurate, making it an ideal tool for facial recognition applications.
