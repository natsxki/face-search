# Album Face Search 

A blazing-fast, (for the moment) local Python application designed to find pictures of a specific person (like yourself!) hidden among hundreds of photos taken. It uses advanced facial recognition to create encodings and FAISS (Facebook AI Similarity Search) to perform vector searches.
Future improvements (on the way) : Applied to my school's photo club's work with 200-500 photos per album. 

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
