import bz2, os, shutil, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(BASE, "shape_predictor_68_face_landmarks.dat")
URLS = [
    "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2",
    "https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2",
]

archive = TARGET + ".bz2"
for url in URLS:
    try:
        print("Downloading", url)
        with urllib.request.urlopen(url, timeout=60) as r, open(archive, "wb") as f:
            shutil.copyfileobj(r, f)
        break
    except Exception as e:
        print("failed:", e)
else:
    raise SystemExit("Download failed")

print("Extracting...")
with bz2.open(archive, "rb") as s, open(TARGET, "wb") as d:
    shutil.copyfileobj(s, d)
os.remove(archive)
print("Done")
