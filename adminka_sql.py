import sqlite3 as sq


async def db_start2():
	global db, cur

	db = sq.connect('admin_base.db')

	cur = db.cursor()

	cur.execute("CREATE TABLE IF NOT EXISTS uah(balance_n INTEGER, balance_w INTEGER, balance_m INTEGER)")

	db.commit()

async def create_tran():
	uah = cur.execute("SELECT 1 FROM uah").fetchone()

	if not uah:
		cur.execute("INSERT INTO uah VALUES(?, ?, ?)", (0, 0, 0))
		db.commit()

#GET
async def get_balance_n():
	bal = cur.execute(f"SELECT balance_n FROM uah").fetchone()
	db.commit()
	return bal
async def get_balance_w():
	bal = cur.execute(f"SELECT balance_w FROM uah").fetchone()
	db.commit()
	return bal
async def get_balance_m():
	bal = cur.execute(f"SELECT balance_m FROM uah").fetchone()
	db.commit()
	return bal

#EDIT
async def edit_balance_n(bal_n):
	cur.execute(f"UPDATE uah SET balance_n = {bal_n}")
	db.commit()
async def edit_balance_w(bal_w):
	cur.execute(f"UPDATE uah SET balance_w = {bal_w}")
	db.commit()
async def edit_balance_m(bal_m):
	cur.execute(f"UPDATE uah SET balance_m = {bal_m}")
	db.commit()
