# Deploy on Vercel

The original `app.py` is a Streamlit app. Streamlit is best deployed on Streamlit Community Cloud, but Vercel expects a standard Python web application with a top-level `app` variable.

To support Vercel, this project includes `api/index.py`, a small Flask version of the same game. It exports this required value:

```python
app = Flask(__name__)
```

`vercel.json` directs all website requests to that file.

## Deploy steps

1. Import `Ayaanwanii/GuessTheNumber` into Vercel.
2. In **Project Settings → Environment Variables**, create a variable named `SECRET_KEY` with a long, random value.
3. Deploy. Vercel installs the libraries in `requirements.txt` automatically.

Use the Vercel URL for the Flask version. For the original Streamlit design, deploy `app.py` through Streamlit Community Cloud instead.
