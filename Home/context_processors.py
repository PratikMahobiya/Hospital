from django.contrib.auth.models import Group

def menu_processor(request):
    menu = {}
    user = request.user
    print("context_p:- ",user)#for testing purpose
    if str(user) == "doctor":
        menu['Appointments'] = '/appointments'
        menu['Cases'] = '/case'
    elif str(user) == "patient":
        menu['Reports'] = '/reports'
        menu['Appointments'] = '/appointments'
        menu['Medication'] = '/bill/medicines'
        menu['Bills'] = '/bill'
        menu['Cases'] = '/case'
    # elif hasGroup(user, 'receptionist'):
    #     menu['New Patient'] = '/profile/register'
    #     menu['Manage Appointments'] = '/appointments'
    #     menu['New Appointment'] = '/appointments/book'
    #     menu['Bills'] = '/bill'
    #     menu['Cases'] = '/case'
    #     menu['Generate Case'] = '/case/generate'
    # elif hasGroup(user, 'lab_attendant'):
    #     menu['Reports'] = '/reports'
    #     menu['Generate Report'] = '/reports/generate'
    # elif hasGroup(user, 'inventory_manager'):
    #     menu['All Stock'] = ''
    #     menu['Stock Details'] = ''
    print("CONT-dict:- ",menu)
    return {'menu': menu}
