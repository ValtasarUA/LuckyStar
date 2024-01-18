from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
	await bot.send_invoice(
		chat_id=message.chat.id,
		title="Поповнення казино.",
		description="",
		payload="info is",
		provider_token="2051251535:TEST:OTk5MDA4ODgxLTU",
		currency="uah",
		prices=[
			LabeledPrice(
				label='10 UAH',
				amount='1000'
				)
		],
		max_tip_amount=[1000, 2000, 3000, 4000],
		start_parameter='',
		provider_data=None,
		need_name = True,
		need_phone_number = False,
		need_email = False,
		need_shipping_address = False,
		request_timeout=15
	)


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
	await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

