
# Tech Stack

**Backend:** DRF

**Frontend:** Jinja2, Pure JS

**Server:** Gunicorn

**Services:** Docker, PostgreSQL


# Run Locally with docker-compose


```bash
  docker-compose up -d
```

# Run Locally without docker-compose (SQLite)


```bash
  python manage.py migrate --settings=config.settings.dev
```

```bash
  python manage.py runserver --settings=config.settings.dev
```

https://stripe-django-oy9j.onrender.com/core/shop/products/
