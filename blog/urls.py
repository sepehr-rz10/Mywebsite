from django.urls import path
from blog.views import * 


app_name = 'blog'

urlpatterns = [
    
    path('' , blog_view , name = 'index' ),
    path('<int:pid>' , blog_single , name = 'single'),
    #path('post-<int:pid>' , test , name = 'test')


    
    
    #path('<str:name>/lastname/<str:family_name>/age/<int:age>' , test , name = 'test')

    
]