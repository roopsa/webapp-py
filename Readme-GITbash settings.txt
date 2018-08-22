 Change "origin" of your GIT repository
$ git remote rm origin
$ git remote add origin git@github.com:aplikacjainfo/proj1.git
$ git config master.remote origin
$ git config master.merge refs/heads/master


#############################################
echo "# webapp-py" >> README.md
git init
//NOT required: git add README.md
git commit -m "first commit"
git remote add origin https://github.com/roopsa/webapp-py.git   
git push -u origin master
…or push an existing repository from the command line
git remote add origin https://github.com/roopsa/webapp-py.git
git push -u origin master
or 
git push origin HEAD:master

#############################################
clone the project to your local machine(liunx):
git clone https://github.com/roopsa/webapp-py.git

run docker daemon: start docker engine:
sudo service docker start

#############################################
run from docker:
https://www.jamessturtevant.com/posts/Deploying-Python-Website-To-Azure-Web-with-Docker/
#############################################
docker tag <image id> <tag>

docker tag 8247e6c6c344 51690784/test
#############################################
login to docker from terminal and push your image:
docker login
docker push 51690784/test
#############################################

Create Web app using docker:

#############################################
#############################################
to stop docker/restart docker engine:
sudo service docker stop
sudo service docker restart