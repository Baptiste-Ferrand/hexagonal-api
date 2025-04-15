from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.infrastructure.db.session import get_db
from app.infrastructure.db.repositories.sqlalchemy_image_repository import SQLAlchemyImageRepository
from app.infrastructure.db.repositories.sqlalchemy_image_like_repository import SQLAlchemyImageLikeRepository
from app.application.use_cases.like_image import LikeImageUseCase

# Remplace ceci plus tard par ton vrai système d'authentification
def get_current_user_id() -> UUID:
    # Simule un user connecté pour l'instant
    return UUID("11111111-1111-1111-1111-111111111111")

router = APIRouter(prefix="/images", tags=["images"])

@router.post("/{image_id}/like")
def like_image(image_id: UUID, db: Session = Depends(get_db)):
    user_id = get_current_user_id()

    image_repo = SQLAlchemyImageRepository(db)
    like_repo = SQLAlchemyImageLikeRepository(db)
    use_case = LikeImageUseCase(image_repo, like_repo)

    try:
        use_case.execute(user_id=user_id, image_id=image_id)
        return {"message": "Image liked"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
