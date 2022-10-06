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
<table>
<tr><th>index</th><th> Top Gun </th><th>Terminator</th></tr>
<tr><td>Top Gun</td><td> 0</td><td>.25</td></tr>
<tr><td>Terminator</td><td> .5 </td><td>0</td></tr>
</table>

when user select any movies we sort this based on similarity and return.

<div align="center">
    <img src="/static/Front_Page.JPG" width="400px"</img> 
</div>