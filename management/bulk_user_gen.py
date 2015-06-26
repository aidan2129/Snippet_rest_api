# execfile('management/bulk_user_gen.py') in python manage.py shell

from django.contrib.auth.models import User
import names
users = []

number = raw_input("How many users should be generated? ")

print "Generating users...."

for i in range(int(number)):
    user = User(first_name=names.get_first_name(), 
                last_name=names.get_last_name(),
                username=names.get_first_name() + '%d' % int(random.randrange(1000)),
                email='%s@mydomain.com' % names.get_first_name(),
                password='test',
                is_active=True, )
    users.append(user)
 
User.objects.bulk_create(users)