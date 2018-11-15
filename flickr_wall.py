import flickrapi
import pprint
import os

from xml.etree import ElementTree as ET
           
api_key = '################################'
api_secret = '################'
              
flickr   = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
flickr_e = flickrapi.FlickrAPI(api_key, api_secret, format='etree')

sets = flickr.photosets.getList(user_id='83186018@N00')
pp   = pprint.PrettyPrinter(indent=4)

albums = {}

list = open('albums.txt', 'w')

size = "_c" #(800x600)


for set in sets['photosets']['photoset']:
    try:
        id = set['id']
        title= set['title']['_content']    

        albums[id] = title 
        list.write(id + ' , "' + title + '"\n')
    
        albumfile = open('albums/' + id, 'w')

        for photo in flickr_e.walk_set(id):
            try:
                photo_id = photo.get('id')
                secret = photo.get('secret')
                farm  = photo.get('farm')
                server = photo.get('server')
                url="https://farm" + farm + ".staticflickr.com/" + server + "/" + photo_id + "_" + secret + size + ".jpg"
                albumfile.write(url + "\n")
            except e:
                print(e)
                
            albumfile.close()
        except e2:
            print(e2)

        list.close()
