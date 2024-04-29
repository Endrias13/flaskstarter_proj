git clone git@github.com:Endrias13/flaskstarter_proj.git

cd flaskstarter_proj

python3 -m venv ~/.myrepo

source ~/.myrepo/bin/activate

make -f Makefile_Task_1 all

git clone git@github.com:Endrias13/flaskstarter_proj.git

python3 -m venv ~/.flask-ml-azure

source ~/.flask-ml-azure/bin/activate

pip install -r requirements.txt 

az webapp up -n flaskapp-proj-app 

chmod +x make_predict_azure_app.sh

./make_predict_azure_app.sh
