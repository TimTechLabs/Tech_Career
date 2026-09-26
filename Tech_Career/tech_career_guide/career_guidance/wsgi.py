import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'career_guidance.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
app = application
