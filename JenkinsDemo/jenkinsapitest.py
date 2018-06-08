# Reference  https://www.jianshu.com/p/8fda9e96addd


from  jenkinsapi.jenkins import Jenkins
import time

JenkinsServer = Jenkins(baseurl="http://10.98.137.20:8080/", username="wangg27", password="WEurfn!1@2")
JenkinsServer.poll()
myJob = JenkinsServer.get_job("JenkinsTest1")
latest_build_number = myJob.get_last_buildnumber()
print("Current latest build is %s" % latest_build_number)
parameters = {"Parameter1": "MyParameter1", "Parameter2": "MyParameter2"}
run_job = myJob.invoke(securitytoken="SHARED_CI_TOKEN",
                       build_params=parameters,
                       block=False)  # Start a Jenkins Job with parameters,   Here we need set a remote trigger token in jenkins job.And uncheck the "Prevent Cross Site Request Forgery exploits
# build_number = run_job.get_build_number()
print(run_job.is_running())
while (myJob.get_last_buildnumber() <= latest_build_number):
    print("Build is not start")
    time.sleep(2)
new_build_number = myJob.get_last_buildnumber()
print(new_build_number)

myBuild = myJob.get_build(buildnumber=new_build_number)  # Get the build by build number
print(myBuild.get_status())  # Check the build status
print(myBuild.is_running())  # Check whether this build is ongoing
downstream_jobs = myJob.get_downstream_jobs()
for downstream_job in downstream_jobs:
    print(downstream_job.get_last_buildnumber())
