FROM python:3.10-slim

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملف المتطلبات لتثبيت الحزم
COPY requirements.txt .

# تثبيت المكتبات المطلوبة
RUN pip install --no-cache-dir -r requirements.txt

# نسخ مجلد التطبيق
COPY ./app ./app

# تعيين متغير البيئة للبورت
ENV PORT=10000

# أمر تشغيل التطبيق باستخدام Uvicorn على جميع الواجهات وبورت 10000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
