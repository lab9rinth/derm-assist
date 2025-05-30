# Derm-Assist - AI-Powered Dermatology Assistant

An AI-powered dermatology assistant platform for India's youth, providing instant skin condition screening and analysis.

## Tech Stack

- Backend: FastAPI
- Database: MongoDB
- Frontend: HTML, CSS, JavaScript
- Templates: Jinja2

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up MongoDB:
- Install MongoDB Community Edition
- Start MongoDB service
- Create a database named 'derm-assist'

4. Create a .env file in the project root with the following variables:
```
MONGODB_URL=mongodb://localhost:27017
SECRET_KEY=your-secret-key-here
ENVIRONMENT=development
```

5. Run the application:
```bash
uvicorn main:app --reload
```

The application will be available at http://localhost:8000

## Project Structure

```
dermato_ai/
├── main.py              # FastAPI application
├── requirements.txt     # Project dependencies
├── .env                # Environment variables
├── static/            # Static files
│   ├── css/          # CSS files
│   ├── js/           # JavaScript files
│   └── images/       # Image assets
└── templates/        # HTML templates
```

## Features

- AI-Powered Skin Condition Screening
- Mole Tracking
- Explainable Reports
- Dermatologist Review System
- Multilingual Support
- Privacy-First Approach

## Contributing

Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License. 
