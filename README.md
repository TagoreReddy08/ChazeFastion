# ChazeFashion Product Catalog

Link: **https://chaze-fashion-website.onrender.com/**

**Note:** This repository is part of a class project for academic purposes.

## Setup

1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd ProductCatlog
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## Deployment (Render/Railway)

1. Ensure `gunicorn` is in `requirements.txt` and `Procfile` exists:
   ```
   web: gunicorn ChazeFashion.wsgi
   ```
2. Push your code to GitHub.
3. Connect your repo to Render or Railway and deploy as a Django app.
4. Set environment variables (e.g., `DJANGO_SECRET_KEY`, `DEBUG=False`).
5. Your site will be live at the provided URL.

## Features
- Modern, responsive UI (TailwindCSS)
- Add to Cart, View Cart, Remove from Cart, Total Price
- Product listing, detail, and wishlist

## License
MIT
