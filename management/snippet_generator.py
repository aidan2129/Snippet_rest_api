from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments import highlight
import random
import string

digits = "".join( [random.choice(string.digits) for i in xrange(8)] )
chars = "".join( [random.choice(string.letters) for i in xrange(15)] )
snippets = []


number = raw_input("How many snippets should be generated? ")

print "Generating snippets...."

for i in range(int(number)):
    title = 'snippet%d' % i,
    code = digits + chars
    language = random.choice(LANGUAGE_CHOICES)[0]
    style = random.choice(STYLE_CHOICES)[0]

    #generate highlighted html
    lexer = get_lexer_by_name(language)
    options =  {'title':title} or {}
    formatter = HtmlFormatter(style=style, full=True, **options)
    print options
    highlighted = highlight(code, lexer, formatter)

    snippet = Snippet(title=title[0], 
                code=code,
                language=language,
                style=style,
                owner=User.objects.order_by('?').first(),
                highlighted=highlighted)
    snippets.append(snippet)
 
Snippet.objects.bulk_create(snippets)