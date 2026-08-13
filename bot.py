import telebot
from telebot import types
import os

# =========================================================
# ⚙️ CONFIGURATION (Aapki Details)
# =========================================================
BOT_TOKEN = "8806001099:AAFySoP1wRBInEL4QqkGGYsZ98z-neaFFl8"  # 👈 Yahan apna Bot Token daalein
UPI_ID = "hasanguftqn@ptyes"       # Aapki UPI ID
ADMIN_ID = 8734479878              # Aapki Telegram Admin ID
QR_IMAGE_PATH = "qr.png"          # QR Code Photo (Termux folder mein)

bot = telebot.TeleBot(BOT_TOKEN)

# =========================================================
# 🔘 KEYBOARDS (BUTTONS LAYOUT)
# =========================================================
def main_menu_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # App Buttons
    btn_netflix = types.InlineKeyboardButton("🎬 Netflix Ultra HD", callback_data="netflix")
    btn_youtube = types.InlineKeyboardButton("🔴 YouTube Premium", callback_data="youtube")
    btn_spotify = types.InlineKeyboardButton("🎵 Spotify VIP", callback_data="spotify")
    btn_prime = types.InlineKeyboardButton("📦 Prime Video HD", callback_data="prime")
    
    # Service & Help Buttons
    btn_qr = types.InlineKeyboardButton("📲 Payment QR & UPI", callback_data="pay_qr")
    btn_support = types.InlineKeyboardButton("📞 Admin Support", callback_data="support")
    btn_faq = types.InlineKeyboardButton("📜 Terms & FAQ", callback_data="faq")
    
    # Layout Grid
    markup.add(btn_netflix, btn_youtube)
    markup.add(btn_spotify, btn_prime)
    markup.add(btn_qr)
    markup.add(btn_support, btn_faq)
    
    return markup

def back_button():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu"))
    return markup

# =========================================================
# 🚀 START COMMAND (/start)
# =========================================================
@bot.message_handler(commands=['start', 'help'])
def start_command(message):
    welcome_text = (
        "👑 **WELCOME TO VIP PREMIUM STORE** 👑\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "✨ **100% Original & Trusted Premium Apps**\n\n"
        "Aapka hamare official store mein swagat hai! Yahan aapko sabhi **Premium Apps** sabse kam daam mein milenge.\n\n"
        "⚡ **Why Choose Us?**\n"
        "• 🚀 Instant Delivery (5-10 Mins)\n"
        "• 🔒 100% Private & Safe Accounts\n"
        "• 🛡️ Full Plan Warranty & Support\n\n"
        "👇 **Niche button par click karke apna favorite app select karein:**"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=main_menu_keyboard())

# =========================================================
# 📲 BUTTON CLICKS & NAVIGATION
# =========================================================
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id

    if call.data == "main_menu":
        welcome_text = (
            "👑 **WELCOME TO VIP PREMIUM STORE** 👑\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "👇 **Niche button par click karke app choose karein:**"
        )
        bot.edit_message_text(welcome_text, chat_id, msg_id, parse_mode='Markdown', reply_markup=main_menu_keyboard())

    elif call.data == "netflix":
        text = (
            "🎬 **NETFLIX PREMIUM 4K UHD**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "• 📺 Ultra HD 4K + HDR Quality\n"
            "• 🔒 Private Profile & Screen PIN\n"
            "• 📱 TV, Mobile, Laptop Supported\n"
            "• ⏳ **Validity:** 1 Month\n"
            "• 💰 **Price:** Sirf **₹20**\n\n"
            f"🔹 **UPI ID:** `{UPI_ID}`\n\n"
            "👉 Pay karne ke baad **Screenshot** chat mein bhej dein!"
        )
        bot.edit_message_text(text, chat_id, msg_id, parse_mode='Markdown', reply_markup=back_button())

    elif call.data == "youtube":
        text = (
            "🔴 **YOUTUBE PREMIUM + MUSIC**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "• 🚫 100% Ad-Free Video Streaming\n"
            "• 🎧 YouTube Music Premium Included\n"
            "• 📱 Background Play & Downloads\n"
            "• ⏳ **Validity:** 1 Month\n"
            "• 💰 **Price:** Sirf **₹20**\n\n"
            f"🔹 **UPI ID:** `{UPI_ID}`\n\n"
            "👉 Pay karne ke baad **Screenshot** chat mein bhej dein!"
        )
        bot.edit_message_text(text, chat_id, msg_id, parse_mode='Markdown', reply_markup=back_button())

    elif call.data == "spotify":
        text = (
            "🎵 **SPOTIFY PREMIUM VIP**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "• 🎧 High Quality Audio (320kbps)\n"
            "• 🚫 Zero Ads & Unlimited Skips\n"
            "• ⬇️ Offline Song Downloads\n"
            "• ⏳ **Validity:** 1 Month\n"
            "• 💰 **Price:** Sirf **₹20**\n\n"
            f"🔹 **UPI ID:** `{UPI_ID}`\n\n"
            "👉 Pay karne ke baad **Screenshot** chat mein bhej dein!"
        )
        bot.edit_message_text(text, chat_id, msg_id, parse_mode='Markdown', reply_markup=back_button())

    elif call.data == "prime":
        text = (
            "📦 **AMAZON PRIME VIDEO HD**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "• 🍿 Full HD Movies & Web Series\n"
            "• ⚡ High-Speed Buffering Free Server\n"
            "• 📱 Multi-Device Supported\n"
            "• ⏳ **Validity:** 1 Month\n"
            "• 💰 **Price:** Sirf **₹20**\n\n"
            f"🔹 **UPI ID:** `{UPI_ID}`\n\n"
            "👉 Pay karne ke baad **Screenshot** chat mein bhej dein!"
        )
        bot.edit_message_text(text, chat_id, msg_id, parse_mode='Markdown', reply_markup=back_button())

    elif call.data == "pay_qr":
        caption = (
            "📲 **PAYMENT QR CODE & DETAILS**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "Kisi bhi UPI app (GPay, PhonePe, Paytm) se **₹20** pay karein.\n\n"
            f"🔹 **UPI ID:** `{UPI_ID}`\n\n"
            "⚠️ **IMPORTANT:** Payment karne ke baad screenshot aur app ka naam is chat mein bhej dein!"
        )
        # Check agar Termux folder mein QR image maujood hai
        if os.path.exists(QR_IMAGE_PATH):
            with open(QR_IMAGE_PATH, 'rb') as qr:
                bot.send_photo(chat_id, qr, caption=caption, parse_mode='Markdown', reply_markup=back_button())
        else:
            bot.edit_message_text(caption, chat_id, msg_id, parse_mode='Markdown', reply_markup=back_button())

    elif call.data == "support":
        text = (
            "📞 **24/7 CUSTOMER SUPPORT**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "Kisi bhi dikkat ya help ke liye hamare Admin se sampark karein:\n\n"
            "💬 **Admin Telegram:** @RioRober\n"
            "⏱️ **Response Time:** 5-10 Minutes"
        )
        bot.edit_message_text(text, chat_id, msg_id, parse_mode='Markdown', reply_markup=back_button())

    elif call.data == "faq":
        text = (
            "📜 **TERMS & FAQ**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "1. **Delivery kitni der mein milti hai?**\n"
            "   └ Screenshot bhejne ke 5-10 minute ke andar.\n\n"
            "2. **Warranty milegi?**\n"
            "   └ Haan, pooray 1 mahine ki full replacement warranty.\n\n"
            "3. **Payment ke baad kya karein?**\n"
            "   └ Direct screenshot bhej dein, Admin verify karke account de dega."
        )
        bot.edit_message_text(text, chat_id, msg_id, parse_mode='Markdown', reply_markup=back_button())

# =========================================================
# 📸 AUTOMATIC PAYMENT SCREENSHOT RECEIVER
# =========================================================
@bot.message_handler(content_types=['photo'])
def handle_payment_screenshot(message):
    user = message.from_user
    username = f"@{user.username}" if user.username else "No Username"
    
    # User ko Confirmation Message
    user_reply = (
        "✅ **PAYMENT SCREENSHOT RECEIVED!**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Aapka payment screenshot hume safaltapurvak mil gaya hai! 🙏\n\n"
        "⏳ **Status:** Admin Verification Pending...\n"
        "⏱️ **Delivery:** 5-10 minute ke andar aapka account active kar diya jayega."
    )
    bot.reply_to(message, user_reply, parse_mode='Markdown')
    
    # Admin (Aapko) Automatic Alert aur Screenshot bhejna
    try:
        admin_msg = (
            "🚨 **NEW PAYMENT RECEIVED!** 🚨\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 **User:** {user.first_name} ({username})\n"
            f"🆔 **User ID:** `{user.id}`\n"
            f"📝 **Caption:** {message.caption if message.caption else 'No Caption'}"
        )
        photo_id = message.photo[-1].file_id
        bot.send_photo(ADMIN_ID, photo_id, caption=admin_msg, parse_mode='Markdown')
    except Exception as e:
        print(f"Admin Alert Error: {e}")

# =========================================================
# ⚡ BOT RUN
# =========================================================
print("⚡ VIP Premium Store Bot 100% Ready & Running...")
bot.infinity_polling()
