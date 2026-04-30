# Contributing to Canteen Management System

Thank you for considering contributing to our project! Here's how you can help.

## Code of Conduct

Be respectful, inclusive, and constructive in all interactions.

## How to Contribute

### Reporting Bugs

1. Check [GitHub Issues](https://github.com/yourusername/canteen_project/issues) for existing reports
2. Create a new issue with:
   - Clear title
   - Detailed description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment (OS, Python version, etc.)
   - Screenshots if applicable

### Suggesting Features

1. Check [GitHub Issues](https://github.com/yourusername/canteen_project/issues)
2. Create an issue with:
   - Clear title (start with "Feature Request:")
   - Description of the feature
   - Use cases and benefits
   - Possible implementation approach

### Submitting Code

#### 1. Setup Development Environment

```bash
git clone https://github.com/yourusername/canteen_project.git
cd canteen_project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number
```

#### 3. Make Your Changes

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Write clear, descriptive commit messages
- Add tests for new functionality
- Update documentation as needed

#### 4. Run Quality Checks

```bash
# Format code
black app/ canteen_project/

# Lint code
pylint app/ canteen_project/

# Check imports
isort app/ canteen_project/

# Run tests
python manage.py test

# Check coverage
coverage run --source='app' manage.py test
coverage report
```

#### 5. Commit & Push

```bash
git add .
git commit -m "feat: Add your feature description"
git push origin feature/your-feature-name
```

#### 6. Submit Pull Request

- Go to GitHub and create Pull Request
- Link any related issues: `Closes #123`
- Describe your changes clearly
- Wait for reviews and CI/CD checks to pass

## Code Standards

### Python Style

```python
# Use type hints where possible
def add_to_cart(request: HttpRequest, item_id: int) -> HttpResponse:
    """Add item to shopping cart.
    
    Args:
        request: HTTP request object
        item_id: ID of item to add
        
    Returns:
        Redirect to cart page
    """
    pass

# Use meaningful variable names
for item in cart_items:  # Good
for i in items:         # Avoid

# Keep functions small and focused
# Max line length: 100 characters
```

### Django Best Practices

```python
# In models.py
class MyModel(models.Model):
    """Clear docstring explaining the model."""
    
    name = models.CharField(max_length=100, help_text="Item name")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "My Models"
    
    def __str__(self):
        return self.name

# In views.py
def my_view(request):
    """Clear docstring explaining the view."""
    items = MyModel.objects.filter(active=True)
    return render(request, 'template.html', {'items': items})

# Use decorators for authentication
@login_required
def protected_view(request):
    pass
```

### Testing Requirements

```python
# app/tests.py
from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
    """Test cases for MyModel."""
    
    def setUp(self):
        """Create test data."""
        MyModel.objects.create(name="Test Item")
    
    def test_model_creation(self):
        """Test that model creates correctly."""
        item = MyModel.objects.get(name="Test Item")
        self.assertEqual(item.name, "Test Item")
    
    def test_model_string_representation(self):
        """Test __str__ method."""
        item = MyModel.objects.get(name="Test Item")
        self.assertEqual(str(item), "Test Item")
```

## Commit Message Format

Use conventional commits:

```
feat: Add new feature description
fix: Fix bug in component
docs: Update documentation
style: Format code
refactor: Refactor component without behavior change
test: Add tests
chore: Update dependencies
```

Examples:
```
feat: Add wishlist functionality
fix: Fix OTP validation timeout issue
docs: Update deployment guide
test: Add tests for checkout view
```

## Pull Request Process

1. **Update** the README.md with new features/changes
2. **Add tests** for new functionality (aim for >80% coverage)
3. **Ensure** all checks pass:
   - ✅ Linting (Pylint, Black, Flake8)
   - ✅ Tests pass
   - ✅ No new warnings
   - ✅ SonarQube quality gate passes
4. **Request review** from maintainers
5. **Address feedback** promptly
6. **Merge** only after approval

## Development Tips

### Run Tests Locally

```bash
# All tests
python manage.py test

# Specific app
python manage.py test app

# Specific test class
python manage.py test app.tests.MyTestCase

# Specific test method
python manage.py test app.tests.MyTestCase.test_method

# With verbose output
python manage.py test -v 2

# Stop on first failure
python manage.py test --failfast
```

### Check Coverage

```bash
coverage run --source='app' manage.py test
coverage report
coverage html  # Open htmlcov/index.html
```

### Debug Mode

```python
# In views.py
from django.db import connection
from django.conf import settings

if settings.DEBUG:
    print("Debug info:", variable)
    print(f"Query count: {len(connection.queries)}")
```

### Database Reset

```bash
# Delete all migrations (except __init__.py)
# Then run:
python manage.py makemigrations
python manage.py migrate
```

## Common Issues

### Import Errors

```bash
# Ensure app is in INSTALLED_APPS in settings.py
# Reinstall dependencies:
pip install -r requirements.txt --upgrade
```

### Database Issues

```bash
# Reset database
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Tests Failing

```bash
# Run with verbose output
python manage.py test -v 2

# Run specific test
python manage.py test app.tests.MyTest.test_method --failfast
```

## Release Process

Only maintainers can create releases:

1. Update version in appropriate files
2. Create git tag: `git tag v1.0.0`
3. Push tag: `git push origin v1.0.0`
4. GitHub Actions will automatically create a release

## Questions?

- Open an issue with your question
- Check existing documentation
- Discuss in GitHub Discussions

Thank you for contributing! 🎉
