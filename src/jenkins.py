from decouple import config
import jenkins


class Jenkins:
    def __init__(self, bot_instance):
        self.chat_id = config("CHAT_ID")
        self.group_id = config("GROUP_ID")
        self.jenkins_url = config("JENKINS_URL")
        self.jenkins_user = config("JENKINS_USER")
        self.jenkins_pass = config("JENKINS_PASSWORD")
        self.job_to_monitor = config("JOB_TO_MONITOR")
        self.bot = bot_instance
        self.jenkins_instance = jenkins.Jenkins(self.jenkins_url, username=self.jenkins_user,
                                                password=self.jenkins_pass)

    def is_job_running(self):
        for job in self.jenkins_instance.get_jobs():
            if job['name'] == self.job_to_monitor:
                self.bot.send_message(self.chat_id, job['name'])

