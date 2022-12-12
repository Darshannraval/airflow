from git import Repo

repo = Repo("/home/vagrant/test/airflow")
o = repo.remotes.origin
branch = repo.active_branch
print ("current branch is: ", branch)

head = repo.head

if head == head:
  repo.git.checkout("main")
  o.pull()
  new_branch = "feat-dev5"
  repo.git.branch(new_branch)
  repo.git.checkout(new_branch)
  print ("new branch is: ", new_branch)
  with open("/home/vagrant/test/airflow/kitchen.yml", "w") as file:
      file.write("cinc: 15.0.0")
      
  repo.git.add("/home/vagrant/test/airflow/kitchen.yml")
  repo.git.commit("-m","modified code")
  repo.git.push("--set-upstream", o, repo.head.ref)
