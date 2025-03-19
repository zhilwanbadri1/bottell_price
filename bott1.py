import requests
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import telegram
from bs4 import BeautifulSoup

# توکن ربات تلگرام و ID کانال‌های خودت رو اینجا وارد کن
TOKEN = '5916551233:AAFeGwvdk7Uk85yiRC-q6Jo4dpAaJOOR1kY'
CHANNEL_ID_1 = '@aaafffggghsssssss'  # شناسه کانال اول
CHANNEL_ID_2 = '@efiefjseffieffew54'  # شناسه کانال دوم

# تابع برای دریافت قیمت بیت کوین از API
def get_bitcoin_price():
    try:
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
        response = requests.get(url)
        data = response.json()
        return data['bitcoin']['usd']
    except Exception as e:
        print(f"خطا در دریافت قیمت بیت کوین: {e}")
        return "خطا در دریافت قیمت بیت کوین"


# تابع برای دریافت قیمت دلار ایران از API
import requests
from bs4 import BeautifulSoup

def get_bbit_price():
    try:
        url = "https://nobitex.ir/btc/"

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # پیدا کردن div که شامل قیمت بیت کوین است
            price_div = soup.find('div', class_='text-headline-medium text-txt-neutral-default dark:text-txt-neutral-default desktop:text-headline-large')

            if price_div:
                # استخراج قیمت از داخل div
                return price_div.text.strip()  # قیمت در داخل این div است
        return "قیمت بیت کوین پیدا نشد"
    except Exception as e:
        print(f"خطا در دریافت قیمت بیت کوین: {e}")
        return "خطا در دریافت قیمت بیت کوین"


    

# تابع برای دریافت قیمت دلار ایران از API
def get_dollar_price():
    try:
        url = "https://www.tgju.org/profile/price_dollar_rl"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            price_div = soup.find('div', class_='block-last-change-percentage')

            if price_div:
                price_span = price_div.find('span', class_='price')
                if price_span:
                    return price_span.text.strip()
            return "قیمت دلار پیدا نشد"
        return "خطا در دریافت قیمت دلار"
    except Exception as e:
        print(f"خطا در دریافت قیمت دلار: {e}")
        return "خطا در دریافت قیمت دلار"

# دریافت قیمت طلا 18 عیار
def get_geram_price():
    try:
        url = "https://www.tgju.org/profile/geram18"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            price_div = soup.find('div', class_='block-last-change-percentage')

            if price_div:
                price_span = price_div.find('span', class_='price')
                if price_span:
                    return price_span.text.strip()
            return "قیمت گرم پیدا نشد"
        return "خطا در دریافت قیمت طلا"
    except Exception as e:
        print(f"خطا در دریافت قیمت طلا: {e}")
        return "خطا در دریافت قیمت طلا"

# دریافت قیمت تتر از سایت نوبیتکس
def get_teter_price():
    try:
        url = "https://nobitex.ir/usdt/"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # پیدا کردن div که شامل قیمت تتر است
            price_div = soup.find('div', class_='flex h-20 items-center gap-4 text-body-small desktop:text-body-large')

            if price_div:
                # استخراج قیمت از داخل div
                return price_div.contents[0].strip()  # قیمت در داخل اولین المنت متنی است
        return "قیمت تتر پیدا نشد"
    except Exception as e:
        print(f"خطا در دریافت قیمت تتر: {e}")
        return "خطا در دریافت قیمت تتر"


import requests
from bs4 import BeautifulSoup

def get_ether_price():
    try:
        url = "https://nobitex.ir/eth/"

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # پیدا کردن div که شامل قیمت بیت کوین است
            price_div = soup.find('div', class_='text-body-bold-large text-txt-neutral-default dark:text-txt-neutral-default')

            if price_div:
                # استخراج قیمت از داخل div
                return price_div.text.strip()  # قیمت در داخل این div است
        return "قیمت اتریوم پیدا نشد"
    except Exception as e:
        print(f"خطا در دریافت قیمت اتریوم : {e}")
        return "خطا در دریافت قیمت اتریوم :"


# تابع ارسال پیام و حذف پیام قبلی با مکانیزم تلاش مجدد
async def send_bitcoin_price(context: CallbackContext) -> None:
    retries = 3  # تعداد دفعات تلاش مجدد
    for attempt in range(retries):
        try:
            # دریافت قیمت‌ها
            pricebit = get_bitcoin_price()
            pricedollar = get_dollar_price()
            price_geram = get_geram_price()
            priceteter = get_teter_price()
            pricebit22 = get_bbit_price()
            priceether=get_ether_price()

            # ساخت پیام
            message_text = f"قیمت بیت کوین: $ {pricebit}\n"
            message_text += f"قیمت دلار: {pricedollar}  ریال\n"
            message_text += f"قیمت طلا: {price_geram} ریال\n"
            message_text += f"قیمت تتر: {priceteter} تومان\n"
            message_text += f"قیمت بیت کوین به تومان : {pricebit22}\n"
            message_text+=f"قیمت اتریوم : $ {priceether}"

            print(f"در حال ارسال پیام به کانال اول: {message_text}")  # چاپ برای بررسی

            # ارسال پیام به کانال اول
            new_message_1 = await context.bot.send_message(
                chat_id=CHANNEL_ID_1,  # کانال اول
                text=message_text,
                disable_notification=True  # جلوگیری از نوتیفیکیشن
            )
            print(f"پیام جدید به کانال اول با ID {new_message_1.message_id} ارسال شد.")  # چاپ برای بررسی

            # ارسال پیام به کانال دوم
            new_message_2 = await context.bot.send_message(
                chat_id=CHANNEL_ID_2,  # کانال دوم
                text=message_text,
                disable_notification=True  # جلوگیری از نوتیفیکیشن
            )
            print(f"پیام جدید به کانال دوم با ID {new_message_2.message_id} ارسال شد.")  # چاپ برای بررسی

            # بررسی اینکه context.job.data معتبر است
            if context.job.data is None:
                context.job.data = {}

            # حذف پیام قبلی از کانال اول
            last_message_id_1 = context.job.data.get('last_message_1', None)
            if last_message_id_1 is not None:
                try:
                    await context.bot.delete_message(chat_id=CHANNEL_ID_1, message_id=last_message_id_1)
                    print(f"پیام قبلی از کانال اول با ID {last_message_id_1} حذف شد.")
                except telegram.error.TelegramError as e:
                    print(f"خطا در حذف پیام قبلی از کانال اول: {e}")

            # حذف پیام قبلی از کانال دوم
            last_message_id_2 = context.job.data.get('last_message_2', None)
            if last_message_id_2 is not None:
                try:
                    await context.bot.delete_message(chat_id=CHANNEL_ID_2, message_id=last_message_id_2)
                    print(f"پیام قبلی از کانال دوم با ID {last_message_id_2} حذف شد.")
                except telegram.error.TelegramError as e:
                    print(f"خطا در حذف پیام قبلی از کانال دوم: {e}")

            # ذخیره ID پیام جدید برای حذف در بار بعدی
            context.job.data['last_message_1'] = new_message_1.message_id
            context.job.data['last_message_2'] = new_message_2.message_id

            break  # اگر موفق شد، از حلقه خارج می‌شود

        except telegram.error.TimedOut:
            print(f"زمان تایم‌اوت در تلاش {attempt + 1} رخ داده. دوباره تلاش می‌کنیم...")
            time.sleep(5)  # زمان انتظار بین تلاش‌ها
            continue  # تلاش مجدد
        except Exception as e:
            print(f"خطای غیرمنتظره: {e}")
            break  # اگر خطای غیرمنتظره باشه، دیگه تلاش نمی‌کنه

# تابع اصلی برای شروع ربات
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('ربات شروع به کار کرد!')

def main():
    # ایجاد ربات و تنظیم تایم‌اوت‌ها
    application = Application.builder().token(TOKEN).read_timeout(300).write_timeout(300).build()

    # اضافه کردن دستور /start
    application.add_handler(CommandHandler("start", start))

    # برنامه‌ریزی برای ارسال قیمت‌ها هر 30 ثانیه
    application.job_queue.run_repeating(send_bitcoin_price, interval=5, first=0)  # فاصله ارسال 30 ثانیه

    # شروع ربات
    application.run_polling()

if __name__ == '__main__':
    main()
