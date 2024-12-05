from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import String, Integer,LargeBinary


engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite1')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass




class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(String(10))
    socialNetworkId: Mapped[str] = mapped_column(String(50))
    





class Application(Base):
    __tablename__ = 'applications'

    id: Mapped[int] = mapped_column(primary_key=True)
    socialNetworkId: Mapped[str] = mapped_column(String(50))
    fullname: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)
    address: Mapped[str] = mapped_column(String(50))
    phoneNumber: Mapped[int] = mapped_column(Integer)
    docPhoto: Mapped[LargeBinary] = mapped_column(LargeBinary)
    userPhoto: Mapped[LargeBinary] = mapped_column(LargeBinary)



async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)