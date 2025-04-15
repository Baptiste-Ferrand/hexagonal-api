from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.infrastructure.db.models.base import Base

class ImageModel(Base):
    __tablename__ = "images"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    data_url = Column(String, nullable=False)
    like_count = Column(Integer, default=0)

    owner = relationship("UserModel", backref="images")
