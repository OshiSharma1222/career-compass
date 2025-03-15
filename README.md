# Career Guidance Platform

A comprehensive career guidance platform built with Django that helps students and professionals make informed career decisions through AI-powered recommendations, mentor guidance, and community support.

## Features

- AI-based career recommendations
- Mentor matching and guidance
- Real-time community discussions
- Career events and workshops
- Expert-written blogs and resources
- Structured career roadmaps
- Social authentication
- Personalized dashboards

## Tech Stack

- Django 5.0.3
- Django REST Framework
- Tailwind CSS
- Channels (WebSockets)
- PostgreSQL
- Redis
- scikit-learn

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd career_guidance_platform
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Tailwind CSS dependencies:
```bash
python manage.py tailwind install
```

5. Set up environment variables:
Create a `.env` file in the root directory with:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/career_guidance_db
REDIS_URL=redis://localhost:6379/0
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Start the development server:
```bash
python manage.py runserver
```

9. In a separate terminal, start the Tailwind CSS watcher:
```bash
python manage.py tailwind start
```

## Project Structure

- `users/` - User authentication and profiles
- `careers/` - Career recommendations and roadmaps
- `mentors/` - Mentor profiles and guidance
- `community/` - Forums and discussions
- `events/` - Career events management
- `exams/` - Competitive exams info
- `blogs/` - Career insights and articles

## Contributing

Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.