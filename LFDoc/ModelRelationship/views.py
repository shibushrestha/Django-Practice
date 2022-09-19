from django.http import HttpResponse
from django.shortcuts import render
from ModelRelationship.RelationExample import Entry, Blog, Author

def home(request):
    allEntries = Entry.objects.order_by('pub_date')
    context = {'allEntries':allEntries}
    return render(request, 'ModelRelationship/home.html', context)


# JSONPlaceholder (Getting fake data from JSONPlaceholder to populate the database)
def get_data(request):
    import requests
    url1 = 'https://jsonplaceholder.typicode.com/posts'
    r1 = requests.get(url1)
    data1 = r1.json()
    url2 = 'https://jsonplaceholder.typicode.com/users'
    r2 = requests.get(url2)
    data2 = r2.json()

    '''
    for x in data1:
        headline = x['title']
        body_text = x['body']
        pub_date = "2022-05-16"
        mod_date = "2022-05-16"
        b = Blog.objects.get(name="Shibu Blog")
        e = Entry.objects.create(blog=b, headline = headline, body_text=body_text, pub_date=pub_date, mod_date=mod_date)
    for a in data2:
        author_name = a['name']
        email = a['email']
        author = Author.objects.create(name=author_name, email=email)
    '''
    print(type(data2))
    return HttpResponse('Here is your data')