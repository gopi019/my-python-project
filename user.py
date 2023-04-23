class User:
    def __init__(self, name, email, pwd, job_title):
        self.job_title = job_title
        self.pwd = pwd
        self.email = email
        self.name = name

    def change_password(self, name, pwd, new_pwd):
        self.pwd = new_pwd

    def change_job_title(self, new_title ):
        self.job_title = new_title



