import asyncio
from threading import Thread


async def asfunc1():
    print("async1 start")

    async def asfunc2():
        print("async2 start")

        async def asfunc3():
            print("async3 start")
            await asyncio.sleep(2)
            print("async3 end")

        def func2():
            print("normal2 start")
            asyncio.run(asfunc3())
            print("normal2 end")

        await asyncio.sleep(2)
        thread2 = Thread(target=func2)
        thread2.start()

        print("async2 end")

    def func1():
        print("normal1 start")
        asyncio.run(asfunc2())
        print("normal1 end")

    thread1 = Thread(target=func1)
    thread1.start()

    print("async1 end")

asyncio.run(asfunc1())
