#!/bin/sh

PYTHON3_VERSION=$(python3 -c 'import sys; print(str(sys.version_info[0])+"."+str(sys.version_info[1]))')

echo "******************************************************"
echo ""
echo "YOLO-FILTER"
echo ""
echo "Current system uses Python 3 version: ${PYTHON3_VERSION}"
echo "Current folder is: $(pwd)"
echo "Installation optimized for a Raspberry PI"
echo ""
echo "******************************************************"
echo "Checking preconditions"
echo "******************************************************"
sudo apt-get update && sudo apt-get install -y python3-pip python3-virtualenv libssl-dev python3-scipy libatlas3-base python3-picamera python3-matplotlib python3-tk python3-numpy build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev
pip3 install virtualenv
pip3 install --upgrade virtualenv

echo "\n******************************************************"
echo "Activating Python Virtual Environment"
echo "******************************************************"
virtualenv env
. env/bin/activate

echo "\n******************************************************"
echo "Installing Python requirements"
echo "******************************************************"
pip3 install --ignore-installed -r requirements.txt

echo "\n******************************************************"
echo "Get the CNN (Convolutional Neural Network) weights"
echo "******************************************************"
if [ ! -f ./model-weights/yolov3.weights ]
then
	echo "Model weights not found. Downloading . . ."
	mkdir ./model-weights
	wget -O ./model-weights/yolov3.weights https://pjreddie.com/media/files/yolov3.weights
else
    echo "Model weights found. Skipping download (237 MB)."
fi

echo "\n******************************************************"
echo "Setup complete. Ready to go!"
echo "******************************************************"
echo "To run you MUST activate the Python Virtual Environment by running: source ./env/bin/activate"
echo "To get out of the Python virtual environment, run: 'deactivate'"
echo "To execute a detection on a sample image, run: python detect.py --image samples/interstellar.jpg"
echo "To execute a detection on a sample video, run: python detect.py --image samples/subway.mp4"
echo ""
echo "       .---."
echo "      /     \\     Enjoy YOLOv3!"
echo "      \\.@-@./"
echo "      /\`\\_/\`\\"
echo "     //  _  \\\\\\"
echo "    | \\     )|_"
echo "   /\`\\_\`>  <_/ \\"
echo "   \\__/'---'\\__/"
echo ""
echo ""
echo ""
echo ""
