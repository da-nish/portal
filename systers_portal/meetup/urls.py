from django.conf.urls import url

from meetup.views import (MeetupLocationAboutView, MeetupLocationList, MeetupView,
                          MeetupLocationMembersView, AddMeetupView, DeleteMeetupView,
                          EditMeetupView, UpcomingMeetupsView, PastMeetupListView,
                          MeetupLocationSponsorsView, RemoveMeetupLocationMemberView,
                          AddMeetupLocationMemberView, RemoveMeetupLocationOrganizerView,
                          MakeMeetupLocationOrganizerView, ApproveMeetupLocationJoinRequestView,
                          RejectMeetupLocationJoinRequestView, MeetupLocationJoinRequestsView,
                          AddMeetupLocationView, EditMeetupLocationView, DeleteMeetupLocationView,
                          JoinMeetupLocationView, AddMeetupCommentView, EditMeetupCommentView,
                          DeleteMeetupCommentView, RsvpMeetupView, RsvpGoingView,
                          AddSupportRequestView, EditSupportRequestView, DeleteSupportRequestView,
                          SupportRequestView, SupportRequestsListView, ApproveSupportRequestView,
                          RejectSupportRequestView, UnapprovedSupportRequestsListView,
                          AddSupportRequestCommentView, EditSupportRequestCommentView,
                          DeleteSupportRequestCommentView, RequestMeetupLocationView,
                          NewMeetupLocationRequestsListView, ViewMeetupLocationRequestView,
                          RejectMeetupLocationRequestView, ApproveRequestMeetupLocationView,
                          RequestMeetupView, NewMeetupRequestsListView, ViewMeetupRequestView,
                          ApproveRequestMeetupView, RejectMeetupRequestView,
                          CancelMeetupLocationJoinRequestView)


urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/about/$', MeetupLocationAboutView.as_view(),
        name='about_meetup_location'),
    url(r'^(?P<slug>[\w-]+)/upcoming/$', UpcomingMeetupsView.as_view(),
        name='upcoming_meetups'),
    url(r'^(?P<slug>[\w-]+)/past/$', PastMeetupListView.as_view(),
        name='past_meetups'),
    url(r'^(?P<slug>[\w-]+)/members/$', MeetupLocationMembersView.as_view(),
        name='members_meetup_location'),
    url(r'^(?P<slug>[\w-]+)/add/$', AddMeetupView.as_view(), name='add_meetup'),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/delete/$', DeleteMeetupView.as_view(),
        name='delete_meetup'),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/edit/$', EditMeetupView.as_view(),
        name="edit_meetup"),
    url(r'^(?P<slug>[\w-]+)/approve-location-request/$', ApproveRequestMeetupLocationView.as_view(),
        name='approve_meetup_location_request'),
    url(r'^(?P<slug>[\w-]+)/view-request/$', ViewMeetupLocationRequestView.as_view(),
        name='view_meetup_location_request'),
    url(r'view-requests/$', NewMeetupLocationRequestsListView.as_view(),
        name='new_meetup_location_requests'),
    url(r'^(?P<slug>[\w-]+)/reject-request/$', RejectMeetupLocationRequestView.as_view(),
        name='reject_meetup_location_request'),
    url(r'^(?P<slug>[\w-]+)/request/$', RequestMeetupView.as_view(),
        name="request_meetup"),
    url(r'^(?P<slug>[\w-]+)/view_meetup_requests/$', NewMeetupRequestsListView.as_view(),
        name="new_meetup_requests"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/view_meetup_requests/$',
        ViewMeetupRequestView.as_view(), name="view_meetup_request"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/approve_meetup_request/$',
        ApproveRequestMeetupView.as_view(), name="approve_meetup_request"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/reject_meetup_request/$',
        RejectMeetupRequestView.as_view(), name="reject_meetup_request"),
    url(r'locations/$', MeetupLocationList.as_view(), name='list_meetup_location'),
    url(r'^(?P<slug>[\w-]+)/sponsors/$', MeetupLocationSponsorsView.as_view(),
        name='sponsors_meetup_location'),
    url(r'^(?P<slug>[\w-]+)/remove/(?P<username>[\w.@+-]+)/$',
        RemoveMeetupLocationMemberView.as_view(),
        name='remove_member_meetup_location'),
    url(r'^(?P<slug>[\w-]+)/add_member/$', AddMeetupLocationMemberView.as_view(),
        name='add_member_meetup_location'),
    url(r'^(?P<slug>[\w-]+)/remove_organizer/(?P<username>[\w.@+-]+)/$',
        RemoveMeetupLocationOrganizerView.as_view(),
        name='remove_organizer_meetup_location'),
    url(r'^(?P<slug>[\w-]+)/make_organizer/(?P<username>[\w.@+-]+)/$',
        MakeMeetupLocationOrganizerView.as_view(),
        name='make_organizer_meetup_location'),
    url(r'^(?P<slug>[\w-]+)/join/(?P<username>[\w.@+-]+)/$', JoinMeetupLocationView.as_view(),
        name='join_meetup_location'),
    url(r'^(?P<slug>[\w-]+)/cancel/(?P<username>[\w.@+-]+)/$',
        CancelMeetupLocationJoinRequestView.as_view(),
        name='cancel_meetup_location_join_request'),
    url(r'^(?P<slug>[\w-]+)/join_requests/$', MeetupLocationJoinRequestsView.as_view(),
        name='join_requests_meetup_location'),
    url(r'^(?P<slug>[\w-]+)/join_requests/approve/(?P<username>[\w.@+-]+)/$',
        ApproveMeetupLocationJoinRequestView.as_view(),
        name='approve_join_request_meetup_location'),
    url(r'^(?P<slug>[\w-]+)/join_requests/reject/(?P<username>[\w.@+-]+)/$',
        RejectMeetupLocationJoinRequestView.as_view(),
        name='reject_join_request_meetup_location'),
    url(r'add/$', AddMeetupLocationView.as_view(), name="add_meetup_location"),
    url(r'request-meetuplocation/$', RequestMeetupLocationView.as_view(),
        name="request_meetup_location"),
    url(r'^(?P<slug>[\w-]+)/edit/$', EditMeetupLocationView.as_view(), name="edit_meetup_location"),
    url(r'^(?P<slug>[\w-]+)/delete/$', DeleteMeetupLocationView.as_view(),
        name='delete_meetup_location'),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/add_comment/$', AddMeetupCommentView.as_view(),
        name="add_meetup_comment"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/edit_comment/(?P<comment_pk>\d+)/$',
        EditMeetupCommentView.as_view(),
        name="edit_meetup_comment"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/delete_comment/(?P<comment_pk>\d+)/$',
        DeleteMeetupCommentView.as_view(),
        name="delete_meetup_comment"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/rsvp/$', RsvpMeetupView.as_view(),
        name="rsvp_meetup"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/going/$', RsvpGoingView.as_view(),
        name="rsvp_going"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/add_support_request/$',
        AddSupportRequestView.as_view(),
        name='add_support_request'),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/edit_support_request/(?P<pk>\d+)/$',
        EditSupportRequestView.as_view(),
        name="edit_support_request"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/delete_support_request/(?P<pk>\d+)/$',
        DeleteSupportRequestView.as_view(),
        name='delete_support_request'),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/support_request/(?P<pk>\d+)/$',
        SupportRequestView.as_view(),
        name="view_support_request"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/support_requests_list/$',
        SupportRequestsListView.as_view(),
        name="list_support_requests"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/unapproved_support_requests/$',
        UnapprovedSupportRequestsListView.as_view(),
        name="unapproved_support_requests"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/support_request/approve/(?P<pk>\d+)/$',
        ApproveSupportRequestView.as_view(),
        name='approve_support_request'),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/support_request/reject/(?P<pk>\d+)/$',
        RejectSupportRequestView.as_view(),
        name='reject_support_request'),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/support_request/(?P<pk>\d+)/add_comment/$',
        AddSupportRequestCommentView.as_view(),
        name="add_support_request_comment"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/support_request/(?P<pk>\d+)/edit_comment/'
        '(?P<comment_pk>\d+)/$',
        EditSupportRequestCommentView.as_view(),
        name="edit_support_request_comment"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/support_request/(?P<pk>\d+)/delete_comment/'
        '(?P<comment_pk>\d+)/$',
        DeleteSupportRequestCommentView.as_view(),
        name="delete_support_request_comment"),
    url(r'^(?P<slug>[\w-]+)/(?P<meetup_slug>[\w-]+)/$', MeetupView.as_view(), name="view_meetup"),
]
