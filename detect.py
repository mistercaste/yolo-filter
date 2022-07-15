import argparse
import sys
import os

from utils import *

parser = argparse.ArgumentParser()
parser.add_argument('--model-cfg', type=str, default='./cfg/yolov3.cfg',
                    help='path to config file')
parser.add_argument('--model-weights', type=str,
                    default='./model-weights/yolov3.weights',
                    help='path to weights of model')
parser.add_argument('--image', type=str, default='',
                    help='path to image file')
parser.add_argument('--video', type=str, default='',
                    help='path to video file')
parser.add_argument('--src', type=int, default=0,
                    help='source of the camera')
parser.add_argument('--output-dir', type=str, default='outputs/',
                    help='path to the output directory')
parser.add_argument('--visualize', action='store_true', default=False,
                    help='If set visualizes the currently processed image in a GUI window')
parser.add_argument('--store-only-on-item-detection', action='store_true', default=False,
                    help='Saves files only if a detection happens, otherwise skip')
parser.add_argument('--model-classes', type=str, default='cfg/classes.txt',
                    help='the list of classes')
parser.add_argument("--include-classes", nargs="+", default=[],
                    help='A list of classes to include when filtering')
args = parser.parse_args()

# print the arguments
print('#' * 60)
print('----- info -----')
print('[i] The config file: ', args.model_cfg)
print('[i] The weights of model file: ', args.model_weights)
print('[i] The classes of model file: ', args.model_classes)
print('[i] Only filtering on classes: ', args.include_classes)
print('[i] Path to image file: ', args.image)
print('[i] Path to video file: ', args.video)
print('[i] Open GUI window while processing: ', args.visualize)
print('[i] Skip storing unless a detection happens: ', args.store_only_on_item_detection)
print('#' * 60)

# Define classes from file
classes = None
with open(args.model_classes, 'rt') as file:
    classes = file.read().rstrip('\n').split('\n')
print('Classes configured for CV recognition: ')
print(classes)
print('#' * 60)

# Define filters
excluded_classes_ids = []
for i in args.include_classes:
    excluded_classes_ids.append(classes.index(i))

# Check outputs directory
if not os.path.exists(args.output_dir):
    print('==> Creating the {} directory...'.format(args.output_dir))
    os.makedirs(args.output_dir)
else:
    print('==> Skipping create the {} directory...'.format(args.output_dir))

# Give the configuration and weight files for the model and load the network using them
net = cv2.dnn.readNetFromDarknet(args.model_cfg, args.model_weights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def _main():
    wind_name = 'Detection using YOLOv3'
    if args.visualize:
        cv2.namedWindow(wind_name, cv2.WINDOW_NORMAL)

    output_file = ''

    if args.image:
        if not os.path.isfile(args.image):
            print("[!] ==> Input image file {} doesn't exist".format(args.image))
            sys.exit(1)
        cap = cv2.VideoCapture(args.image)
        output_file = args.image[:-4].rsplit('/')[-1] + '.jpg'
    elif args.video:
        if not os.path.isfile(args.video):
            print("[!] ==> Input video file {} doesn't exist".format(args.video))
            sys.exit(1)
        cap = cv2.VideoCapture(args.video)
        output_file = args.video[:-4].rsplit('/')[-1] + '.avi'
    else:
        # Get data from the camera
        cap = cv2.VideoCapture(args.src)

    # Get the video writer initialized to save the output video
    if not args.image:
        video_writer = cv2.VideoWriter(
            os.path.join(args.output_dir, output_file),
            cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
            cap.get(cv2.CAP_PROP_FPS), (
                round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            )
        )

    while True:

        has_frame, frame = cap.read()

        # Stop the program if reached end of video
        if not has_frame:
            print('[i] ==> Done processing!')
            if args.store_only_on_item_detection and not len(objects):
                print('[i] ==> Output file storage skipped: no item detected')
            else:
                print('[i] ==> Output file is stored at', os.path.join(args.output_dir, output_file))
            cv2.waitKey(1000)
            break

        # Create a 4D blob from a frame
        blob = cv2.dnn.blobFromImage(frame, 1 / 255, (IMG_WIDTH, IMG_HEIGHT),
                                     [0, 0, 0], 1, crop=False)

        # Set the network input
        net.setInput(blob)

        # Run the forward pass to get output of the output layers
        outs = net.forward(get_outputs_names(net))

        # Remove the bounding boxes with low confidence
        objects = post_process(frame, outs, CONF_THRESHOLD, NMS_THRESHOLD, classes, excluded_classes_ids)
        print('[i] ==> # of items detected: {}'.format(len(objects)))
        print('#' * 60)

        # Initialize the information to display on the frame
        info = [
            ('Number of items detected', '{}'.format(len(objects)))
        ]

        for (i, (txt, val)) in enumerate(info):
            text = '{}: {}'.format(txt, val)
            cv2.putText(frame, text, (10, (i * 20) + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLOR_WHITE, 2)

        # Save the output video to file
        if args.store_only_on_item_detection and not len(objects):
            print("Skipping file saving")
        else:
            if args.image:
                cv2.imwrite(os.path.join(args.output_dir, output_file), frame.astype(np.uint8))
            else:
                video_writer.write(frame.astype(np.uint8))

        if args.visualize:
            cv2.imshow(wind_name, frame)

        key = cv2.waitKey(1)
        if key == 27 or key == ord('q'):
            print('[i] ==> Interrupted by user!')
            break

    cap.release()
    cv2.destroyAllWindows()

    print('==> All done!')
    print('#' * 60 + '\n')


if __name__ == '__main__':
    _main()
