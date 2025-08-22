movie_a={"marco","f1","batman","bleach","demon slayer","attack on titan","one piece","naruto"}
movie_b={"spiderman","batman","superman","ironman","f1","hulk","demon slayer","attack on titan"}
movie_both_watch=movie_a.intersection(movie_b)
print("movies both like:",movie_both_watch)
movie_either_watch=movie_a.union(movie_b)
print("movies either like:",movie_either_watch)
movie_a_only=movie_a.difference(movie_b)
print("movies only a like:",movie_a_only)
movie_b_only=movie_b.difference(movie_a)
print("movies only b like:",movie_b_only)
