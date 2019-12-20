# InspectionGUI - - A Minimal Graphical User Interface for Concrete Crack Detection from Images

InspectionGUI is a minimal interface for structural crack detection from images using deep learning written in Python. Transfer learning is utilized in order to fine-tune InceptionV3 using Keras with Tensorflow backend. 

## Related Publications
Kucuksubasi, F., & Sorguc, A. G. (2018). Transfer Learning-Based Crack Detection by Autonomous UAVs. In 35th International Symposium on Automation and Robotics in Construction (pp. 584–591). Berlin. https://doi.org/10.22260/ISARC2018/0081


## Prerequisites

- Anaconda/Miniconda or Docker is required to install.
- Tested under Ubuntu 16.04

## Build
You can easily install inspectionGUI using conda or docker.
### Clone
```
git clone https://github.com/fatihksubasi/inspectiongui
```
### Conda
```
cd /path/to/inspectiongui
```
```
conda env create -f environment.yml
```
```
chmod +x run_conda.sh
```
### Docker
#### Pull from Docker Hub
```
docker pull fatihksubasi/inspectiongui
```
#### Build from Source
```
cd /path/to/inspectiongui
```
```
docker build -t fatihksubasi/inspectiongui .
```
```
chmod +x run_docker.sh
```

## Run
### Conda
```
./run_conda.sh
```
### Docker
```
./run_docker.sh
```
The container opens the GUI in a new browser tab.

## Usage
1. Select any image in your image folder
2. Press 'Load Images'
3. Press 'Show Images'
4. You can see all images using the slider before detecting the images containing crack.
5. Press 'Detect Cracks' button to feed the images into the CNN model.
6. Images with detected cracks will appear as soon as testing ends.
7. Press 'Clear & Refresh' to remove detected crack images  

## Notes

- You can rerun crack detection function after deleting images in /images/predicted
- Tensorflow version with GPU support gives better performance in detection.

## Directory Structure
    .
    ├── at_runtime.sh         # shell script to handle resolution and user forwarding
    ├── crack_detection.py    # crack detection functions 
    ├── Dockerfile            # docker build file
    ├── environment.yml       # conda environment config 
    ├── gui.py                # main GUI wrapper 
    ├── images                 
        ├── predicted
            ├── ...
        ├── 1.png
        ├── ...       
    ├── inspectiongui.kv      # kv language for GUI   
    ├── models
        ├──brick.h5           # CNN architecture 
        ├── brick.json        # CNN weights 
        ├── brick-labels.json # CNN class labels
    ├── run_conda.sh                # shell script to run the GUI
    ├── run_docker.sh         # shell script to run GUI in Docker container
    └── README.md