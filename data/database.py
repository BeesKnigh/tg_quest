import aiosqlite


class DataBase:
    def __init__(self, name: str, table: str) -> None:
        self.name = f'data/{name}'
        self.table = table

    async def create_table(self):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS search (
                "id"	INTEGER,
                "user_id"	INTEGER UNIQUE,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            """
            await cursor.executescript(query)
            await db.commit()

    async def search_ins(self, **kwargs) -> None:
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            await cursor.execute(
                """
                INSERT INTO users(
                user_id_1,
                user_id_2,
                ) VALUES (?, ?)
                """,
                **kwargs
            )

    async def register_pl(self, user_id) -> None:
        async with aiosqlite.connect(self.name) as db:

            cursor = await db.cursor()
            await cursor.execute(
                f"""
                INSERT INTO search (
                user_id
                ) VALUES ({user_id})
                """
            )
            await db.commit()

    async def round_game(self, user_id, round_id, defense, attack, health, session_id) -> None:
        async with aiosqlite.connect(self.name) as db:

            cursor = await db.cursor()
            await cursor.execute(
                f"""
                INSERT
                INTO
                game(user_id, round_id, defense, attack, health, session_id)
                VALUES({user_id}, ?, ?, ?, ?, ?)
                """
            )
            await db.commit()

    async def count_pl(self):
        async with aiosqlite.connect(self.name) as db:

            cursor = await db.cursor()
            result = await cursor.execute(
                """
                SELECT COUNT(*) FROM search
                """
            )
            resultfetch = await result.fetchone()
            await db.commit()
            return resultfetch[0]

    async def select_to_pl(self) -> None:
        async with aiosqlite.connect(self.name) as db:

            cursor = await db.cursor()
            result = await cursor.execute(
                """
                SELECT * FROM search limit 2
                """
            )
            resultfetch = await result.fetchall()
            await db.commit()
            return resultfetch

    async def delete_in_search(self) -> None:
        async with aiosqlite.connect(self.name) as db:

            cursor = await db.cursor()
            await cursor.executescript(
                """
                DELETE FROM search; DELETE FROM sqlite_sequence WHERE name = 'search'
                """
            )
            await db.commit()

    async def add_to_game(self) -> None:
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            await cursor.execute(
                """
                INSERT INTO game (user_id, round_id, step, health) VALUES (?, ?, ?, ?)
                SELECT
                  s1.user_id as user1_id,
                  3 as health1,
                  s2.user_id as user2_id,
                  3 as health2
                FROM
                  (SELECT user_id FROM search WHERE id = 1) s1
                  CROSS JOIN
                  (SELECT user_id FROM search WHERE id = 2) s2;
                """
            )
            await db.commit()

    async def get_user_id(self) -> None:
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            result = await cursor.execute(
                """
                SELECT user1_id FROM players
                """
            )
            resultfetch = await result.fetchone()
            await db.commit()
            return resultfetch

    async def switch_1(self) -> None:
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            await cursor.execute(
                """
                INSERT OR REPLACE INTO game (attack, defense)
                SELECT
                  s1.user_id as attack,
                  s2.user_id as defense,
                FROM
                  (SELECT user1_id FROM players WHERE id = 1) s1
                  CROSS JOIN
                  (SELECT user2_id FROM players WHERE id = 2) s2;
                """
            )
            await db.commit()

    async def switch_2(self) -> None:
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            await cursor.execute(
                """
                INSERT OR REPLACE INTO game (attack, defense)
                SELECT
                  s1.user_id as attack,
                  s2.user_id as defense,
                FROM
                  (SELECT user2_id FROM players WHERE id = 1) s1
                  CROSS JOIN
                  (SELECT user1_id FROM players WHERE id = 2) s2;
                """
            )
            await db.commit()

    async def last_health(self, user_id) -> None:
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            await cursor.execute(
                f"""
                SELECT health FROM game WHERE user_id = {user_id} 
                ORDER BY health ASC
                LIMIT 1
                """
            )
            await db.commit()

    async def select_rounds(self, session_id) -> None:
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            result = await cursor.execute(
                """
                SELECT round_id FROM game WHERE session_id = ?
                """
            )
            resultfetch = await result.fetchone()
            await db.commit()
            return resultfetch[0]

    async def insert_legs_def(self) -> None:
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            await cursor.execute(
                """
                INSERT OR REPLACE INTO game (attack) VALUES (1)
                """
            )
            await db.commit()

