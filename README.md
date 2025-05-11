# 🎵 that_one

**that_one** is a Python-based web application that generates Spotify playlists based on user-input emotions. It integrates Natural Language Processing (NLP) for emotion detection, Spotify API management, and a web frontend with Bootstrap.

## 📖 Overview

The project lets users enter text describing their mood or feelings. It then uses an emotion classifier to identify the dominant emotion and create a personalized playlist from Spotify matching that emotion.

## 📦 Project Structure

```
that_one/
├── app.py                     # Main Flask app
├── playlist_creator/          # Playlist generation logic
├── spotify_api/               # Spotify API interaction
├── n_pl/                      # Natural Language Processing utilities
├── pre_processing/            # Preprocessing tools for text
├── training/                  # Machine learning training scripts
├── translator/                # Optional text translation module
├── web/                       # Frontend static files and templates
├── templates/                 # HTML templates for the web interface
├── requirements.txt           # Python dependencies
├── Procfile                   # For deploying to Heroku or similar services
└── README.md
```

## 🚀 Features

- Detects emotion from user-input text using a trained NLP classifier.
- Creates emotion-based Spotify playlists via the Spotify Web API.
- Web interface built with Flask and styled using Bootstrap.
- Includes multilingual support via a translator module.
- Clean project separation between frontend, backend, and ML logic.

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/KaulitzGuimaraes/that_one.git
   cd that_one
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Spotify API credentials (Client ID and Secret) in `spotify_api/spotifymanager.py`.

## 📊 Model & Data

- **Emotion Classifier**: Trained using a Bag-of-Words model and stored in `Classifier.bin`.
- **Training Data**: Merged dataset saved as `merged_training.pkl`.
- **Predictions**: Saved JSON files for testing and validation.

## 🌐 Run the App

```bash
python app.py
```

Then, open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📑 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

Created by [KaulitzGuimaraes](https://github.com/KaulitzGuimaraes) — feel free to reach out for collaboration or feedback!
