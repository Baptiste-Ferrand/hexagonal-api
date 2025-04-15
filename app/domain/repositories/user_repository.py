from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional
from app.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
