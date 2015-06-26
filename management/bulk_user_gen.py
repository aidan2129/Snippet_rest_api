# execfile('management/bulk_user_gen.py') in python manage.py shell

from django.contrib.auth.models import User
import names
users = []

for i in range(100):
    user = User(first_name=names.get_first_name(), 
                last_name=names.get_last_name(),
                username=names.get_first_name() + '%d' % i,
                email='%s@mydomain.com' % names.get_first_name(),
                password='test',
                is_active=True, )
    users.append(user)
 
User.objects.bulk_create(users)