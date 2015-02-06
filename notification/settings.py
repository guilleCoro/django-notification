from django.conf import settings

# the templates to be used by notification
EMAIL_SUBJECT_TEMPLATE = getattr(settings, 'NOTIFICATION_EMAIL_SUBJECT_TEMPLATE', 'notification/email_subject.txt')
EMAIL_BODY_PLAIN_TEMPLATE = getattr(settings, 'NOTIFICATION_EMAIL_BODY_PLAIN_TEMPLATE', 'notification/email_body.txt')
EMAIL_BODY_HTML_TEMPLATE = getattr(settings, 'NOTIFICATION_EMAIL_BODY_HTML_TEMPLATE', 'notification/email_body.html')

# the place where to look for templates for specific notice types -- must be terminated with a slash
TEMPLATE_ROOT = getattr(settings, 'NOTIFICATION_TEMPLATE_ROOT', 'notification/')

# use celery for sending messages
USE_CELERY = getattr(settings, 'NOTIFICATION_USE_CELERY', False)
