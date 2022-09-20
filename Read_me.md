To Activate environment 
conda activate moviepred
conda install pip
pip freeze > requirement.txt
pip install -r requirement.txt

to run FastAPI 
uvicorn app:app --reload