#!/bin/sh

echo "*************************************************"
echo "Yolo Filter : setup of Python virtual environment"
echo "*************************************************"

echo "\nInstalling Python Virtual Environments"
pip install virtualenv
pip install --upgrade virtualenv

echo "\nSetting up Python Virtual Environment for this project"
cd ..
virtualenv -p python3.9 yolo-filter
source ./yolo-filter/bin/activate

echo "Installing Python requirements . . ."
cd yolo-filter
pip install -r requirements.txt
echo "Python requirements installation complete."

echo "\nDownloading the CNN (Convolutional Neural Network) weights . . ."
mkdir ./model-weights
wget -O ./model-weights/yolov3.weights https://pjreddie.com/media/files/yolov3.weights

echo "*************************************************"
echo "Setup of Virtual Environment complete"
echo "*************************************************"

echo "\nTo activate the Python Virtual Environment, please run: source ./bin/activate"
echo "To get out of the Python virtual environment, please run: 'deactivate'"

echo "\nTo execute a detection on a sample image, run: python detect.py --image samples/interstellar.jpg"
echo "To execute a detection on a sample video, run: python detect.py --image samples/subway.mp4"

echo "\nEnjoy YOLOv3!\n"
