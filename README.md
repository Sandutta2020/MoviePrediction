To Activate environment 
***********************************
conda activate moviepred
conda install pip
pip freeze > requirement.txt
pip install -r requirement.txt
**************************************
to run FastAPI 
uvicorn app:app --reload
**************************************
Limitation : only limited list will be displayed for better explanation

The Reason  of This app is to find similar movies  based on user recommendation and movie keywords and movie genre type

In our analysis part we already created 2  matrix based on similarty between each movies

consider we have 2 movies 
1) Top Gun
2) Terminator

The matrix will be like 
          <br>| Top Gun | Terminator|<br>
          ----------------------<br>
Top Gun   |    0    |   .25<br>
           ---------------------<br>
Terminator|   .5     |    0<br>
          ---------------------<br>

when user select any movies we sort this based on similarity and return.