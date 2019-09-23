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
      return ans

  def make_a_answer(self, id_user, id_question, topic, answer, date):
    query = "MATCH (a: User), (w: Post)\n"
    query += "WHERE id(a) = {} and id(w) = {}\n".format(id_user,id_question)
    query += "CREATE (p: Post {type: 'A', topic: $topic, answer: $answer, date: $date})\n"
    query += "CREATE (a)-[r: ANSWER]->(p)\n"
    query += "CREATE (w)-[:ANSWER_TO]->(p)\n"
    query += "RETURN id(p)"
    with self.driver.session() as session:
      ans = session.run(
        query, topic=topic, answer=answer, date=date).single().value()
      session.close()
      return ans

  def make_vote(self,voteKind,id_user,id_post):
    query = "MATCH (a: User)\n"
    query += "WHERE id(a) = {}\n".format(id_user)
    query += "MATCH (p:Post)\n"
    query += "WHERE id(p)= {}\n".format(id_post)
    query += "CREATE (a)-[:VOTE2 {type:[$voteKind]}]->(p)\n"
    with self.driver.session() as session:
      ans = session.run(
        query, voteKind=voteKind).single()
      session.close()
      return ans

cc = Connection()
id_test = cc.create_user("hola", "test@gmail.com", "123123", "Estudiante")
id_post = cc.make_a_question(id_test, "IT", "What can I do for carlos loveme?", "24/06/12")
id_answer = cc.make_a_answer(id_test, id_post,"IT2", "The answer is", datetime.today())
cc.make_vote(-1,id_test,id_answer)



