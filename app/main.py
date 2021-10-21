# third-party imports
from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

# local imports
from . import schemas, models
from .database import Base, engine, SessionLocal


app = FastAPI()

# creating tables in the database
Base.metadata.create_all(bind=engine)


def get_conn():
    conn = SessionLocal()
    try:
        yield conn
    finally:
        conn.close()


@app.post('/tag', status_code=status.HTTP_201_CREATED)
def tag_create(request: schemas.TagCreate, conn: Session = Depends(get_conn)):
    new_tag = models.Tag(name=request.name)
    conn.add(new_tag)
    conn.commit()
    conn.refresh(new_tag)
    return new_tag


@app.get('/tag/{name}')
def tag_read(name, conn: Session = Depends(get_conn)):
    tag = conn.query(models.Tag).filter(models.Tag.name == name).first()

    if not tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'the {name} tag was not found.')

    return tag


@app.get('/tag', response_model=List[schemas.Tag])
def tag_list(conn: Session = Depends(get_conn)):
    return conn.query(models.Tag).all()


@app.put('/tag/{name}', status_code=status.HTTP_202_ACCEPTED)
def tag_update(name,
               request: schemas.TagCreate,
               conn: Session = Depends(get_conn)):
    tag = conn.query(models.Tag).filter(models.Tag.name == name)

    if not tag.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'the {name} tag was not found.')

    tag.update(request.dict())
    conn.commit()


@app.delete('/tag/{name}', status_code=status.HTTP_204_NO_CONTENT)
def tag_delete(name, conn: Session = Depends(get_conn)):
    tag = conn.query(models.Tag).filter(models.Tag.name == name)

    if not tag.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'the {name} tag was not found.')

    tag.delete(synchronize_session=False)
    conn.commit()
