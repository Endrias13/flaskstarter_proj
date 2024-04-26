
CI/CD Github Deployment Project:

<img width="938" alt="azure_pipeline_deploy" src="https://github.com/Endrias13/flaskstarter_proj/assets/33791240/880537ec-47ca-4b5a-9e86-22785ab064dd">


*Your project repository should include the following initial files:
  1. Makefile: Automates setup, testing, and other commands.
  2. requirements.txt: Lists all the Python packages your project depends on.
  3. app.py: Your main Python application file (assuming from the placeholders).
  4. test_app.py: Contains tests for your app.py.


*Connecting GitHub Repo to Azure Cloud:
  Generate an SSH Key in Azure Cloud:
    - Use Azure Cloud Shell or your local terminal (if configured to access Azure) to generate an SSH key pair with ssh-keygen -t rsa -b 4096.
    - Add the public SSH key to your GitHub account under Settings > SSH and GPG keys > New SSH key.
    - Clone Your GitHub Repository:
        Use the command provided, ensuring you replace Endrias13/Udacity_Proj with your repository's actual name.


*Project Scaffolding in Azure Cloud:

1. Create a Python Virtual Environment:
    python3 -m venv ~/.myrepo
    
2. Activate the Virtual Environment:  
    source ~/.myrepo/bin/activate
   
4. Install Dependencies and Run Tests:
    make all


*Running the Python Script:
With your environment set up and dependencies installed, you can now run your Python scripts (app.py and test_app.py) directly in the Azure Cloud environment.

*GitHub Actions for CI/CD
Set up GitHub Actions to automate building and testing for every pull request to your repository. Additionally, configure it to deploy merged pull requests to production.


*Create Azure Flask Web App:

1. python3 -m venv ~/.flask-ml-azure (Set up environment)
2. source ~/.flask-ml-azure/bin/activate
3. pip install -r requirements.txt (Download all the required python packages)
4. az webapp up -n flaskapp-proj-app (Can be any name)
5. Run prediction script: ./make_predict_azure_app.sh 


*Running the Flask App with Locust
To test the performance of your Flask application, use Locust by writing a locustfile.py that simulates user behavior. Then, run Locust locally or in your cloud environment to identify potential bottlenecks.

*Continuous Delivery with Azure Pipelines
Set Up Azure Pipelines: Connect your GitHub repository to Azure Pipelines and configure it to automatically deploy your application to Azure upon a successful build/test cycle. 






