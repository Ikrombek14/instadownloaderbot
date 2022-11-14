from telegram.ext import CommandHandler,Updater,MessageHandler, Filters
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton
from insta import instadownloader


def start(update, context):
    message = update.message.from_user.first_name
    update.message.reply_photo(
        photo=open('image.jpg','rb'),
        caption=f"🙋‍♂Salom <b>{message}</b> ushbu bot sizga INSTAGRAMDAN <i>reels, photo, post </i> larni yuklab beradi.\n \n"
                f"⚽ Boshlash uchun link yuboring!\n \n "
                f"📎 Masalan: https://www.instagram.com/p/Cg45hlHsQb9/", parse_mode='HTML'
    )
    update.message.reply_chat_action(action=ChatAction.TYPING)


def instagram(update, context):
    link = update.message.text
    data = instadownloader(link=link)
    if data == 'Bad':
        update.message.reply_text(text="Bu url xato")
    else:
        if data ['type']=='image':
            update.message.reply_text(text='Yuklanmoqda')
            update.message.reply_photo(
                photo=data['media'],
                caption="@Instagrammediarobot  Do'stlaringizga ulashing!")

        elif data['type']=='video':
            update.message.reply_text(text='Yuklanmoqda ...')
            update.message.reply_video(video=data['media'],caption="@Instagrammediarobot  Do'stlaringizga ulashing!")
        elif data['type']=='carusel':
            for i in data['media']:
                update.message.reply_document(document=i,caption="@Instagrammediarobot  Do'stlaringizga ulashing!")
        else:
            update.message.reply_text(text="Bu xato url")








def main():
    updater=Updater(token='5760839164:AAEi0Wj73VG87EPBlMrZ7ZQLHyy_tlIu-m8')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start',start))
    dispatcher.add_handler(MessageHandler(Filters.all, instagram))
    updater.start_polling()
    updater.idle()
if __name__=='__main__':
    main()