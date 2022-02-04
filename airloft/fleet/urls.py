from django.urls import path
from . import views


urlpatterns = [
    ############## Project ##############
    path("create/aircraft", views.CreateAircraftApiview.as_view(), name="add_airraft"),
    path("create/airport", views.CreateAirportApiview.as_view(), name="add_airport"),
    path("create/flight", views.CreateFlightApiview.as_view(), name="add_flight"),

    # path('projects', views.RetriveProjectsApiView.as_view(), name='list_projects'),
    # path('projects/me', views.RetriveMyProjectsApiView.as_view(), name='list_my_projects'),
    # path('project/<int:id>', views.RetriveOneProjectApiview.as_view(), name='list_a_project'),
    # path('project/update/<int:pk>', views.UpdateProjectApiview.as_view(), name='update_project'),
    # path('project/delete/<int:pk>', views.DeleteProjectApiview.as_view(), name='delete_project'),
    # ############# ProjectActivity #############
    # path('create/activity', views.CreateProjectActivityApiview.as_view(), name='add_activity'),
    # path('activitys', views.RetriveProjectsActivitiesApiView.as_view(), name='list_activities'),
    # path('activity/update/<int:pk>', views.UpdateProjectActivityApiview.as_view(), name='update_a_activity'),
    # path('activity/delete/<int:pk>', views.DestroyProjectActivityApiview.as_view(), name='list_update_delete_activity'),
    # path('analytics/activity/duration/<int:user>/<int:project>', views.GetIndividualProjectActivityTime.as_view(), name='total_individual_project_activity_time'),
    # path('analytics/activity/duration/<int:project>', views.GetTotalProjectActivityTime.as_view(), name='total_project_activity_time'),
]
