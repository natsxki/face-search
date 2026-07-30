<div align="center">

# ⋆౨ৎ⋆ Album Face Search ⋆౨ৎ⋆

***Find every photo of someone across hundreds of pictures, in milliseconds***

<br>

![Python](https://img.shields.io/badge/Python-3.10+-FFB5C2?style=flat-square&logo=python&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-vector%20search-C8B6FF?style=flat-square)
![face_recognition](https://img.shields.io/badge/face__recognition-dlib-B5D8FF?style=flat-square)
![OpenCV](https://img.shields.io/badge/OpenCV-video-B8E6D9?style=flat-square&logo=opencv&logoColor=white)
![Local & Private](https://img.shields.io/badge/100%25-local%20♡%20private-FFE0B5?style=flat-square)

<br>

*A little local Python app that hunts down every picture of a specific person in a big album*
*powered by facial recognition + FAISS.*

</div>

---

## What is this?

Originally created this as a prototype for my school's Audiovisual club that has a few hundreds pictures for each of the +- hundred events per year on its website. I wanted students to be able to find their pictures without scrolling forever.

Given a folder of pictures and one clear photo (or video!) of a face, this returns every image that person appears in - searching thousands of faces in milliseconds, entirely on your own machine. 

---

## Features

- **Fast** - [FAISS](https://github.com/facebookresearch/faiss) (Facebook AI Similarity Search) does exact nearest-neighbor lookups over face vectors in milliseconds
- **Image *or* video queries** - search from a static photo, or extract a face profile from a short video by averaging encodings across frames
- **iPhone friendly** - reads Apple `.HEIC` photos via `pillow-heif`, alongside `.jpg` / `.jpeg` / `.png`
- **Private by design** - everything runs locally; no data is ever sent anywhere
- **Tunable matching** - a distance threshold keeps results tight so you don't get false matches

---

## How it works

```
   BUILD PHASE  (build_index.py)              SEARCH PHASE  (search.py)

   data/albums/                               query.png  ── or ──  a video
        │                                          │                  │
        ▼                                          ▼                  ▼
   detect faces                              detect face        sample frames,
   (face_recognition/dlib)                   in query           average encodings
        │                                          │                  │
        ▼                                          └────────┬─────────┘
   128-d encoding per face                                  ▼
        │                                          128-d query vector
        ▼                                                   │
   FAISS IndexFlatL2  ◀───────── nearest-neighbor search ───┘
   + metadata.pkl                                           │
   (path + location)                                        ▼
                                            keep matches under the L2
                                            threshold  →  list of photos ✧
```

**Details**

- Every face becomes a **128-dimensional encoding** (via `face_recognition`, which wraps dlib's model).
- Encodings are stored in a **FAISS `IndexFlatL2`** (exact L2 search), with a parallel `metadata.pkl` holding each face's source image path and bounding box.
- At search time, the query face is compared against the whole index. Matches are filtered by a **squared-L2 threshold of `0.36`** - which is the equivalent of `face_recognition`'s standard Euclidean cutoff of `0.6` (since `0.6² = 0.36`).
- **Video queries** sample every 5th frame, encode any faces found, and **average** them into one robust query vector - nice for when a single photo is a bit blurry.
- Results are de-duplicated by image path, so each matching photo shows up once.

---

## Project structure

```
face-search/
├── query.png              <-- the face you want to find (jpg / png / heic)
├── requirements.txt
├── data/
│   ├── albums/            <-- drop all your photos in here
│   └── index/             <-- FAISS index + metadata, auto-generated ✧
└── src/
    ├── build_index.py     ⋆ scans albums → builds the FAISS database
    ├── search.py          ✧ runs a query (image or video) → matching photos
    ├── face_utils.py      · face detection + encoding helper
    └── video_utils.py     · extracts an averaged encoding from a video
```

---

## Installation & setup (macOS)

### 0. Add your pictures

- Put all your photos into `data/albums/`
- Put one clear photo of the target face in the project root, named `query.jpg` / `.png` / `.heic`

### 1. System requirements

You'll need [Homebrew](https://brew.sh/). Install the C++ build tools FAISS and dlib rely on:

```bash
brew install cmake openblas
```

### 2. Create a virtual environment

```bash
cd /path/to/face-search
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python dependencies

```bash
python3 -m pip install -r requirements.txt
```

> !!!! **Python 3.12+ fix (missing models error):** on newer Python, `face_recognition` sometimes can't find its models even when installed. Run these once to fix it permanently:
> ```bash
> python3 -m pip install setuptools
> python3 -m pip install --force-reinstall git+https://github.com/ageitgey/face_recognition_models
> ```

### 4. Build the index, then search

From inside the `src/` folder:

```bash
python3 build_index.py     # scans data/albums/ and builds the database
python3 search.py          # searches for ../query.png and prints matches
```

---

## Notes

- The album indexer currently picks up `.jpg` / `.jpeg` / `.png`. `.HEIC` is registered globally (so HEIC *query* images work), but to index HEIC files sitting in your albums you'd just add `.heic` to the extension filter in `build_index.py`. 
- Roadmap: scale to 500+ photos per album for the photo club, eventually an online version.

I decided not to go further with this project for now because all the challenges related to biometric data.

---

<div align="center">

*Made by [**natsxki**](https://github.com/natsxki)*

</div>
