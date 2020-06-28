from apscheduler.schedulers.blocking import BlockingScheduler
import DailyDataJson
import InferenceForecastDataJson
import time

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun' ,hour=16 , minute =10)
def scheduled_job():
	DailyDataJson.dd()
	InferenceForecastDataJson.ifd(0.3)
	InferenceForecastDataJson.ifd(0.4)
	InferenceForecastDataJson.ifd(0.5)
	InferenceForecastDataJson.ifd(0.6)
	InferenceForecastDataJson.ifd(0.7)
	InferenceForecastDataJson.ifd(0.8)
	
sched.start()