# Real Estate Price Prediction - Namma Bengaluru

A simple **Flask-based web API** to predict home prices in Bengaluru, India, using a pre-trained machine learning model.

This project allows users to get estimated prices for properties based on **location, square footage, number of bedrooms (BHK), and bathrooms**.

---

## Features

- Predict home prices in **Bengaluru**.
- Provides **location suggestions** and validation.
- **JSON API endpoints** for easy integration.
- Pre-trained model loaded from Hugging Face Hub.
- Error handling for invalid inputs.

---

## Folder Structure

server.py # Flask server code
util.py # Utility functions to load model and make predictions
