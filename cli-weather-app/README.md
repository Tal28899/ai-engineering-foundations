# CLI Weather App

A command-line tool that fetches and displays live weather data for a given city using a public weather API.

## What this demonstrates

- Making HTTP requests to a third-party REST API (`requests` library)
- Parsing and handling JSON API responses
- Secure API key management using environment variables (`python-dotenv`)
- Basic error handling for failed requests and invalid input
- Building a usable command-line interface with a loop for repeated queries

## Tech stack

Python · `requests` · `python-dotenv` · OpenWeatherMap API

## Setup

```bash
cd cli-weather-app
pip install -r requirements.txt
cp .env.example .env   # then add your own OpenWeatherMap API key
python weather_cli.py
```

## Example usage

```
Enter city name: Lahore
Fetching weather for Lahore...
Temperature: 34°C
Condition: Clear sky
```

## Notes

This was built as a foundational exercise in API integration and error handling — patterns that carry directly into working with LLM and RAG-related APIs.
