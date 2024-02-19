import jenkins

# Jenkins URL and credentials
JENKINS_URL = 'http://54.87.147.137:8080/'
USERNAME = 'admin'
PASSWORD = '11390f232fcee633ff7fc863ec99e41da1'

# Job name
PIPELINE_JOB_NAME = 'first_jon'

# Function to trigger a Jenkins pipeline build
def trigger_pipeline_build():
    server = jenkins.Jenkins(JENKINS_URL, username=USERNAME, password=PASSWORD)
    server.build_job(PIPELINE_JOB_NAME)

# Main function
def main():
    trigger_pipeline_build()

if __name__ == "__main__":
    main()
