from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '_site')
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag in ('a','link','script'):self.links.append(d.get('href',d.get('src','')))
errors=[];count=0
for p in root.rglob('*.html'):
 parser=Parser();parser.feed(p.read_text());count+=1
 for link in parser.links:
  u=urlsplit(link)
  if u.scheme or u.netloc or not u.path:continue
  target=root/unquote(u.path.lstrip('/')) if u.path.startswith('/') else p.parent/unquote(u.path)
  if not target.exists():errors.append((str(p.relative_to(root)),u.path))
print('HTML pages:',count,'Broken internal links:',errors)
assert not errors
