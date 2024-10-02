import asyncio
from django.db.models.signals import post_save
from django.dispatch import receiver
from telegram import Bot
from .models import Application
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

async def send_telegram_message(chat_id, message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text=message)

@receiver(post_save, sender=Application)
def send_telegram_notification(sender, instance, created, **kwargs):
    if created:  # только если объект создан
        message =  message = f"Новая заявка на выступление с нашего сайта:\nИмя: {instance.name}\nEmail: {instance.email}\nСообщение: {instance.text}"
        asyncio.run(send_telegram_message(CHAT_ID, message))
