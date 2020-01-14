from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('boxes/', views.BoxListView.as_view(), name='boxes'),
    path('boxes/<int:pk>', views.BoxDetailView.as_view(), name='box-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',
         views.AuthorDetailView.as_view(), name='author-detail'),
]


urlpatterns += [
    path('myboxes/', views.createdboxesByUserListView.as_view(), name='my-created'),
    path(r'borrowed/', views.createdboxesAllListView.as_view(), name='all-created'),  # Added for challenge
]



# Add URLConf to create, update, and delete authors
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

# Add URLConf to create, update, and delete boxes
urlpatterns += [
    path('boxes/create/', views.BoxCreate.as_view(), name='box_create'),
    path('boxes/<int:pk>/update/', views.BoxUpdate.as_view(), name='box_update'),
    path('boxes/<int:pk>/delete/', views.BoxDelete.as_view(), name='box_delete'),
]
