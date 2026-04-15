# face-search
How to retrieve quickly your own pictures from albums with hundreds of group photos?


## 1. Install dependencies
pip install -r requirements.txt

## 2. Add photos
Put all albums in:
data/albums/

## 3. Build index
cd src
python build_index.py

## 4. Search
python search.py