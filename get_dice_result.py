from sqlite import *
async def get_row(result_dice: int):
  slot_values = {
    1: ("бар", 'бар', 'бар'),
    2: ("виноград", 'бар', 'бар'),
    3: ("лимон", 'бар', 'бар'),
    4: ("сімка", 'бар', 'бар'),
    5: ("бар", 'виноград', 'бар'),
    6: ("виноград", 'виноград', 'бар'),
    7: ("лимон", 'виноград', 'бар'),
    8: ("сімка", 'виноград', 'бар'),
    9: ("бар", 'лимон', 'бар'),
    10: ("виноград", 'лимон', 'бар'),
    11: ("лимон", 'лимон', 'бар'),
    12: ("сімка", 'лимон', 'бар'),
    13: ("бар", 'сімка', 'бар'),
    14: ("виноград", 'сімка', 'бар'),
    15: ("лимон", 'сімка', 'бар'),
    16: ("сімка", 'сімка', 'бар'),
    17: ("бар", 'бар', 'виноград'),
    18: ("виноград", 'бар', 'виноград'),
    19: ("лимон", 'бар', 'виноград'),
    20: ("сімка", 'бар', 'виноград'),
    21: ("бар", 'виноград', 'виноград'),
    22: ("виноград", 'виноград', 'виноград'),
    23: ("лимон", 'виноград', 'виноград'),
    24: ("сімка", 'виноград', 'виноград'),
    25: ("бар", 'лимон', 'виноград'),
    26: ("виноград", 'лимон', 'виноград'),
    27: ("лимон", 'лимон', 'виноград'),
    28: ("сімка", 'лимон', 'виноград'),
    29: ("бар", 'сімка', 'виноград'),
    30: ("виноград", 'сімка', 'виноград'),
    31: ("лимон", 'сімка', 'виноград'),
    32: ("сімка", 'сімка', 'виноград'),
    33: ("бар", 'бар', 'лимон'),
    34: ("виноград", 'бар', 'лимон'),
    35: ("лимон", 'бар', 'лимон'),
    36: ("сімка", 'бар', 'лимон'),
    37: ("бар", 'виноград', 'лимон'),
    38: ("виноград", 'виноград', 'лимон'),
    39: ("лимон", 'виноград', 'лимон'),
    40: ("сімка", 'виноград', 'лимон'),
    41: ("бар", 'лимон', 'лимон'),
    42: ("виноград", 'лимон', 'лимон'),
    43: ("лимон", 'лимон', 'лимон'),
    44: ("сімка", 'лимон', 'лимон'),
    45: ("бар", 'сімка', 'лимон'),
    46: ("виноград", 'сімка', 'лимон'),
    47: ("лимон", 'сімка', 'виноград'),
    48: ("сімка", 'сімка', 'лимон'),
    49: ("бар", 'бар', 'сімка'),
    50: ("виноград", 'бар', 'сімка'),
    51: ("лимон", 'бар', 'сімка'),
    52: ("сімка", 'бар', 'сімка'),
    53: ("бар", 'виноград', 'сімка'),
    54: ("виноград", 'виноград', 'сімка'),
    55: ("лимон", 'виноград', 'сімка'),
    56: ("сімка", 'виноград', 'сімка'),
    57: ("бар", 'лимон', 'сімка'),
    58: ("виноград", 'лимон', 'сімка'),
    59: ("лимон", 'лимон', 'сімка'),
    60: ("сімка", 'лимон', 'сімка'),
    61: ("бар", 'сімка', 'сімка'),
    62: ("виноград", 'сімка', 'сімка'),
    63: ("лимон", 'сімка', 'сімка'),
    64: ("сімка", 'сімка', 'сімка'),
  }
  return ', '.join(slot_values.get(result_dice)).capitalize()

async def get_point(result_dice: int):
  if result_dice in (1, 22, 43):
    return 4
  elif result_dice in (6, 11, 16, 17, 27, 32, 33, 48, 49, 54, 59, 38):
    return 1.6
  elif result_dice == 64:
    return 9
  else:
    return -1

async def get_result_text(result_dice: int, bid: int, user_id: int):
  result = await get_point(result_dice=result_dice)
  point = float(bid) * result
  combination_text = await get_row(result_dice=result_dice)


  if result > 0:
    balance = await get_balance2(user_id)
    bon = await get_bonus(user_id)
    bal = float(balance[0]) + float(point)
    await edit_balance2(user_id=user_id, bal=str(float(bal)))
    balance2 = await get_balance2(user_id)
    bon2 = await get_bonus(user_id)
    text_for_games = f'Ваша комбінація: \r\n {combination_text} X{float(result)+1}\r\n\n🙂 Вітаємо! Ви виграли {float(point)+bid} UAH!\n\n💳 Баланс: {float(balance2[0])} UAH\n🎁 Бонус: {float(bon2[0])} UAH'
    print(f"{user_id} Слоти - ставка: {bid} UAH    +{bid} = {balance2[0]}") 
  else:
    balance2 = await get_balance2(user_id)
    bon2 = await get_bonus(user_id)
    res_balance_user = float(balance2[0]) - float(bid)
    res_balance_user2 = float(bon2[0]) - float(bid)
    if float(bon2[0]) >= float(bid):
      await edit_bonus(user_id, res_balance_user2)
    else:
      if float(balance2[0]) >= float(bid):
        await edit_balance2(user_id, str(float(res_balance_user)))
      else:
        await edit_balance2(user_id, str(float(0)))

    balance2 = await get_balance2(user_id)
    bon2 = await get_bonus(user_id)
    text_for_games = f'Ваша комбінація: \r\n {combination_text}\r\n\n😞 Удача не на вашому боці...\n Спробуйте ще раз.\n\n💳 Баланс: {float(balance2[0])} UAH\n🎁 Бонус: {float(bon2[0])} UAH'
    print(f"{user_id} Слоти - ставка: {bid} UAH    -{bid} = {balance2[0]}") 
  return text_for_games