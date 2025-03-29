from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import qrcode
from io import BytesIO

app = FastAPI()

# Enable CORS so the frontend can access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this to restrict access)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/generate_qr/")
async def generate_qr(data: str = Query(..., min_length=1)):
    """Generate a QR Code and return it as an image."""
    # Generate QR Code
    qr = qrcode.make(data)

    # Save QR code to an in-memory buffer
    img_io = BytesIO()
    qr.save(img_io, format="PNG")
    img_io.seek(0)  # Move cursor to the beginning

    # Return the image as a response
    return StreamingResponse(img_io, media_type="image/png")
