# scheduler.py

from apscheduler.schedulers.blocking import BlockingScheduler
import pytz
from agent import run_agent

# Create scheduler with IST timezone
sched = BlockingScheduler(timezone=pytz.timezone("Asia/Kolkata"))

# Schedule the task to run daily at 12:53 PM IST
@sched.scheduled_job("interval", seconds=30)
def scheduled_task():
    print("[SCHEDULER] Running daily agent...")
    run_agent()

if __name__ == "__main__":
    print("Scheduler started... waiting for 12:53 PM IST")
    sched.start()
