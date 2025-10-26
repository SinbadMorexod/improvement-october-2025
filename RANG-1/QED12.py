# pomodoro | 
""" 


"""







import asyncio

async def make_coffee():
    print("Начинаем варить кофе")
    await asyncio.sleep(5)  # ждём 2 секунды
    print("Кофе готов!")




async def main():
    await make_coffee()

asyncio.run(main())
