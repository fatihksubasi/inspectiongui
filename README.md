
## Prerequisites

- Anaconda/Miniconda or Docker is required to install.
- Tested under Ubuntu 16.04

## Build
### Clone
```
git clone https://gitlab.com/fatihksubasi/inspectiongui.git
```
### Conda
```
cd /path/to/inspectiongui
```
```
conda env create -f environment.yml
```
```
chmod +x run.sh
```
### Docker
```
cd /path/to/inspectiongui
```
```
docker build -t inspectiongui .
```

## Run
### Conda
```
./run.sh
```
### Docker
```
./run_docker.sh
```
The container opens the GUI in a new browser tab.

## Usage
###  Note: Most of the features is deactive except crack detection 
1. Open Revisiting tab
2. You can see all images using the slider before detecting the images containing crack.
3. Press 'Predict images with cracks' button to feed the images into CNN model.
4. Close and re-run the GUI to view the images with cracks.

## Notes
- Please do not remove file named 'image_pose_matching.txt' inside images folder. These are pose (position and orientation) information of the UAV at the time when corresponding image is taken.
- You can rerun crack detection function after deleting images in /images/predicted

## Directory Structure
    .
    ├── at_runtime.sh         # shell script to handle resolution and user forwarding
    ├── brick.h5              # CNN architecture 
    ├── brick.json            # CNN weights 
    ├── brick-labels.json     # CNN class labels
    ├── crack_detection.py    # crack detection functions 
    ├── Dockerfile            # docker build file
    ├── environment.yml       # conda environment config 
    ├── gui.py                # main GUI wrapper 
    ├── images                 
        ├── predicted
            ├── image_pose_matchings.txt
            ├── ...
        ├── image_pose_matchings.txt
        ├── 1.png
        ├── ...       
    ├── planner.kv            # kv language for GUI   
    ├── run.sh                # shell script to run the GUI
    ├── run_docker.sh         # shell script to run GUI in Docker container
    └── README.md