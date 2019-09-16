from neo4j import GraphDatabase
from datetime import datetime


class Connection:
  def __init__(self):
    self.uri = "bolt://localhost:7687"
    self.driver = GraphDatabase.driver(self.uri, auth=("neo4j", "123123"))

  def create_user(self, username, email, password, role):
    query = "CREATE (n: User {username: $username, email: $email, password: $password, role: $role}) RETURN id(n)"
    with self.driver.session() as session:
      ans = session.run(
        query, username=username, email=email, password=password, role=role).single().value()
      session.close()
      return ans

  def make_a_question(self, id_user, topic, question, date):
    query = "MATCH (a: User)\n"
    query += "WHERE id(a) = {}\n".format(id_user)
    query += "CREATE (p: Post {type: 'Q', topic: $topic, question: $question, date: $date})\n"
    query += "CREATE (a)-[r: QUESTION ]->(p)\n"
    query += "RETURN id(p)"
    with self.driver.session() as session:
      ans = session.run(
        query, topic=topic, question=question, date=date).single().value()
      session.close()


cc = Connection()
id_test = cc.create_user("test", "test@gmail.com", "123123", "Estudiante")
cc.make_a_question(id_test, "IT", "What can I ..?", datetime.today())
