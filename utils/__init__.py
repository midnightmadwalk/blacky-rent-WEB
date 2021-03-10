from .autopinger import ping
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()
scheduler.add_job(ping, "interval", seconds=600)

scheduler.start()