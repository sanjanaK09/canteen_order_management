# Security Policy

## Reporting Security Vulnerabilities

**Please DO NOT open public issues for security vulnerabilities.**

If you discover a security vulnerability in this project, please email: `security@youremail.com`

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if you have one)

We will acknowledge receipt within 48 hours and provide regular updates.

## Security Best Practices

### For Users

1. **Keep Dependencies Updated**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Use Environment Variables**
   - Never commit `.env` file
   - Use `.env.example` as template
   - Store secrets securely

3. **Change Default Credentials**
   - Change `SECRET_KEY` in production
   - Use strong passwords for superuser
   - Rotate API keys regularly

4. **Enable HTTPS**
   - Use HTTPS in production
   - Set `SECURE_SSL_REDIRECT = True`
   - Configure security headers

5. **Regular Updates**
   - Watch for security advisories
   - Update Django regularly
   - Monitor dependencies for vulnerabilities

### For Developers

1. **Code Security**
   ```python
   # ✅ Good: Use environment variables
   api_key = os.getenv('API_KEY')
   
   # ❌ Bad: Hardcode secrets
   api_key = "secret123"
   
   # ✅ Good: Validate user input
   if not isinstance(item_id, int):
       return HttpResponseBadRequest()
   
   # ❌ Bad: Direct SQL queries
   query = f"SELECT * FROM items WHERE id = {item_id}"
   ```

2. **Authentication**
   ```python
   # ✅ Use login_required decorator
   @login_required
   def protected_view(request):
       pass
   
   # ✅ Check permissions
   if request.user.is_authenticated:
       pass
   ```

3. **File Uploads**
   ```python
   from django.core.validators import FileExtensionValidator
   
   # ✅ Validate file extensions
   image = models.ImageField(
       validators=[FileExtensionValidator(['jpg', 'png'])]
   )
   
   # ✅ Limit file size
   FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
   ```

4. **Database**
   ```python
   # ✅ Use ORM (protects against SQL injection)
   items = Item.objects.filter(id=item_id)
   
   # ❌ Never use raw SQL with user input
   items = Item.objects.raw(f"SELECT * WHERE id = {item_id}")
   ```

5. **Logging**
   ```python
   import logging
   
   logger = logging.getLogger(__name__)
   
   # ✅ Don't log sensitive data
   logger.info(f"User {user_id} logged in")
   
   # ❌ Never log passwords or tokens
   logger.info(f"Password: {password}")
   ```

## Security Scanning

### Local Scanning

```bash
# Bandit: Find security issues
bandit -r app/ canteen_project/

# Safety: Check dependencies
safety check

# Pylint: Code quality
pylint app/ canteen_project/
```

### Django Security Checks

```bash
python manage.py check --deploy
```

### GitHub Workflows

- Automatically run on every push
- Check `.github/workflows/` for details
- Results available in GitHub Actions

## Security Headers

Configured in `settings.py`:

```python
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_SECURITY_POLICY = {...}
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
```

## Known Vulnerabilities

None currently known. See [Issues](https://github.com/yourusername/canteen_project/issues) for ongoing investigations.

## Security Advisories

Subscribe to:
- [Django Security Releases](https://www.djangoproject.com/weblog/)
- [Python Security](https://www.python.org/news/security/)
- [GitHub Security Advisories](https://github.com/advisories)

## Production Deployment Security

### Database
- Use PostgreSQL (not SQLite)
- Enable SSL connections
- Regular backups
- Access control

### Server
- Keep OS updated
- Firewall configured
- SSH key-based auth
- Fail2ban for rate limiting

### Application
- DEBUG = False
- ALLOWED_HOSTS configured
- HTTPS enforced
- Security headers set
- Monitoring enabled
- Logging configured

### Dependencies
- Pin exact versions
- Regular security updates
- Scan for vulnerabilities
- Remove unused packages

## Third-party Integrations

### Fast2SMS API
- Keep API key secret
- Rotate regularly
- Monitor usage
- Use HTTPS

### SonarQube
- Change default credentials
- Use HTTPS
- Regular backups
- Access control

## Changelog

All security fixes will be documented in [CHANGELOG](CHANGELOG.md).

---

**Last Updated**: April 2026
