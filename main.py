import pickle
import numpy as np
import PIL.Image
import PIL.ImageOps

with open('mnist_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict-image/")
async def predict_image(UploadFile = File(...)):
    contents = await file.read()
    pil_image = Image.open(io.BytesIO((contents)).convert("L"))
    pil_image = PIL.ImageOps.invert(pil_image)
    pil_image = pil_image.resize((28,28), PIL.Image.ANTIALIAS)
    img_array = np.array(pil_image).reshape(1,-1)
    prediction = model.predict(img_array)
    return {"prediction" : int(prediction[0])}


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}