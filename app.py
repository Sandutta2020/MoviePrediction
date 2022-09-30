from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from Getting_recommendation import getting_recommended_movie
from utilities import read_yaml

movie_config = read_yaml("config.yaml", "Movie_details")
lst = movie_config["Movie_list_dropdown"]
lst = lst[0:movie_config['Default_list_size']]
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
        "form1.html", context={"request": request, "movies": lst}
    )


@app.post("/render", response_class=HTMLResponse)
async def render(request: Request, category_id: str = Form(...)):
    # print(category_id)
    df_movies = getting_recommended_movie(category_id)
    df_movies.reset_index(inplace=True)
    df_movies['Similar Movies'] =df_movies['Title'] + '--------- ' + df_movies['SearchType']
    df_movies=df_movies[['Similar Movies']]
    #print(df_movies.to_html())
    return templates.TemplateResponse(
        "form1.html",
        context={
            "request": request,
            "Res": category_id,
            "movies": lst,
            "rec_movies": df_movies.head(movie_config['Result_size']).to_html(
                border=1, index=False,table_id="result_movies"
            ),
        },
    )


# main
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
