from sqlalchemy import Column, Integer, BigInteger, Boolean, String, DateTime, Enum, Index
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from . import db


class FileSystem(db.Model):
    __tablename__ = 'RAG_FILE_SYSTEM'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(255), default="")
    file_name = Column(String(255), default="")
    file_path = Column(String(255), default="")
    file_size = Column(String(255), default="")
    file_extension = Column(String(255), default="")
    file_status = Column(String(255), default="")
    create_at = Column(DateTime, default=func.now())
    note = Column(String(255), default="")

    # 開AZURE_BLOB儲存空間欄位
    uuid_name = Column(String(255), default="")
    azure_container_name = Column(String(255), default="")
    azure_blob_name = Column(String(255), default="")

    # 檔案審查欄位
    file_purpose = Column(String(255), default="")  # 檔案目的： question:考題上傳 knowledge：專科知識上傳 others：其他
    is_file_useful = Column(Boolean)  # 管理者審核這個檔案是否有用
    manager_id = Column(String(255), default="")
    manager_comment = Column(String(255), default="")
    censor_status = Column(Integer, default=0)  # 0:未審核 1:審核中 2:審核通過 3:審核不通過
    ocr_status = Column(Integer, default=0)  # 0:未OCR 1:OCR中 2:OCR完成
    ocr_text = Column(LONGTEXT, default="")  # OCR辨識文字

    # 專科知識類
    knowledge_department = Column(String(255), default="")  # 科系 生科系
    knowledge_professor = Column(String(255), default="")  # 指定用書教授名
    knowledge_course = Column(String(255), default="")  # 課程 生物學
    knowledge_year = Column(String(255), default="")  # 出場年份 1999

    # 考題類
    question_department = Column(String(255), default="")  # 科系 生科系
    question_professor = Column(String(255), default="")  # 出題教授名 王大明
    question_course = Column(String(255), default="")  # 課程 生物學
    question_year = Column(String(255), default="")  # 出題學年 110
    question_semester = Column(String(255), default="")  # 學期 上學期 #亦烜拿來存學期
    question_exam_type = Column(String(255), default="")  # 考試類型 期中考
    question_exam_question_type = Column(Integer, default=0)  # 題型 0:未分類 1:選擇題 2:填充題 3:問答題 4:簡答題 5:計算題 6:繪圖題 7: 是非題 8:其他

    def to_dict(self):
        # Define the to_dict() method to convert ModelEvaluation to a dictionary
        return {
            "id": self.id,
            "user_id": self.user_id,
            "file_name": self.file_name,
            "file_path": self.file_path,
            "file_size": self.file_size,
            "file_extension": self.file_extension,
            "file_status": self.file_status,
            "create_at": self.create_at,
            "note": self.note,
            "uuid_name": self.uuid_name,
            "azure_container_name": self.azure_container_name,
            "azure_blob_name": self.azure_blob_name,
            "file_purpose": self.file_purpose,
            "is_file_useful": self.is_file_useful,
            "manager_id": self.manager_id,
            "manager_comment": self.manager_comment,
            "censor_status": self.censor_status,
            "ocr_status": self.ocr_status,
            "ocr_text": self.ocr_text,
            "knowledge_department": self.knowledge_department,
            "knowledge_professor": self.knowledge_professor,
            "knowledge_course": self.knowledge_course,
            "knowledge_year": self.knowledge_year,
            "question_department": self.question_department,
            "question_professor": self.question_professor,
            "question_course": self.question_course,
            "question_year": self.question_year,
            "question_semester": self.question_semester,
            "question_exam_type": self.question_exam_type,
            "question_exam_question_type": self.question_exam_question_type
        }
