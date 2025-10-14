# بوت تيليجرام لحل المشكلات

هذا مشروع بسيط لبوت **تيليجرام** يقوم بالرد على رسائل المستخدمين من خلال حلول مأخوذة من **ملف إكسل**.  
يستخدم المكتبتين **python-telegram-bot** و **pandas**.

---

## المميزات

- تحميل قائمة *المشكلات والحلول* من ملف إكسل (`problems.xlsx`).
- الرد على أي رسالة نصية بالحل المطابق.
- يحتوي على أمر `/start` للترحيب بالمستخدم.
- سهل التخصيص والتطوير بإضافة أوامر جديدة.

---

## هيكل المشروع

```
telegram_bot/
│
├── bot.py             # السكربت الرئيسي
├── problems.xlsx      # ملف الإكسل الذي يحتوي على المشكلات والحلول
└── README.md          # ملف التوثيق
```

---

## تنسيق ملف الإكسل

تأكد أن ملف `problems.xlsx` يحتوي على عمودين بالشكل التالي:

| Problem | Solution |
|----------|-----------|
| WiFi not connecting | Restart your router and try again. |
| Cannot log in | Check your username and password. |

يقوم البوت بمطابقة العمود **Problem** (بغض النظر عن حالة الأحرف) ويعرض الحل المقابل من عمود **Solution**.

---
## إنشاء بوت تيليجرام

1. افتح تطبيق **Telegram** وابحث عن الحساب **BotFather**.
2. أرسل الأمر `/newbot` واتبع الخطوات التالية:
   - اختر اسمًا للبوت.
   - اختر اسم مستخدم (username) ينتهي بكلمة **bot** (مثل: `MyHelperBot`).
   - سيعطيك BotFather **رمز الـ API** (يبدو مثل: `123456789:ABC-XYZ...`).
3. انسخ هذا الرمز واستخدمه في الملف `bot.py` مكان النص `"TOKEN_HERE"`.

---

##  خطوات التثبيت

1. **استنساخ المشروع من GitHub**
   ```bash
   git clone https://github.com/msalharbi/telegram_bot.git
   cd telegram_bot
   ```

2. **إنشاء وتفعيل بيئة افتراضية (اختياري ولكن مستحسن)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # في أنظمة macOS/Linux
   venv\Scripts\activate      # في نظام Windows
   ```

3. **تثبيت المكتبات المطلوبة**
   ```bash
   pip install pandas python-telegram-bot==20.3
   ```

4. **إضافة رمز البوت**
   - افتح الملف `bot.py`
   - واستبدل السطر التالي:
     ```python
     app = Application.builder().token("TOKEN_HERE").build()
     ```
     برمز البوت الخاص بك الذي تحصل عليه من [@BotFather](https://t.me/BotFather).

---

## ▶️ تشغيل البوت

```bash
python bot.py
```

بعد التنفيذ، ستظهر رسالة مشابهة:
```
INFO:telegram.ext._application:Application started successfully
```

ثم افتح تطبيق تيليجرام، وابحث عن البوت، وأرسل رسالة مثل:
> wifi not connecting

وسيقوم البوت بالرد بالحل المقابل من ملف `problems.xlsx`.

---

## 💬 مثال على التفاعل

**المستخدم:**  
`wifi not connecting`  

**البوت:**  
`Restart your router and try again.`

---

## أفكار لتطوير المشروع

- إضافة مطابقة تقريبية (fuzzy matching) لأسماء المشكلات المتشابهة.  
- ربط البوت بجداول Google Sheets بدلاً من ملف Excel.  
- تسجيل الأسئلة الأكثر تكراراً لتحليلها لاحقاً.  
- نشر البوت على خوادم سحابية مثل Render أو Heroku أو AWS Lambda.
