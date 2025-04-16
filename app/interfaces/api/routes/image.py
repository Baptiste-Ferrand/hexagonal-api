from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.infrastructure.db.session import get_db
from app.infrastructure.db.repositories.sqlalchemy_image_repository import SQLAlchemyImageRepository
from app.infrastructure.db.repositories.sqlalchemy_image_like_repository import SQLAlchemyImageLikeRepository
from app.application.use_cases.like_image import LikeImageUseCase
from app.interfaces.api.auth_dependency import get_current_user_id

router = APIRouter(prefix="/images", tags=["images"])

@router.post("/{image_id}/like")
def like_image(
    image_id: UUID,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user_id)
):
    image_repo = SQLAlchemyImageRepository(db)
    like_repo = SQLAlchemyImageLikeRepository(db)
    use_case = LikeImageUseCase(image_repo, like_repo)

    try:
        use_case.execute(user_id=user_id, image_id=image_id)
        return {"message": "Image liked"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
