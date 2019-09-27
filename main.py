from neo4j import GraphDatabase
from datetime import datetime


class Connection:
  def __init__(self):
    self.uri = "bolt://localhost:7687"
    self.driver = GraphDatabase.driver(self.uri, auth=("neo4j", "123123"))

  def list_questions(self):
    query = "MATCH (p: Post {type: 'Q'})\n"
    query += "RETURN p\n"
    query += "ORDER BY p.date LIMIT 5"
    with self.driver.session() as session:
      ans = session.run(query).value()
      session.close()
    return ans

  def list_answers_to_question(self, id_question):
    query = "MATCH (p: Post)-[:ANSWER_TO]-(r: Post)\n"
    query += "WHERE id(p) = {}\n".format(id_question)
    query += "RETURN r\n"
    query += "ORDER BY p.date LIMIT 5"
    with self.driver.session() as session:
      ans = session.run(query).value()
      session.close()
    return ans

  def login(self, username, password):
    query = "MATCH (a: User {username: $username, password: $password})\n"
    query += "RETURN id(a)"
    with self.driver.session() as session:
      ans = session.run(query, username=username, password=password).single()
      if ans is not None:
       ans = ans.value()
      session.close()
    return ans

  def create_user(self, name, username, email, password, role):
    query = "CREATE (n: User {username: $username, name: $name, email: $email, password: $password, role: $role}) RETURN id(n)"
    with self.driver.session() as session:
      ans = session.run(
        query, username=username, name=name, email=email, password=password, role=role).single().value()
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

  def make_a_answer(self, id_user, id_question, answer, date):
    query = "MATCH (a: User), (w: Post)\n"
    query += "WHERE id(a) = {} and id(w) = {}\n".format(id_user,id_question)
    query += "CREATE (p: Post {type: 'A', answer: $answer, date: $date})\n"
    query += "CREATE (a)-[r: ANSWER]->(p)\n"
    query += "CREATE (w)-[:ANSWER_TO]->(p)\n"
    query += "RETURN id(p)"
    with self.driver.session() as session:
      ans = session.run(
        query,answer=answer, date=date).single().value()
      session.close()
      return ans

  def make_vote(self,voteKind,id_user,id_ans,censure,classifi):
    query = "MATCH (a: User)\n"
    query += "WHERE id(a) = {}\n".format(id_user)
    query += "MATCH (p:Post)\n"
    query += "WHERE id(p)= {}\n".format(id_ans)
    query += "CREATE (a)-[:VOTE3 {type:$voteKind,censure:$censure, classifi:$classifi, date: $date}]->(p)\n"
    with self.driver.session() as session:
      ans = session.run(
        query, voteKind=voteKind,censure=censure, classifi=classifi, date=datetime.now()).single()
      session.close()
      return ans

  def get_last_answered_users_by_user(self, id_user):
    query = "with date() - duration({years: 1}) AS delta\n"    
    query += "match (a: User)-[:ANSWER]-(r:Post)\n"
    query += "where id(a) = {} and r.date >= delta\n".format(id_user)
    query += "match (user: User)-[:QUESTION]-()-[:ANSWER_TO]-(r: Post)\n"
    query += "return user\n"
    with self.driver.session() as session:
      ans = session.run(
        query).value()
      session.close()
      return ans

  def search(self, id_user):
    query = "MATCH(usuario: User)-[:QUESTION]->(preguntas)\n"
    query += "WHERE id(usuario)={}\n".format(id_user)
    query += "WITH preguntas\n"
    query += "ORDER BY preguntas.date limit 5\n"
    query += "MATCH(preguntas)-[:ANSWER_TO]->(respuestas)\n"
    query += "RETURN [preguntas, respuestas]"
    with self.driver.session() as session:
      ans = session.run(
        query).value()
      session.close()
      return ans

  def tree(self, id_user):
    tree = []
    first = self.get_last_answered_users_by_user(id_user)
    tree.append(first)
    
    second = []
    for user in first:
      second.extend(self.get_last_answered_users_by_user(user.id))
    tree.append(second)

    thrid = []
    for user in second:
      thrid.extend(self.get_last_answered_users_by_user(user.id))
    tree.append(thrid)


    four = []
    for user in thrid:
      four.extend(self.get_last_answered_users_by_user(user.id))
    tree.append(four)

    return tree



#cc = Connection()
#id_test = cc.create_user("hola", "test@gmail.com", "123123", "Estudiante")
#id_post = cc.make_a_question(id_test, "IT", "What can I do for carlos loveme?", "24/06/12")
#id_answer = cc.make_a_answer(id_test, id_post, "The answer is", "24/06/12")
#cc.make_vote(-1,id_test,id_answer, True, "good")
