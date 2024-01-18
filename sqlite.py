import sqlite3 as sq


async def db_start():
  global db, cur

  db = sq.connect('base3.db')

  cur = db.cursor()

  cur.execute("CREATE TABLE IF NOT EXISTS users(user_id TEXT PRIMARY KEY, name TEXT, balans integer, refer INTEGER, bal text)")

  db.commit()

async def db_start3():
  cur.execute("CREATE TABLE IF NOT EXISTS refer(user_one INTEGER, user_tho INTEGER)")
  db.commit()

async def db_start5():
  cur.execute("CREATE TABLE IF NOT EXISTS bonuss(user_id INTEGER, bonus INTEGER)")
  db.commit()

async def db_start6():
  cur.execute("CREATE TABLE IF NOT EXISTS duel(user_id1 INTEGER, usename1 TEXT, stavka INTEGER, user_id2 INTEGER, username2 TEXT)")
  db.commit()

async def db_start7():
  cur.execute("CREATE TABLE IF NOT EXISTS duel_on(user_id1 INTEGER, user_id2 INTEGER)")
  db.commit()
async def db_start8():
  cur.execute("CREATE TABLE IF NOT EXISTS duel_peremog(user_id INTEGER, peremog INTEGER)")
  db.commit()
async def db_start9():
  cur.execute("CREATE TABLE IF NOT EXISTS balances(user_id INTEGER, balance TEXT)")
  cur.execute("CREATE TABLE IF NOT EXISTS mess(user_id INTEGER, id_msg INTEGER)")
  cur.execute("CREATE TABLE IF NOT EXISTS promocodes(promo TEXT, forever TEXT, suma TEXT)")
  cur.execute("CREATE TABLE IF NOT EXISTS user_promo(promok TEXT, user INTEGER)")
  cur.execute("CREATE TABLE IF NOT EXISTS statis(deposit TEXT, widhart TEXT, todeposit TEXT, towidhart TEXT)")
  cur.execute("CREATE TABLE IF NOT EXISTS ref_tod(user_id INTEGER, refs INTEGER)")
  cur.execute("CREATE TABLE IF NOT EXISTS jet(user_id INTEGER, res TEXT)")
  cur.execute("CREATE TABLE IF NOT EXISTS jetres(prograno TEXT, vygrano TEXT)")
  cur.execute("CREATE TABLE IF NOT EXISTS veref(user_id INTEGER, name TEXT, phone TEXT)")
  cur.execute("CREATE TABLE IF NOT EXISTS popov(user_id INTEGER, suma INTEGER, l_id TEXT)")
  cur.execute("CREATE TABLE IF NOT EXISTS pref(user_id INTEGER, user_id2 INTEGER)")
  cur.execute("CREATE TABLE IF NOT EXISTS work(user_id INTEGER, channel TEXT, lim INTEGER)")
  cur.execute("CREATE TABLE IF NOT EXISTS jobs(user_id INTEGER, channel TEXT)")
  cur.execute("CREATE TABLE IF NOT EXISTS jobs_bl(user_id INTEGER, channel TEXT)")
  cur.execute("CREATE TABLE IF NOT EXISTS lotorea(user_id INTEGER)")

  db.commit()
# LOTOREA

async def dell_lotorea():
  cur.execute(f"DELETE FROM lotorea")
  db.commit()

async def create_lotorea(user_id):
  #ref = cur.execute(f"SELECT * FROM lotorea WHERE user_id == ?", (user_id,)).fetchone()

  #if not ref:
  cur.execute("INSERT INTO lotorea VALUES(?)", (user_id,))
  db.commit()
    #return True
  #else:
    #return False

async def get_lotorea_all():
  res = cur.execute("SELECT * FROM lotorea").fetchall()
  return res
async def delete_lotorea(user_id):
  cur.execute(f"DELETE FROM lotorea WHERE user_id == ?", (user_id) )
  db.commit()

# WORK IN MY BOT


async def delete_work(channel):
  cur.execute(f"DELETE FROM work WHERE channel == ?", (channel,) )
  db.commit()
async def delete_jobs(user_id, channel):
  cur.execute(f"DELETE FROM jobs WHERE channel == ? AND user_id == ?", (channel, user_id,) )
  db.commit()

async def get_lim(channel):
  bal = cur.execute(f"SELECT lim FROM work WHERE channel == '{channel}'").fetchone()
  return bal
async def get_us_ad(channel):
  bal = cur.execute(f"SELECT user_id FROM work WHERE channel == '{channel}'").fetchone()
  return bal
async def get_jobs(user_id, channel):
  ref = cur.execute(f"SELECT * FROM jobs WHERE user_id == ? AND channel == ?", (user_id, channel)).fetchone()
  if ref:
    return ref
  else:
    return False
async def get_jobs_bl(user_id, channel):
  ref = cur.execute(f"SELECT * FROM jobs_bl WHERE user_id == ? AND channel == ?", (user_id, channel)).fetchone()
  if ref:
    return ref
  else:
    return False
async def create_jobs_bl(user_id, channel):
  ref = cur.execute(f"SELECT * FROM jobs_bl WHERE user_id == ? AND channel == ?", (user_id, channel)).fetchone()

  if not ref:
    cur.execute("INSERT INTO jobs_bl VALUES(?, ?)", (user_id, channel))
    db.commit()
    return True
  else:
    return False

async def create_jobs(user_id, channel):
  ref = cur.execute(f"SELECT * FROM jobs WHERE user_id == ? AND channel == ?", (user_id, channel)).fetchone()

  if not ref:
    cur.execute("INSERT INTO jobs VALUES(?, ?)", (user_id, channel))
    db.commit()
    return True
  else:
    return False
async def create_work(user_id, channel, lim):
  ref = cur.execute(f"SELECT * FROM work WHERE channel == '{channel}'").fetchone()

  if not ref:
    cur.execute("INSERT INTO work VALUES(?, ?, ?)", (user_id, channel, lim))
    db.commit()
    return True
  else:
    return False
async def edit_work(channel, lim):
  cur.execute(f"UPDATE work SET lim = {lim} WHERE channel == '{channel}'")
  db.commit()
async def get_work_all():
  res = cur.execute("SELECT * FROM work").fetchall()
  return res
async def get_jobs_all(user_id):
  res = cur.execute(f"SELECT * FROM jobs WHERE user_id == {user_id}").fetchall()
  return res



#Vereficatoin

async def create_pref(user_id, user_id2):
  ref = cur.execute(f"SELECT * FROM pref WHERE user_id == {user_id}").fetchone()

  if not ref:
    cur.execute("INSERT INTO pref VALUES(?, ?)", (user_id, user_id2))
    db.commit()
    return True
  else:
    return False
async def create_veref(user_id):
  ref = cur.execute(f"SELECT * FROM veref WHERE user_id == {user_id}").fetchone()

  if not ref:
    cur.execute("INSERT INTO veref VALUES(?, ?, ?)", (user_id, 'False', 'False'))
    db.commit()
    return True
  else:
    return False
async def create_popov(user_id, suma, l_id):
  ref = cur.execute(f"SELECT * FROM popov WHERE l_id == '{l_id}'").fetchone()

  if not ref:
    cur.execute("INSERT INTO popov VALUES(?, ?, ?)", (user_id, suma, l_id))
    db.commit()
    return True
  else:
    return False

async def get_veref(user_id):
  bal = cur.execute(f"SELECT * FROM veref WHERE user_id == {user_id}").fetchone()
  return bal
async def edit_veref_name(user_id, name):
  cur.execute(f"UPDATE veref SET name = '{name}' WHERE user_id == {user_id}")
  db.commit()
async def edit_veref_phone(user_id, phone):
  cur.execute(f"UPDATE veref SET phone = '{phone}' WHERE user_id == {user_id}")
  db.commit()


async def create_jetres():
  ref = cur.execute("SELECT * FROM jetres").fetchone()

  if not ref:
    cur.execute("INSERT INTO jetres VALUES(?,?)", ('0.0', '0.0'))
    db.commit()
    return True
  else:
    return False

async def edit_jetres(prograno):
  cur.execute(f"UPDATE jetres SET prograno = '{prograno}'")
  db.commit()
async def get_jetres():
  bal = cur.execute(f"SELECT prograno FROM jetres").fetchone()
  return bal


async def create_jet(user_id):
  ref = cur.execute(f"SELECT * FROM jet WHERE user_id == {user_id}").fetchone()

  if not ref:
    cur.execute("INSERT INTO jet VALUES(?, ?)", (user_id, 'False'))
    db.commit()
    return True
  else:
    return False
async def edit_jet(user_id, res2):
  cur.execute(f"UPDATE jet SET res = '{res2}' WHERE user_id == {user_id}")
  db.commit()
async def get_jet(user_id):
  bal = cur.execute(f"SELECT res FROM jet WHERE user_id == {user_id}").fetchone()
  return bal
async def get_pref(user_id):
  bal = cur.execute(f"SELECT user_id2 FROM pref WHERE user_id == {user_id}").fetchone()
  return bal

async def get_top():
  res = cur.execute('SELECT * FROM duel_peremog ORDER BY peremog DESC LIMIT 5').fetchall()
  return res

async def get_top_ref():
  res = cur.execute('SELECT * FROM ref_tod ORDER BY refs DESC LIMIT 5').fetchall()
  return res

async def get_top_ref2():
  res = cur.execute('SELECT * FROM users ORDER BY refer DESC LIMIT 5').fetchall()
  return res

async def create_statis(deposit, widhart, todeposit, towidhart):
  ref = cur.execute(f"SELECT * FROM statis").fetchone()

  if not ref:
    cur.execute("INSERT INTO statis VALUES(?, ?, ?, ?)", (deposit, widhart, todeposit, towidhart))
    db.commit()
    return True
  else:
    return False
async def create_reftod(user_id):
  ref = cur.execute(f"SELECT * FROM ref_tod WHERE user_id == {user_id}").fetchone()

  if not ref:
    cur.execute("INSERT INTO ref_tod VALUES(?, ?)", (user_id, 0))
    db.commit()
    return True
  else:
    return False

async def edit_reftod(user_id, refs):
  cur.execute(f"UPDATE ref_tod SET refs = {refs} WHERE user_id == {user_id}")
  db.commit()

async def edit_reftod_all():
  cur.execute(f"UPDATE ref_tod SET refs = {0}")
  db.commit()

async def get_reftod(user_id):
  bal = cur.execute(f"SELECT refs FROM ref_tod WHERE user_id == {user_id}").fetchone()
  if not bal:
    return [0]
    db.commit()
  else:
    return bal


async def get_reftod_all():
  res = cur.execute("SELECT * FROM ref_tod").fetchall()
  return res


async def edit_deposit(deposit):
  cur.execute(f"UPDATE statis SET deposit = {deposit}")
  db.commit()
async def edit_widhart(widhart):
  cur.execute(f"UPDATE statis SET widhart = {widhart}")
  db.commit()

async def edit_todeposit(todeposit):
  cur.execute(f"UPDATE statis SET todeposit = {todeposit}")
  db.commit()
async def edit_towidhart(towidhart):
  cur.execute(f"UPDATE statis SET towidhart = {towidhart}")
  db.commit()
async def get_statis():
  res = cur.execute("SELECT * FROM statis").fetchall()
  return res

async def create_mess(user_id, id_msg):
  ref = cur.execute(f"SELECT * FROM mess WHERE user_id == {user_id}").fetchone()

  if not ref:
    cur.execute("INSERT INTO mess VALUES(?, ?)", (user_id, id_msg))
    db.commit()
    return True
  else:
    return False

async def create_promocode(promo, forever, suma):
  ref = cur.execute(f"SELECT * FROM promocodes WHERE promo == '{promo}'").fetchone()

  if not ref:
    cur.execute("INSERT INTO promocodes VALUES(?, ?, ?)", (promo, forever, suma))
    db.commit()
    return True
  else:
    return False

async def dell_promocode(promo):
  cur.execute(f"DELETE FROM promocodes WHERE promo == ?", (promo,) )
  db.commit()


async def dell_promocode2():
  cur.execute(f"DELETE FROM promocodes")
  db.commit()

async def get_promo(promo):
  bal = cur.execute(f"SELECT * FROM promocodes WHERE promo == ?", (promo,)).fetchone()
  if not bal:
    return [0]
    db.commit()
  else:
    return bal








async def create_bal2(user_id, bal):
  ref = cur.execute(f"SELECT * FROM balances WHERE user_id == {user_id}").fetchone()

  if not ref:
    cur.execute("INSERT INTO balances VALUES(?, ?)", (user_id, bal))
    db.commit()
    return True
  else:
    return False

async def edit_mess(user_id, id_msg):
  cur.execute(f"UPDATE mess SET id_msg= {id_msg} WHERE user_id == {user_id}")
  db.commit()

async def get_mess(user_id):
  bal = cur.execute(f"SELECT id_msg FROM mess WHERE user_id == {user_id}").fetchone()
  if not bal:
    return [0]
    db.commit()
  else:
    return bal


async def create_gra(user_id1, user_id2):
  ref = cur.execute(f"SELECT * FROM duel_on WHERE user_id2 == {user_id2}").fetchone()

  if not ref:
    cur.execute("INSERT INTO duel_on VALUES(?, ?)", (user_id1, user_id2))
    db.commit()
    return True
  else:
    return False

async def create_peremog(user_id):
  ref = cur.execute(f"SELECT * FROM duel_peremog WHERE user_id == {user_id}").fetchone()

  if not ref:
    cur.execute("INSERT INTO duel_peremog VALUES(?, ?)", (user_id, 0))
    db.commit()
    return True
  else:
    return False
async def edit_peremog(user_id, peremog):
  cur.execute(f"UPDATE duel_peremog SET peremog = {peremog} WHERE user_id == {user_id}")
  db.commit()
async def get_peremog(user_id):
  bal = cur.execute(f"SELECT peremog FROM duel_peremog WHERE user_id == {user_id}").fetchone()
  if not bal:
    return [0]
    db.commit()
  else:
    return bal

async def create_balances(user_id):
  ref = cur.execute(f"SELECT * FROM balances WHERE user_id == {user_id}").fetchone()

  if not ref:
    cur.execute("INSERT INTO balances VALUES(?, ?)", (user_id, '0.0'))
    db.commit()
    return True
  else:
    return False

async def create_bonus(user_id, bonus):
  ref = cur.execute(f"SELECT * FROM bonuss WHERE user_id == {user_id}").fetchone()

  if not ref:
    cur.execute("INSERT INTO bonuss VALUES(?, ?)", (user_id, bonus))
    db.commit()
    return True
  else:
    return False

async def edit_duel_on(user_id1, user_id2):
  cur.execute(f"UPDATE duel_on SET user_id1 = {user_id1} WHERE user_id2 == {user_id2}")
  db.commit()


async def edit_duel_id2(user_id1, user_id2):
  cur.execute(f"UPDATE duel SET user_id2 = {user_id2} WHERE user_id1 == {user_id1}")
  db.commit()

async def edit_duel_user2(username2, user_id1):
  cur.execute(f"UPDATE duel SET username2 = '{username2}' WHERE user_id1 == {user_id1}")
  db.commit() 

async def new_duel(user_id1, username1, stavka, user_id2, username2):
  ref = cur.execute(f"SELECT * FROM duel WHERE user_id1 == {user_id1}").fetchone()

  if not ref:
    cur.execute("INSERT INTO duel VALUES(?, ?, ?, ?, ?)", (user_id1, username1, stavka, user_id2, username2))
    db.commit()
    return True
  else:
    return False

async def get_duel_on(user_id2):
  bal = cur.execute(f"SELECT user_id1 FROM duel_on WHERE user_id2 == {user_id2}").fetchone()
  if not bal:
    return [0]
    db.commit()
  else:
    return bal

async def get_all_duel():
  res = cur.execute('SELECT * FROM duel').fetchall()
  if not res:
    return False
  else:
    return res
async def get_duel(user_id):
  bal = cur.execute(f"SELECT * FROM duel WHERE user_id1 == {user_id}").fetchone()
  if not bal:
    return [0]
    db.commit()
  else:
    return bal


async def add_bonus(user_id, bonus):
  ref = cur.execute(f"SELECT * FROM bonuss WHERE user_id == {user_id}").fetchone()

  if not ref:
    cur.execute("INSERT INTO bonuss VALUES(?, ?)", (user_id, bonus))
    db.commit()
    return True
  else:
    cur.execute(f"UPDATE bonuss SET bonus = {bal} WHERE user_id == {user_id}")
    db.commit()
    return False
async def get_bonus(user_id):
  bal = cur.execute(f"SELECT bonus FROM bonuss WHERE user_id == {user_id}").fetchone()
  if not bal:
    return [0]
    db.commit()
  else:
    return bal
async def edit_bonus(user_id, bal):
  cur.execute(f"UPDATE bonuss SET bonus = {bal} WHERE user_id == {user_id}")
  db.commit() 

async def get_balance(user_id):
  bal = cur.execute(f"SELECT balans FROM users WHERE user_id == {user_id}").fetchone()
  db.commit()
  return bal
async def get_balance2(user_id):
  bal = cur.execute(f"SELECT balance FROM balances WHERE user_id == {user_id}").fetchone()
  db.commit()
  return bal

async def get_ref_all():
  ref_all = cur.execute('SELECT * FROM refer').fetchall()
  return ref_all



async def create_profile(user_id, username):
  user = cur.execute("SELECT 1 FROM users WHERE user_id == '{key}'".format(key=user_id)).fetchone()

  if not user:
    cur.execute("INSERT INTO users VALUES(?, ?, ?, ?)", (str(user_id), username, 0, 0))
    db.commit()

async def dell_user(user):
  cur.execute(f"DELETE FROM users WHERE user_id == ?", (user,) )
  db.commit()
async def dell_duel(user_id1):
  cur.execute(f"DELETE FROM duel WHERE user_id1 == ?", (user_id1,) )
  db.commit()

async def get_balance(user_id):
  bal = cur.execute(f"SELECT balans FROM users WHERE user_id == {user_id}").fetchone()
  db.commit()
  return bal

async def get_balance2(user_id):
  bal = cur.execute(f"SELECT balance FROM balances WHERE user_id == {user_id}").fetchone()
  db.commit()
  return bal

async def get_users_all():
  users = cur.execute(f"SELECT user_id FROM users").fetchall()
  db.commit()

  return users

async def get_refers(user_id):
  ref = cur.execute(f"SELECT refer FROM users WHERE user_id == {user_id}").fetchone()
  db.commit()

  return ref

async def get_username(user_id):
  na = cur.execute(f"SELECT name FROM users WHERE user_id == {user_id}").fetchone()
  db.commit()

  return na


async def edit_balance(user_id, bal):
  cur.execute(f"UPDATE users SET balans = {bal} WHERE user_id == {user_id}")
  db.commit()

async def edit_balance2(user_id, bal):
  cur.execute(f"UPDATE balances SET balance = {bal} WHERE user_id == {user_id}")
  db.commit()

async def get_user_ref(user_id):
  ref = cur.execute(f"SELECT refer FROM users WHERE user_id == {user_id}").fetchone()
  db.commit()

  return ref

async def edit_refp(user_id, refs):
  cur.execute(f"UPDATE users SET refer = {refs} WHERE user_id == ?", (user_id,))
  db.commit()

async def add_refer(user_one, user_tho):
  ref = cur.execute("SELECT 1 FROM refer WHERE user_one == ? AND user_tho == ?", (user_one, user_tho)).fetchone()

  if not ref:
    cur.execute("INSERT INTO refer VALUES(?, ?)", (user_one, user_tho))
    db.commit()
    return True
  else:
    return False
async def get_reffer_id(user_tho):
  ref = cur.execute(f"SELECT user_one FROM refer WHERE user_tho == {user_tho}").fetchone()
  db.commit()

  return ref
async def add_promok(promok, user):
  ref = cur.execute("SELECT 1 FROM user_promo WHERE promok == ? AND user == ?", (promok, user)).fetchone()

  if not ref:
    cur.execute("INSERT INTO user_promo VALUES(?, ?)", (promok, user))
    db.commit()
    return True
  else:
    return False

async def add_balances(user_id, bal):
  ref = cur.execute("SELECT 1 FROM balances WHERE user_id == ? AND balance == ?", (user_id, bal)).fetchone()

  if not ref:
    cur.execute("INSERT INTO balances VALUES(?, ?)", (user_id, bal))
    db.commit()
    return True
  else:
    return False


async def get_all():
  all_ = cur.execute(f"SELECT * FROM balances").fetchall()
  db.commit()

  return all_

async def get_all_from_userid(user_id):
  all_user = cur.execute(f"SELECT * FROM users WHERE user_id == {user_id}").fetchall()
  db.commit()

  return all_user
async def get_all_promok(promok):
  all_user = cur.execute(f"SELECT * FROM user_promo WHERE promok == '{promok}'").fetchall()
  db.commit()

  return all_user