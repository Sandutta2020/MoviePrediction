from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import pandas as pd
from Getting_recommendation import getting_recommended_movie
df =pd.read_csv('data/Movie_list.csv')
#print(df.columns)
lst =list(df['Title'])
# initialization
app = FastAPI()

# mount static folder to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 template instance for returning webpage via template engine
templates = Jinja2Templates(directory="templates")

# serve webpage, GET method, return HTML
@app.get("/", response_class=HTMLResponse)
async def get_webpage(request: Request):
    return templates.TemplateResponse(
        "form1.html", 
        context={
            "request": request,
            "movies": lst
        }
    )


@app.post("/render", response_class=HTMLResponse)
async def render(
    request: Request,
    category_id: str =Form(...)
):
    #print(category_id)
    df_movies =getting_recommended_movie(category_id)
    #print(df_movies)
    return templates.TemplateResponse(
        "form1.html",
        context={
            "request": request,
            "Res": category_id,
            "movies": lst,
            "rec_movies": df_movies.head(10).to_html(border =1,index=True,show_dimensions =True)
        },
    )


# main
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)