"""把 src/lessonN/lessonN.src.html 建置成 lessonN/index.html（Skulpt 內嵌，可離線）。
用法：python3 tools/build.py 1
"""
import sys, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
n = sys.argv[1]
src_path = os.path.join(ROOT, 'src', f'lesson{n}', f'lesson{n}.src.html')
out_dir = os.path.join(ROOT, f'lesson{n}')
lib_dir = os.path.join(ROOT, 'tools', 'skulpt')
src = open(src_path, encoding='utf8').read()
sk = open(os.path.join(lib_dir, 'skulpt.min.js'), encoding='utf8').read().replace('</script', '<\\/script').replace('\ufffd', '\\ufffd')
lib = open(os.path.join(lib_dir, 'skulpt-stdlib.js'), encoding='utf8').read().replace('</script', '<\\/script')
cdn = re.findall(r'<script src="https://cdn\.jsdelivr\.net/npm/skulpt@[^"]+/dist/(skulpt\.min\.js|skulpt-stdlib\.js)"></script>', src)
assert cdn == ['skulpt.min.js', 'skulpt-stdlib.js'], cdn
body = re.sub(r'<script src="https://cdn\.jsdelivr\.net/npm/skulpt@[^"]+/dist/skulpt\.min\.js"></script>', lambda m: '<script>/* Skulpt (MIT) https://skulpt.org */\n' + sk + '</script>', src, count=1)
body = re.sub(r'<script src="https://cdn\.jsdelivr\.net/npm/skulpt@[^"]+/dist/skulpt-stdlib\.js"></script>', lambda m: '<script>' + lib + '</script>', body, count=1)
i = body.index('</style>') + len('</style>')
head, rest = body[:i], body[i:]
os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, 'index.html')
open(out, 'w', encoding='utf8').write('<!doctype html>\n<html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n' + head + '</head><body>' + rest + '</body></html>\n')
print(out, os.path.getsize(out) // 1024, 'KB')
