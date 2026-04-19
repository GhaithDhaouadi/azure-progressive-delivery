from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    version = os.getenv("APP_VERSION", "v1-blue")
    color = "blue" if "blue" in version else "green"
    return f"""
    <html>
        <head>
            <title>Ghaith - Azure DevOps Project</title>
            <style>
                body {{ 
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    max-width: 800px; margin: 100px auto; padding: 20px;
                    text-align: center; background: #0f172a; color: #f8fafc;
                }}
                .status {{ font-size: 48px; font-weight: bold; color: {'#3b82f6' if color == 'blue' else '#22c55e'}; }}
                .version {{ 
                    background: #1e293b; padding: 10px 20px; border-radius: 8px;
                    display: inline-block; margin: 20px;
                }}
                .badge {{
                    background: {color}; color: white; padding: 5px 15px;
                    border-radius: 20px; font-weight: bold;
                }}
                a {{ color: #60a5fa; }}
            </style>
        </head>
        <body>
            <div class="status">✅ {version.upper()} ACTIVE</div>
            <div class="version">
                <span class="badge">{color.upper()}</span>
            </div>
            <p>Production-Ready CI/CD Pipeline with Progressive Delivery on Azure</p>
            <p>Ghaith Dhaouadi - Cloud DevOps Engineer</p>
            <hr style="border-color: #334155; margin: 30px 0;">
            <p style="color: #94a3b8;">
                <a href="/health">Health Check</a> | 
                <a href="/docs">API Docs</a>
            </p>
        </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "healthy"}
