from Tourists import Tourists
from db_config import local_session, create_all_entities
from Attractions import Attractions
from Db_repo import DbRepo
from Visits import Visits

# create tables
create_all_entities()

repo = DbRepo(local_session)

t1 = Tourists(name='david', origin_country='usa')
t2 = Tourists(name='rafael', origin_country='mexico')
tourist_ls = [t1, t2]
#repo.add_all(tourist_ls)

at1 = Attractions(name='central park', price=30)
at2 = Attractions(name='spy museum', price=22)
at3 = Attractions(name='eiffel tower', price=75)
attraction_list = [at1, at2, at3]

#repo.add_all(attraction_list)

v1 = Visits(tourist_id='1', attraction_id='2', year_of_visit=2009)
v2 = Visits(tourist_id='1', attraction_id='1', year_of_visit=2020)
v3 = Visits(tourist_id='2', attraction_id='3', year_of_visit=2017)
v4 = Visits(tourist_id='2', attraction_id='2', year_of_visit=2019)
visits_list = [v1, v2, v3, v4]

#repo.add_all(visits_list)

print(repo.get_by_condition(Visits, lambda query: query.filter(Tourists.id == 1).all()))
print(repo.get_by_condition(Visits, lambda query: query.filter(Attractions.id == 1).all()))



