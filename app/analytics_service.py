# analytics_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from app.analytics_models import UserConversion

class AnalyticsService:
    @classmethod
    async def log_user_conversion(cls, session: AsyncSession, user_id: int):
        """
        Logs a user conversion event to the database.

        Args:
            session (AsyncSession): The asynchronous database session.
            user_id (int): The ID of the user who performed the conversion.
        """
        # Logic to log user conversion event to the database
        conversion_event = UserConversion(user_id=user_id)
        session.add(conversion_event)
        await session.commit()
