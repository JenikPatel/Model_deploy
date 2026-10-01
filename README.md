# Bear Classifier

A simple web app that identifies the type of bear in an image. The model was trained with [fastai](https://docs.fast.ai/) and is served through a [Streamlit](https://streamlit.io/) interface, deployable on Streamlit Community Cloud.

Upload a photo (JPG, JPEG or PNG) and the app returns the predicted bear class along with the model's confidence.

## Demo

Live app: https://modeldeploy-lqy4oevqh6yyx58xhwv8dc.streamlit.app/

## How it works

1. The user uploads an image through the Streamlit file uploader.
2. The image is loaded as a fastai `PILImage` and displayed back to the user.
3. The exported learner (`export.pkl`) is loaded with `load_learner`.
4. `learn_inf.predict(img)` returns the predicted class and its probability, which are shown on the page.

## Repository structure

```
.
├── app.py             # Streamlit application
├── export.pkl         # Trained fastai model (exported learner)
├── requirements.txt   # Python dependencies
├── .gitattributes
└── .gitignore
```

## Getting started

### Prerequisites

- Python 3.13 (the model was exported from a Colab CPU runtime, so matching library versions is recommended)
- pip or conda

### Installation

```bash
# Clone the repository
git clone https://github.com/JenikPatel/Model_deploy.git
cd Model_deploy

# (Optional) create and activate an environment
conda create -n bear313 python=3.13
conda activate bear313

# Install dependencies
pip install -r requirements.txt
```

### Run locally

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually http://localhost:8501).

## Deployment (Streamlit Community Cloud)

1. Push this repository to GitHub (it must be public, or connected to your Streamlit account).
2. Go to [share.streamlit.io](https://share.streamlit.io) and click **Create app**.
3. Select the repository, branch, and set the main file path to `app.py`.
4. Click **Deploy**. Streamlit installs everything in `requirements.txt` automatically.

## Dependencies

Pinned versions are listed in `requirements.txt`. The main ones are:

| Package | Purpose |
|---|---|
| `streamlit` | Web interface |
| `fastai` / `fastcore` / `fasttransform` | Model loading and inference |
| `torch` / `torchvision` (CPU build) | Deep learning backend |
| `numpy`, `plum-dispatch` | Supporting libraries |

The `--extra-index-url` line in `requirements.txt` pulls the lightweight CPU-only PyTorch wheels, which keeps the deployment small.

## Notes

- `app.py` includes a small `pathlib` patch so a model exported on Linux (Colab) can be loaded on Windows. It only runs when `sys.platform == 'win32'` and has no effect on Streamlit Cloud.
- Keep the library versions in `requirements.txt` aligned with the environment used to train and export the model; mismatches can cause `export.pkl` to fail to load.

## Future improvements

- Cache the learner with `st.cache_resource` so the model loads once instead of on every upload
- Show the top-3 predictions with probabilities
- Add example images for quick testing

## Acknowledgements

- [fastai](https://docs.fast.ai/) for the training and inference library
- [Streamlit](https://streamlit.io/) for the app framework
