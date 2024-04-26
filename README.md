
CI/CD Github Deployment Project:

********** Documentation **********

Trello Board: https://trello.com/invite/b/G5p5en6j/ATTIce995206d9e2680b4931c5480b010cf97C30DE70/lesson2-project

Project Plan Spreadsheet: 
[project_estimate_sheet.xlsx](https://github.com/Endrias13/flaskstarter_proj/files/15134404/project_estimate_sheet.xlsx)

Youtube Video Demonstration: https://www.youtube.com/watch?v=VrPfzOkc4R4

************************************************************


********** Steps for Task 1 (test_hello script) **********

Your project repository should include the following initial files:

  1. Makefile (Makefile_Task_1): Automates setup, testing, and other commands.
  2. requirements.txt: Lists all the Python packages your project depends on.
  3. app.py: Your main Python application file (assuming from the placeholders).
  4. test_app.py: Contains tests for your app.py.

Connecting GitHub Repo to Azure Cloud:
    - Use Azure Cloud Shell or your local terminal (if configured to access Azure) to generate an SSH key pair with ssh-keygen -t rsa 
    - Add the public SSH key to your GitHub account under Settings > SSH and GPG keys > New SSH key.
    - Clone Your GitHub Repository:
        Use the command provided, ensuring you replace Endrias13/Udacity_Proj with your repository's actual name.

<img width="604" alt="git_clone_azure" src="https://github.com/Endrias13/flaskstarter_proj/assets/33791240/c16879e8-64f1-4bbd-9db9-2c30b569d3f6">




Project Scaffolding in Azure Cloud:

1. Create a Python Virtual Environment:
    python3 -m venv ~/.myrepo
    
2. Activate the Virtual Environment:  
    source ~/.myrepo/bin/activate
   
4. Install Dependencies and Run Tests:
    make all

<img width="947" alt="make_all_command" src="https://github.com/Endrias13/flaskstarter_proj/assets/33791240/1d59b6c9-e646-4115-88af-5b4a605f8ea4">



GitHub Actions for CI/CD:

Please refer to the 'github_actions.py' yaml file that need to integrated into Github actions

Set up GitHub Actions to automate building and testing for every pull request to your repository. Additionally, configure it to deploy merged pull requests to production.

<img width="1439" alt="github_actions_passed" src="https://github.com/Endrias13/flaskstarter_proj/assets/33791240/631083c5-2876-43b5-96d6-779b7edfbe1a">




********** Steps for Task 2 (Azure Flask Web App) **********

Create Azure Flask Web App:

1. python3 -m venv ~/.flask-ml-azure (Set up environment)
2. source ~/.flask-ml-azure/bin/activate
3. pip install -r requirements.txt (Download all the required python packages)
4. az webapp up -n flaskapp-proj-app (Can be any name)
5. Run prediction script: ./make_predict_azure_app.sh 


Launching Flask Web App:

<img width="1438" alt="app_servicce" src="https://github.com/Endrias13/flaskstarter_proj/assets/33791240/525810af-7a43-4acc-81ba-7e529ed555bc">


<img width="1220" alt="azure_app_launch" src="https://github.com/Endrias13/flaskstarter_proj/assets/33791240/3b713f68-5768-458f-a6d8-2b5a0bd51ce1">


Running Prediction:

<img width="714" alt="run_prediction" src="https://github.com/Endrias13/flaskstarter_proj/assets/33791240/52609d21-4097-43f1-95ed-be47d367b253">


Running the Flask App with Locust
To test the performance of your Flask application, use Locust by writing a locustfile.py that simulates user behavior. Then, run Locust locally or in your cloud environment to identify potential bottlenecks.

<img width="1440" alt="locust_test" src="https://github.com/Endrias13/flaskstarter_proj/assets/33791240/d5ab6515-1761-4948-880b-2fbf050f2fbd">



Continuous Delivery with Azure Pipelines
Set Up Azure Pipelines: Connect your GitHub repository to Azure Pipelines and configure it to automatically deploy your application to Azure upon a successful build/test cycle. 

<img width="947" alt="azure_pipeline_deployment" src="https://github.com/Endrias13/flaskstarter_proj/assets/33791240/37a872ec-e6b0-4f13-aa39-9c7d07b376af">



