# Album Face Search 

A blazing-fast, (for the moment) local Python application designed to find pictures of a specific person (like yourself!) hidden among hundreds of photos taken. It uses advanced facial recognition to create encodings and FAISS (Facebook AI Similarity Search) to perform vector searches.
Future improvements (on the way) : Application to my school's photo club's work with more than 500 photos per album & online availability 

## Features 🍓
* **Speed:** Uses FAISS to search through thousands of faces in milliseconds.
* **Apple Format Support:** Natively handles `.HEIC` photos from iPhones alongside `.JPG` and `.PNG`.
* **Video Queries:** Extract your face profile directly from a video instead of just a static image.
* **Local & Private:** No data is sent to the cloud. Everything processes on your own machine.

## Project Structure 

Ensure your project directory looks exactly like this before running the scripts:

```text
├── README.md
├── query.jpg               <-- The picture of the face you want to find
├── requirements.txt
├── data/
│   ├── albums/             <-- Put all your pictures in here
│   └── index/              <-- The FAISS database will be auto-generated here
└── src/
    ├── build_index.py      <-- Scans albums and builds the database
    ├── face_utils.py       <-- Helper functions for face encoding
    ├── search.py           <-- The search engine script
    └── video_utils.py      <-- Helper functions for processing video queries
```

## 🛠️ Installation & Setup (macOS Guide)

### 1. System Requirements
You need Homebrew installed. Open your terminal and install the required C++ compilers:
```bash
brew install cmake openblas

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to prevent system conflicts.

```bash
cd /path/to/your/project
python3 -m venv venv
source venv/bin/activate

### 3. Install Python Dependencies
With your (venv) activated, install the requirements:

```bash
python3 -m pip install -r requirements.txt


⚠️ Important Fix for Python 3.12+ (Missing Models Error)

On a modern version of Python, face_recognition might complain that its models aren't installed even when they are. Run these two commands to fix it permanently:

```bash
python3 -m pip install setuptools
python3 -m pip install --force-reinstall git+[https://github.com/ageitgey/face_recognition_models](https://github.com/ageitgey/face_recognition_models)
