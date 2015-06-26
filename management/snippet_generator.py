from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
import random
import string

digits = "".join( [random.choice(string.digits) for i in xrange(8)] )
chars = "".join( [random.choice(string.letters) for i in xrange(15)] )
snippets = []
 
for i in range(50):
    snippet = Snippet(title='snippet%d' % i, 
                code=digits + chars,
                language=random.choice(LANGUAGE_CHOICES)[0],
                style=random.choice(STYLE_CHOICES)[0],
                owner=User.objects.order_by('?').first())
    snippets.append(snippet)
 
Snippet.objects.bulk_create(snippets)