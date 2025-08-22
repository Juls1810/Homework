from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:19932009@localhost:5432/Julia"
db = create_engine(db_connection_string)


def test_insert():
    sql = text("Select count(*) from subject")
    total = db.execute(sql).scalar()
    print(total)
    sql = text("INSERT INTO subject(subject_title, subject_id) VALUES (:title, :id)")
    db.execute(sql, {"title": "honey", "id": total})
    sql = text("Select * from subject")
    result = db.execute(sql)
    rows = result.fetchall()
    assert rows[-1][1] == "honey"


def test_update():
    sql = text("Select count(*) from subject")
    total = db.execute(sql).scalar()
    print(total)
    sql = text("UPDATE subject SET subject_title = :subj_tit WHERE subject_id = :subj_id")
    db.execute(sql, subj_tit='julia', subj_id=total-1)
    sql = text("Select * from subject")
    result = db.execute(sql)
    rows = result.fetchall()
    assert rows[-1][1] != "honey"
    assert rows[-1][1] == "julia"


def test_delete():
    sql = text("Select count(*) from subject")
    total = db.execute(sql).scalar()-1
    print(total)
    sql = text("DELETE FROM subject WHERE subject_id = :id")
    db.execute(sql, id=total)
    sql = text("SELECT * FROM subject WHERE subject_id = :id")
    row = db.execute(sql, {"id": total}).fetchone()
    assert row is None
