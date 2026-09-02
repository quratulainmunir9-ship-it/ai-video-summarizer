# AI Video Summarizer

## AI-Powered Video Summarization Platform

AI Video Summarizer is a full-stack application designed to help users understand lengthy video content more efficiently. The project processes video content and uses AI-based analysis to generate concise, meaningful summaries.

The project was developed as a **Final Year Project (FYP)** using a React frontend, Django backend, and AI-powered video processing pipeline.

---

## Overview

Long videos can contain a large amount of information, making it time-consuming to watch and review the complete content.

This project addresses that problem by providing an AI-assisted workflow that transforms video content into a more accessible and concise summary.

The application is designed to help users:

* Process video content
* Analyze the information contained in videos
* Generate concise summaries
* Understand important content without watching the entire video

---

## Key Features

### 🎥 Video Processing

Users can provide video content for processing through the application.

### 🤖 AI-Powered Summarization

The system uses AI-based processing to analyze video content and generate a concise summary.

### 📝 Content Understanding

The generated output helps users quickly understand the main information contained in a video.

### 🌐 Full-Stack Architecture

The application combines a modern frontend with a backend API and AI processing workflow.

### 🚀 Deployed Application

A production deployment is available for testing and demonstration.

**Live Demo:**
https://ai-video-summarizer-tau.vercel.app/

---

## System Architecture

```text
                User
                  |
                  v
        +-------------------+
        |   React Frontend  |
        |   User Interface  |
        +---------+---------+
                  |
                  v
        +-------------------+
        |   Django Backend  |
        |    API Layer      |
        +---------+---------+
                  |
                  v
        +-------------------+
        |  AI Processing    |
        | Video Analysis &  |
        |   Summarization   |
        +---------+---------+
                  |
                  v
        +-------------------+
        |  Generated Video  |
        |     Summary       |
        +-------------------+
```

---

## Technology Stack

| Component            | Technology                |
| -------------------- | ------------------------- |
| Frontend             | React                     |
| Backend              | Django                    |
| Programming Language | Python                    |
| AI                   | AI-based video processing |
| Deployment           | Vercel                    |
| Version Control      | Git & GitHub              |

---

## Project Structure

```text
ai-video-summarizer/
|
+-- ai-video-summarizer/
|   +-- frontend application
|
+-- backend/
|   +-- Django backend
|   +-- API
|   +-- AI processing
|
+-- README.md
+-- .gitignore
```

---

## How It Works

The application follows a simple processing workflow:

```text
Upload / Provide Video
          |
          v
    Video Processing
          |
          v
      AI Analysis
          |
          v
   Content Extraction
          |
          v
   Summary Generation
          |
          v
    User Views Summary
```

The architecture is designed to separate the user interface, backend services, and AI processing components.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/quratulainmunir9-ship-it/ai-video-summarizer.git
cd ai-video-summarizer
```

### 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the Django development server:

```bash
python manage.py runserver
```

### 3. Frontend Setup

Open another terminal and navigate to the frontend directory.

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm start
```

> The exact frontend setup may vary depending on the configuration of the current React application.

---

## Future Development — VIDNEX

The project can be extended beyond basic summarization into a more complete **AI Video Intelligence & Evidence Engine**.

Potential future capabilities include:

* Timestamp-based evidence extraction
* Searchable video evidence
* Chapter generation
* Evidence-linked summaries
* Question answering over video content
* Key-event detection
* Important moment identification
* Structured video insights
* Evidence-backed AI responses
* Video intelligence dashboard

The long-term goal is to move from simply asking:

> **“What is this video about?”**

toward:

> **“What happened, where did it happen, and what evidence from the video supports it?”**

---

## Project Type

**Final Year Project (FYP)**

**Domain:** Artificial Intelligence / Video Intelligence

**Architecture:** Full Stack

**Frontend:** React

**Backend:** Django

---

## Project Status

The current version is a functional AI Video Summarizer prototype.

The project is also being explored for further development into a more advanced **AI Video Intelligence & Evidence Engine (VIDNEX)**.

---

## Author

**Quratulain Munir**

BS Computer Science Graduate

GitHub:
https://github.com/quratulainmunir9-ship-it

---

## License

This project was developed as an academic Final Year Project.
