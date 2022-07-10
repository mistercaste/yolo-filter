# YOLO-FILTER

# Deep learning detection with YOLOv3

The purpose of this fork is to provide a command line utility for general-purpose computational-vision.
Sample usages could be home video surveillance, counting users/objects, etc...

Target of the fork is also to provide a filter on the objects to recognize (see: `cfg/classes.txt`), while using a general purpose [CNN](https://en.wikipedia.org/wiki/Convolutional_neural_network) model.

## Getting started

The YOLOv3 (You Only Look Once) is a state-of-the-art, real-time object detection algorithm. The published model recognizes 80 different objects in images and videos. For more details, you can refer to this [paper](https://pjreddie.com/media/files/papers/YOLOv3.pdf).

## YOLOv3's architecture

![Imgur](assets/yolo-architecture.png)

Credit: [Ayoosh Kathuria](https://towardsdatascience.com/yolo-v3-object-detection-53fb7d3bfe6b)

## Python Prerequisites

* python 3 (tested on `3.6`, `3.7`, `3.8`, `3.9`)
* pip
* tensorflow
* opencv-python
* opencv-contrib-python
* numpy
* Keras
* matplotlib
* pillow

## Python Virtual Environment

* This project is isolated in a `Python Virtual Environment (virtualenv)`.
* This allows us to work with different versions of the dependencies.
* For more information, please see [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/).
* The setup of the virtualenv can be performed simply by executing the command below in the folder of the git clone:

```bash
$ ./kickoff.sh
```

## Run

Once the environment is set, the application can start with one of the following commands:

>**IMAGE INPUT**
```bash
$ python detect.py --image samples/interstellar.jpg
```

>**VIDEO INPUT**
```bash
$ python detect.py --video samples/subway.mp4
```

>**WEBCAM**
```bash
$ python detect.py --src 1
```

## Sample output

![Imgur](assets/interstellar.jpg)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for more details.

## References

This is a fork of [Yolo FACE](https://github.com/sthanhng/yoloface);
however some features were added by other very similar projects on the internet and some -of course- by myself. As none of these projects referenced an original fork, which I suspect exists (maybe even from the original YOLO author, [Joseph Chet Redmon](https://pjreddie.com/)?), I've referenced YoloFACE with the purpose of continuing from the codebase of this project.
Might anyone know which project is the original fork, please contact me: I will be more than happy to update my references. Thank you.

Matt