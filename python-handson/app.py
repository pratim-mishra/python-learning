import os
import uuid
import pandas as pd

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

from src.pipeline.inference import run_full_pipeline

from fastapi.middleware.cors import CORSMiddleware
os.makedirs("data", exist_ok=True)

app = FastAPI(
    title="Customer Support QA Evaluator",
    version="1.0"
)


# CORS (Cross-Origin Resource Sharing) middleware controls which websites or
# applications are allowed to communicate with our FastAPI application.
#
# Here, we are allowing requests from ANY origin, using ANY HTTP method
# (GET, POST, PUT, DELETE, etc.), and sending ANY HTTP headers.
#
# This is useful during development because it allows our frontend and
# backend to communicate even when they are running on different URLs/ports.
#
# NOTE: In a production application, it is safer to replace "*" with the
# specific frontend origins that should be allowed to access the API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"message": "QA Evaluator API is running"}


@app.post("/evaluate-file")
async def evaluate_file(file: UploadFile = File(...)):

    # -----------------------------
    # Validate file type
    # -----------------------------
    
    allowed_extensions = [".csv", ".xlsx"]

    file_extension = os.path.splitext(file.filename)[1].lower()

    if file_extension not in allowed_extensions:
        return {
            "error": "Please upload a CSV or XLSX file"
        }

    # -----------------------------
    # Create temporary paths
    # -----------------------------

    input_path = f"data/{uuid.uuid4()}{file_extension}"
    output_path = f"data/output_{uuid.uuid4()}.xlsx"

    # -----------------------------
    # Save uploaded file
    # -----------------------------

    # “Start reading the file, and while waiting for it to finish, the server can do other work.”

    with open(input_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # -----------------------------
    # Load dataframe dynamically
    # -----------------------------

    if file_extension == ".csv":
        df = pd.read_csv(input_path)

    elif file_extension == ".xlsx":
        df = pd.read_excel(input_path)

    # -----------------------------
    # Run pipeline
    # -----------------------------

    output_df = run_full_pipeline(df)

    # -----------------------------
    # Save output
    # -----------------------------

    output_df.to_excel(output_path, index=False)

    # -----------------------------
    # Return output file
    # -----------------------------

    return FileResponse(
        path=output_path,
        filename="qa_output.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )