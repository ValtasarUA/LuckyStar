from sqlite import *
async def get_row_darts(result_dice_darts: int):
  slot_values_darts = {
  1: ("Програш"),
  2: ("Програш"),
  3: ("Програш"),
  4: ("Програш"),
  5: ("виграш"),
  6: ("виграш"),
  }
  return slot_values_darts.get(result_dice_darts).capitalize()


async def get_point_darts(result_dice_darts: int):

  if result_dice_darts == 5:
    return 1.0
  if result_dice_darts == 6:
    return 1.2
  else:
    return -1


async def get_result_text_darts(result_dice_darts: int, bid: int, user_id: int):
  result = await get_point_darts(result_dice_darts=result_dice_darts)
  point = float(bid) * result
  combination_text = await get_row_darts(result_dice_darts=result_dice_darts)


  if result > 0:
    balance = await get_balance2(user_id)
    bon = await get_bonus(user_id)
    bal = float(balance[0]) + float(point)
    await edit_balance2(user_id=user_id, bal=str(float(bal)))
    balance2 = await get_balance2(user_id)
    bon2 = await get_bonus(user_id)
    text_for_games = f'🙂 X{result + 1}\nВи виграли {point*2} UAH!\n\n💳 Баланс: {float(balance2[0])} UAH\n🎁 Бонус: {float(bon2[0])} UAH'
    print(f"{user_id} Дартс - ставка: {bid} UAH    +{bid} = {balance2[0]}") 
  else:
    balance2 = await get_balance2(user_id)
    bon2 = await get_bonus(user_id)
    res_balance_user = float(balance2[0]) - float(bid)
    res_balance_user2 = float(bon2[0]) - float(bid)
    if float(bon2[0]) >= float(bid):
      await edit_bonus(user_id, res_balance_user2)
    else:
      if float(balance2[0]) >= float(bid):
        await edit_balance2(user_id, str(res_balance_user))
      else:
        await edit_balance2(user_id, str(float(0)))
    balance2 = await get_balance2(user_id)
    bon2 = await get_bonus(user_id)
    text_for_games = f'😞 Мимо...\n Спробуйте ще раз.\n\n💳 Баланс: {float(balance2[0])} UAH\n🎁 Бонус: {float(bon2[0])} UAH'
    print(f"{user_id} Дартс - ставка: {bid} UAH    -{bid} = {balance2[0]}") 
  return text_for_games