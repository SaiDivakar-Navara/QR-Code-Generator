from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import qrcode
from io import BytesIO

app = FastAPI()

# CORS (optional but fine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend static files
app.mount("/static", StaticFiles(directory="Frontend"), name="static")

# Serve - index.html
@app.get("/")
def serve_frontend():
    return FileResponse("Frontend/index.html")

# QR generation API
@app.get("/generate_qr")
async def generate_qr(data: str = Query(..., min_length=1)):
    qr = qrcode.make(data)
    img_io = BytesIO()
    qr.save(img_io, format="PNG")
    img_io.seek(0)
    return StreamingResponse(img_io, media_type="image/png")
