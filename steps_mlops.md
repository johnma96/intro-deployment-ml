# Training a model
1. Start a local repository with a template like cokiecutter, this will speed up the develop
2. Create a remote repository and conect it to local
3. Develop your EDA, feature enginnering, tests of models and select the best model for your problem
4. Save your model like .pkl object

# Implementing Data Version Control with DVC library(
Other tools for ML Data Versioning:
	- Neptune
	- Pachyderm
	- Delta Lake
	- Git LFS
	- Dolt
	- lakeFS
	- DVC
	- ML-Metadata

	Data and models are tracked and save within some storage like Google Store or any AWS service

## Basics commands for DVS
	1. dvc init
	2. dvc remote
	3. dvc add
	4. dvc pull
	5. dvc push
	6. dvc run create subtask for be executed with repro
	7. dvc repro
	8. dvc dag Directed acyclic graph

## Steps
1. Run dvc init to start tracking of data and models
2. Set GOOGLE_APPLICATION_CREDENTIALS enviroment variable using:
	export GOOGLE_APPLICATION_CREDENTIALS=$(realpath <path/to/credentials>)
	echo $GOOGLE_APPLICATION_CREDENTIALS
3. Set remote storage and track files(AWS, GCP, Drive, etc)
	* Go to cloud storage service of GCP
	* Create bucket
		- Name
		- Multi-region
		- Standard
		- Other default or custom settings
	* dvc remote add data-tracker gs://model_dataset_tracker_course/data
	* dvc remote add model-tracker gs://model_dataset_tracker_course/model
	* Add files
		dvc add file/pathdirected acyclic graph OR dvc add data/local/path --to-remote -r data-tracker
	* Push files
		dvc push models/model.pkl -r model-tracker

# Create source files
	Create files within src folder for load, prepare and process data, other for
	train your model and make some reports about its performance. Check cookiecutter
	to get inspiration

# Pipeline for retraing
## Generate a DAG(directed acyclic graph) using DVC
	This DAG allows you implement a workflow for the re-traing of models
	1. Go to terminal
	2. dvc run -n name/of/step -o path/of/outputs python path/of/script (Create step to save scripts)
	3. Add other Steps
		dvc run -n name/of/step -d files python path/of/script (check if is necessary add outputs)
	4. dvc repro is a command for reproduce de DAG when code has been modified
		If there's not changes nothing happens. For force the remake of DAG use
		dvc repro -f
	5. Check the dag
		dvc dag

# Develop of API using FastAPI