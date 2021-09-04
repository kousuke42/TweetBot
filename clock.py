from apscheduler.schedulers.blocking import BlockingScheduler
import words

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=30)
def timed_job():
    words.puttweet()
    print("tweetしました。")

if __name__ == "__main__":
    twische.start()