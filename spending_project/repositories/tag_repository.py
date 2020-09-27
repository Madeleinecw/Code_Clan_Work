from db.run_sql import run_sql
from models.merchant import Merchant
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (tag) VALUES (%s)"
    values = [tag]
    run_sql(sql, values)

def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for result in results:
        tag = Tag(result["tag"])
        tags.append(tag)
    return tags

def select(tag):
    sql = "SELECT * FROM tags WHERE tag = %s"
    values = [tag]
    result = run_sql(sql, values)[0]
    tag = Tag(result["tag"])
    return tag

def delete_all():
    sql = 'DELETE FROM tags'
    run_sql(sql)

def delete(tag):
    sql = "DELETE FROM tags WHERE tag = %s"
    values = [tag]
    run_sql(sql, values)

def update(tag):
    sql = "UPDATE tags SET tag = %s"
    values = [tag]
    run_sql(sql, values)
