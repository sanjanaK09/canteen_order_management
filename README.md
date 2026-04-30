# Canteen Management System

A Django-based online canteen management system with food ordering, wishlist, and OTP-based authentication.

## Features

- 🍔 Browse food menu
- 🛒 Shopping cart functionality
- ❤️ Wishlist management
- 📱 OTP-based login
- 💳 Multiple payment methods
- 📊 Admin dashboard for food management
- ✅ Full test coverage
- 🔒 Security hardened

## Tech Stack

- **Backend**: Django 6.0.4
- **Database**: SQLite (development)
- **Frontend**: HTML, CSS
- **Testing**: Django TestCase
- **Code Quality**: Pylint, Black, Flake8, isort
- **CI/CD**: GitHub Actions
- **Security Scanning**: Bandit, Safety, SonarQube

## Prerequisites

- Python 3.9+
- pip or virtual environment manager
- Git

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/canteen_project.git
   cd canteen_project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser.

## Usage

### Admin Panel
- Navigate to `http://127.0.0.1:8000/admin/`
- Login with superuser credentials
- Add food items with images and prices

### User Features
- Browse menu at homepage
- Add items to cart
- Checkout and select payment method
- Add items to wishlist (requires login)

## Development

### Code Quality Tools

Run linting:
```bash
pylint app/ canteen_project/
```

Format code:
```bash
black app/ canteen_project/
```

Check imports:
```bash
isort app/ canteen_project/
```

Run tests:
```bash
python manage.py test
```

Run tests with coverage:
```bash
coverage run --source='app' manage.py test
coverage report
coverage html
```

### Django Security Checks
```bash
python manage.py check --deploy
```

## Project Structure

```
canteen_project/
├── app/
│   ├── migrations/          # Database migrations
│   ├── static/             # CSS, JS, images
│   ├── templates/          # HTML templates
│   ├── models.py           # Database models
│   ├── views.py            # Views logic
│   ├── urls.py             # App URL routing
│   └── admin.py            # Admin configuration
├── canteen_project/        # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI app
├── .github/workflows/      # CI/CD pipelines
├── .pylintrc               # Pylint configuration
├── sonar-project.properties # SonarQube configuration
├── requirements.txt        # Python dependencies
├── manage.py              # Django management
└── README.md              # This file
```

## GitHub Actions Workflows

### 1. Code Linting & Quality (`.github/workflows/lint.yml`)
- Runs pylint, black, flake8, isort
- Tests on Python 3.9, 3.10, 3.11

### 2. Django Tests (``.github/workflows/django-tests.yml`)
- Runs Django migrations
- Executes test suite
- Generates coverage reports
- Runs security checks

### 3. SonarQube Scan (`.github/workflows/sonarqube.yml`)
- Code quality analysis
- Coverage reporting
- Codecov integration

### 4. Security Scan (`.github/workflows/security.yml`)
- Bandit security scanning
- Dependency vulnerability checks
- Secret detection

## Configuration

### Environment Variables

Create `.env` file (copy from `.env.example`):

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
FAST2SMS_API_KEY=your-api-key
```

### Settings.py

Key settings are now environment-aware:
- `DEBUG`: Controlled via env variable
- `SECRET_KEY`: Read from environment
- `ALLOWED_HOSTS`: Comma-separated from env
- `FILE_UPLOAD_MAX_MEMORY_SIZE`: Configurable file upload limit

## Security Considerations

⚠️ **Important for Production**:

1. Set `DEBUG=False` in production
2. Use strong `SECRET_KEY`
3. Set `ALLOWED_HOSTS` to your domain
4. Enable `CSRF_COOKIE_SECURE=True`
5. Enable `SESSION_COOKIE_SECURE=True`
6. Use environment variables for sensitive data
7. Implement file upload validation
8. Add rate limiting on OTP endpoints
9. Use HTTPS only
10. Set up proper logging

See [SECURITY.md](SECURITY.md) for detailed security guidelines.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### Quick Start for Contributors

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit a Pull Request

## CI/CD Pipeline

All pull requests are automatically tested:

- ✅ Code linting (Pylint, Black, Flake8)
- ✅ Django tests
- ✅ Code coverage
- ✅ Security scanning
- ✅ SonarQube analysis

Merge only happens when all checks pass.

## Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test app

# Run with verbose output
python manage.py test -v 2

# Run with coverage
coverage run --source='app' manage.py test
coverage report
coverage html  # Generate HTML report
```

## Deployment

### Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Use strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use PostgreSQL instead of SQLite
- [ ] Enable HTTPS
- [ ] Configure proper logging
- [ ] Set up static/media file serving (AWS S3, Nginx, etc.)
- [ ] Run security checks: `python manage.py check --deploy`
- [ ] Set up monitoring and alerting
- [ ] Configure database backups

### Deployment Options

- **Heroku**: `git push heroku main`
- **Railway**: Connect GitHub repo
- **DigitalOcean App Platform**: Connect GitHub repo
- **AWS EC2**: Use gunicorn + Nginx
- **PythonAnywhere**: Upload and configure

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## Known Issues & Limitations

- [ ] OTP not expiring (implement TTL)
- [ ] No rate limiting on OTP verification
- [ ] Cart stored in session (consider database storage)
- [ ] Media files served by Django (use Nginx/S3 in production)
- [ ] No file upload validation (add in production)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, open an issue on [GitHub Issues](https://github.com/yourusername/canteen_project/issues).

## Authors

- Your Name - Initial work

## Changelog

### Version 1.0.0
- Initial release
- Food menu browsing
- Cart functionality
- OTP-based authentication
- Admin dashboard
- Full CI/CD setup
