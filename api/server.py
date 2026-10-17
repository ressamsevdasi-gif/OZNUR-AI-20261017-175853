import json,re,io
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import zipfile

ROOT=Path(__file__).resolve().parent.parent
WEB=ROOT/"web"; HOST="127.0.0.1"; PORT=8788

def analyze(data,name):
    files=[]; text_files=[]; extmap={}; lines=chars=code=0
    text_ext={"py","pyw","js","jsx","ts","tsx","java","kt","kts","c","cpp","h","hpp","cs","go","rs","php","rb","swift","dart","sh","ps1","html","css","json","xml","yaml","yml","toml","md","txt"}
    code_ext={"py","pyw","js","jsx","ts","tsx","java","kt","kts","c","cpp","cs","go","rs","php","rb","swift","dart","sh","ps1"}
    with zipfile.ZipFile(data) as z:
        for info in z.infolist():
            if info.is_dir(): continue
            n=info.filename
            files.append({"path":n,"size":info.file_size})
            ex=Path(n).suffix.lower().lstrip(".") or "[uzantısız]"
            extmap[ex]=extmap.get(ex,0)+1
            if ex in text_ext and info.file_size<=4_000_000:
                try:
                    t=z.read(info).decode("utf-8","replace")
                    text_files.append({"path":n,"size":info.file_size,"text":t})
                    chars+=len(t); lines+=len(t.splitlines())
                    if ex in code_ext: code+=1
                except Exception: pass
    return {"name":name,"summary":{"files":len(files),"text_files":len(text_files),"code_files":code,"lines":lines,"characters":chars,"extensions":extmap,"description":"ZIP içeriği yalnızca okunmuş ve yapısal olarak analiz edilmiştir. Kod çalıştırılmamıştır."},"files":files,"textFiles":text_files,"tree":"\n".join("├─ "+f["path"] for f in files[:1200])}

class H(BaseHTTPRequestHandler):
    def out(self,status,data,typ="text/plain; charset=utf-8"):
        self.send_response(status);self.send_header("Content-Type",typ);self.send_header("Cache-Control","no-store");self.end_headers();self.wfile.write(data)
    def do_GET(self):
        p=urlparse(self.path).path
        if p=="/api/health":
            return self.out(200,b'{"ok":true,"mode":"read_only","execution":false}',"application/json")
        if p=="/": p="/index.html"
        fp=(WEB/p.lstrip("/")).resolve()
        if WEB.resolve() not in fp.parents and fp!=WEB.resolve(): return self.out(403,b"Forbidden")
        if not fp.is_file(): return self.out(404,b"Not found")
        types={".html":"text/html; charset=utf-8",".js":"text/javascript; charset=utf-8",".webmanifest":"application/manifest+json",".svg":"image/svg+xml"}
        return self.out(200,fp.read_bytes(),types.get(fp.suffix,"application/octet-stream"))
    def do_POST(self):
        ln=int(self.headers.get("Content-Length","0")); body=self.rfile.read(ln)
        if self.path=="/api/analyze":
            m=re.search(br'filename="([^"]+)"',body); start=body.find(b"PK\x03\x04")
            if not m or start<0:return self.out(400,b"invalid multipart/zip")
            end=body.rfind(b"PK\x05\x06"); end=len(body) if end<0 else min(len(body),end+22+65535)
            try:
                result=analyze(io.BytesIO(body[start:end]),m.group(1).decode("utf-8","replace"))
                return self.out(200,json.dumps(result,ensure_ascii=False).encode(),"application/json; charset=utf-8")
            except Exception as e:return self.out(400,str(e).encode())
        if self.path=="/api/query":
            try:o=json.loads(body or b"{}"); q=str(o.get("question","")); s=o.get("project",{}).get("summary",{})
            except Exception:return self.out(400,b"invalid json")
            ans=f"Yerel API proje özeti: {s.get('files',0)} dosya, {s.get('code_files',0)} kod dosyası, {s.get('lines',0)} satır, {s.get('characters',0)} karakter. Soru: {q}. Kod çalıştırma kapalıdır."
            return self.out(200,json.dumps({"answer":ans},ensure_ascii=False).encode(),"application/json; charset=utf-8")
        return self.out(404,b"Not found")

if __name__=="__main__":
    print(f"ÖZNUR AI API: http://{HOST}:{PORT}")
    print("READ ONLY / CODE EXECUTION DISABLED")
    ThreadingHTTPServer((HOST,PORT),H).serve_forever()
