from database.models import async_session
from database.models import Application, User
from sqlalchemy import select
from sqlalchemy.sql import text



async def set_application(socialNetworkId : str,fullname: str, age:int, address: str, phoneNumber: int, docPhoto: bytes, userPhoto: bytes):
    new_application = Application(socialNetworkId = socialNetworkId,fullname = fullname,age=age,address=address,phoneNumber=phoneNumber,docPhoto=docPhoto,userPhoto=userPhoto)
    async with async_session() as session:
        session.add(new_application)
        await session.commit()
        await session.close()



async def check_my_application(phoneNumber: str,socialNetworkId : str):
    async with async_session() as session:
        application = await session.scalar(select(Application).where(Application.phoneNumber == phoneNumber,Application.socialNetworkId == socialNetworkId))

        if not application:
            return False
        else:
            return True


async def check_application(phoneNumber: str):
    async with async_session() as session:
        application = await session.scalar(select(Application).where(Application.phoneNumber == phoneNumber))

        if not application:
            return False
        else:
            return True
        
async def check_application_byId(socialNetworkId: str):
    async with async_session() as session:
        application = await session.scalar(select(Application).where(Application.socialNetworkId == socialNetworkId))

        if not application:
            return False
        else:
            return True


async def check_role(socialNetworkId: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.socialNetworkId == socialNetworkId))
        return user
    

async def get_applications():
    async with async_session() as session:
        # выполните запрос
        result = await session.execute(text("SELECT * FROM applications"))
        applications = result.fetchall()  # Получаем все строки результата

        # Преобразуем кортежи в объекты Application
        application_objects = [Application(fullname=row[2],age=row[3],address=row[4],phoneNumber=row[5]) for row in applications]

        return application_objects

async def get_applications_byRegion(region: str):
    async with async_session() as session:
        # выполните запрос
        result = await session.execute(text(f"SELECT * FROM applications WHERE address = '{region}'"))
        applications = result.fetchall()  # Получаем все строки результата

        # Преобразуем кортежи в объекты Application
        application_objects = [Application(fullname=row[2],age=row[3],address=row[4],phoneNumber=row[5]) for row in applications]

        return application_objects

async def get_applications_byAge(startAge: int,endAge: int):
    async with async_session() as session:
        # выполните запрос
        result = await session.execute(text(f"SELECT * FROM applications WHERE age BETWEEN {startAge} AND {endAge}"))
        applications = result.fetchall()  # Получаем все строки результата

        # Преобразуем кортежи в объекты Application
        application_objects = [Application(fullname=row[2],age=row[3],address=row[4],phoneNumber=row[5]) for row in applications]

        return application_objects


async def delete_application(socialNetworkId: str):
    async with async_session() as session:
        application = await session.scalar(select(Application).where(Application.socialNetworkId == socialNetworkId))
        await session.delete(application)
        await session.commit()
        await session.close()

async def add_employee(socialNetworkId: str,role: str):
    user = User(socialNetworkId=socialNetworkId,role=role)

    async with async_session() as session:
        session.add(user)
        await session.commit()
        await session.close()

async def add_admin(socialNetworkId: str,role: str):
    user = User(socialNetworkId=socialNetworkId,role=role)

    async with async_session() as session:
        session.add(user)
        await session.commit()
        await session.close()

async def remove_employee(socialNetworkId: str,role: str):

    async with async_session() as session:
        user = await session.scalar(select(User).where(User.socialNetworkId == socialNetworkId and User.role == role))
        await session.delete(user)
        await session.commit()
        await session.close()