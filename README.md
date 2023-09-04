## vacuum-cleaner

If you're trying to run the vacuum cleaner project, here are the steps you need to take. 

1. You need to have docker installed on your machine. 

2. To download the project from its git repository, you need to have the git version control system installed on your machine. 

2.a. Once git is installed, clone the repository with the command 'git clone https://github.com/csemrm/vacuum-cleaner.git'

2.b. Go to the repository root with the 'cd vacuum-cleaner' command

2.c. Run the docker build command so that you can fetch the docker image and other dependencies 

2.d. Finally, to make the project live, run the 'docker-compose up' command. 

3. If you're downloading the project from an email or some other source, unzip it first. 

3.a. Then navigate to the root of the project with 'cd vacuum-cleaner'

3.b. Download the docker image and other dependencies with the docker build command

3.c. Run 'docker-compose up' to make the project live. 

4. To access the project, visit http://127.0.0.1:8000/api/vacuum using your web browser or a REST client such as Postman or Insomnia. 

5. Send parameters in JSON format, such as 

```

{

"cleaning_batches": [[3, 2, 4], [2, 1, 4], [4, 5]],

"priority_rooms": [7, 14, 1]

}

``` 

To get the desired result. 

Hopefully, this explains how to run the project. Feel free to reach out to me if you have any further questions!