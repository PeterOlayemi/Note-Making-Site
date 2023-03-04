from django.urls import path
from . import views

app_name='note'

urlpatterns = [
    path('', views.index, name='index'),
    path('note/', views.note, name='note'),
    path('draft_notes/', views.draft, name='draft'),
    path('add_note/', views.addnote, name='addnote'),
    path('detail_note/<int:_id>', views.notedetail, name='detailnote'),
    path('detail_draft/<int:_id>', views.draftdetail, name='detaildraft'),
    path('delete/<int:_id>', views.deletenote, name='delete'),
    path('edit_note/<int:_id>', views.editnote, name='editnote'),
    path('publish_draft/<int:_id>', views.publish, name='publish'),
]
