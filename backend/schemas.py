from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    email: str
    display_name: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserWithProjectResponse(UserResponse):
    projects: List["ProjectResponse"] = []

    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    project_name: str
    project_description: Optional[str] = None
    needle_size: Optional[int] = None
    yarn: Optional[str] = None
    project_comments: Optional[str] = None
    project_picture: Optional[str] = None

class ProjectCreate(ProjectBase):
    user_id: int

class ProjectUpdate(BaseModel):
    project_name: Optional[str] = None
    project_description: Optional[str] = None
    needle_size: Optional[int] = None
    yarn: Optional[str] = None
    project_comments: Optional[str] = None
    project_picture: Optional[str] = None

class ProjectResponse(ProjectBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True

class CounterBase(BaseModel):
    stitch_counter: int
    row_counter: int
    counter_comments: Optional[str] = None

class CounterUpdate(BaseModel):
    stitch_counter: Optional[int] = None
    row_counter: Optional[int] = None
    counter_comments: Optional[str] = None

class CounterResponse(CounterBase):
    id: int
    project_id: int
    row_adjustments: List["RowAdjustmentResponse"] = []
    class Config:
        orm_mode = True

class RowAdjustmentBase(BaseModel):
    row_number: int
    increases: int
    decreases: int

class RowAdjustmentUpdate(BaseModel):
    row_number: int
    increases: Optional[int] = 0
    decreases: Optional[int] = 0

class RowAdjustmentResponse(RowAdjustmentBase):
    id: int
    counter_id: int
    class Config:
        orm_mode = True
