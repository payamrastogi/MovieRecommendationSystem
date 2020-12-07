# importing the module 
import imdb 
   
# creating instance of IMDb 
ia = imdb.IMDb() 
   
# name  
name = "cube"
   
# searching the name  
search = ia.search_movie(name) 
  
  
# loop for printing the name and id 
for i in range(len(search)): 
      
    # getting the id 
    id = search[i].movieID 
      
    # printing it 
    print(search[i]['title'] + " : " + id ) 
    print(search[i])


movie = ia.get_movie('0094226')
print (movie['title'])
print (movie.current_info)
#print (movie['main'])
print (movie.infoset2keys)
print (movie['year'])
print (movie['art directors'])
print (movie['art directors'][0].personID)
print (movie['art directors'][0]['name'])
print(ia.get_movie_infoset())