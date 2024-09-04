from apscheduler.schedulers.background import BackgroundScheduler
from app import daily_motivation

scheduler = BackgroundScheduler()

def post_to_bluesky():
    quote = daily_motivation()
    # Lógica para postar no Bluesky usando as credenciais do config.py

scheduler.add_job(post_to_bluesky, 'interval', hours=app.config['POST_INTERVAL_HOURS'])
scheduler.start()

if __name__ == '__main__':
    try:
        while True:
            pass  # Mantenha o script rodando
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
