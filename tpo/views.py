from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
#from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.core.mail import send_mail, mail_admins
from django.contrib import messages
from chatmaster.p2p_chat import *
from MySQLdb import *

def Leave_Page(request):
    form = LeaveForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LeaveForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in request.POST.get as required
            # ...
            # redirect to a new URL
            leave_form = form.save()
            Name = leave_form.Name
            Email = leave_form.Email
            Phone = leave_form.Phone
            Subject = leave_form.Subject
            Message = leave_form.Message
            body = "\nCompany Name - " + str(Name) + "\nMessage - " + str(Message)
            send_mail(subject=Subject, message=body, fail_silently=False, from_email="rotikapdaaurmakan15@gmail.com",
                      recipient_list=['miramiranomi07@gmail.com'])
            messages.add_message(request, messages.INFO, 'Feedback Submitted')
            print "done"

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LeaveForm()

    return render(request, 'tpo/leavePage.html', {'form': form})


def Feedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in request.POST.get as required
            # ...
            # redirect to a new URL
            feedback_form = form.save()


    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedbackForm()

    return render(request, 'tpo/feedback.html', {'form': form})


def Contact_Us(request):
    return render(request, 'tpo/ContactUs.html')


def Calender(request):
    return render(request, 'tpo/Calender.html')


def Home(request):
    return render(request, 'tpo/home.html')


def Varanasi(request):
    return render(request, 'tpo/varanasi.html')


def Why(request):
    return render(request, 'tpo/why.html')


def Procedure_And_Policy(request):
    return render(request, 'tpo/Procedure&Policy.html')


def Disciplines(request):
    return render(request, 'tpo/disciplines.html')


def Overview(request):
    return render(request, 'tpo/overview.html')


def Beyond(request):
    return render(request, 'tpo/Beyond.html')


def Tpomessage(request):
    return render(request, 'tpo/tpomessage.html')

def Facilities(request):
    return render(request, 'tpo/facilities.html')

def Directormsg(request):
    return render(request, 'tpo/Directormsg.html')

def Tpomsg(request):
    return render(request, 'tpo/tpomsg.html')




def Prevrec(request):
    db = connect('localhost',"root","cse7005061XYZ","tpo")
    c = db.cursor()
    sql = '''SELECT * FROM tpo_prevrec;'''
    try:
        c.execute(sql)
        data = c.fetchall()
        data2 = [];
        for x in data:
            l = len(x)
            data2.append(x[0])
        return render(request,'tpo/prevrec.html',{'x':data2})
    except:
        return render(request, 'tpo/prevrec.html')


@csrf_protect
def Register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            #profile = profile_form.save(commit=False)
            #profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            #if 'picture' in request.FILES:
             #   profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            #profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors#, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        #profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'tpo/register.html',
            {'user_form': user_form, 'registered': registered})


def Login(request):
    if request.user.id:
        logout(request)
        return render(request, 'tpo/home.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'tpo/home.html')
        return HttpResponse('User NOt found')

    form = LoginForm()
    return render(request, 'tpo/login.html',{'user':'dsf','form':form})


def Logout(request):
    logout(request)
    render_to_response(request, 'tpo/home.html')


def Policy_pdf(request):
    return FileResponse(open("tpo/static/Downloads/Placement_Policy_2016_17.pdf", 'rb'), content_type='application/pdf')


def Zip(request):
    return FileResponse(open("tpo/static/Downloads/IIT(BHU)_JNF_INF.zip", 'rb'), content_type='application/zip')





def CompanyResponseSheet(request):
    context = {}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        if True:
            Name_Of_the_Company = request.POST.get('Name_Of_the_Company')


            #f.Name_Of_the_Company = Name_Of_the_Company
            Address = request.POST.get('Address')
            #f.Address = Address
            Type = request.POST.get('Type')
            #f.Type = Type
            Indstry_sctr_Core = request.POST.get('Indstry_sctr_Core')
            print Indstry_sctr_Core
            #f.Indstry_sctr_Core = Indstry_sctr_Core
            Indstry_sctr_consulting = request.POST.get('Indstry_sctr_consulting')
            #f.Indstry_sctr_consulting = Indstry_sctr_consulting
            Indstry_sctr_IT = request.POST.get('Indstry_sctr_IT')
            #f.some_field = Indstry_sctr_IT
            Indstry_sctr_Finanace = request.POST.get('Indstry_sctr_Finanace')
            #f.Indstry_sctr_Finanace = Indstry_sctr_Finanace
            Indstry_sctr_Govrnt = request.POST.get('Indstry_sctr_Govrnt')
            #f.Indstry_sctr_Govrnt = Indstry_sctr_Govrnt
            Indstry_sctr_Other = request.POST.get('Indstry_sctr_Other')
            #f.Indstry_sctr_Other = Indstry_sctr_Other
            req_functional_areas_Red = request.POST.get('req_functional_areas_Red')
            #f.req_functional_areas_Red = req_functional_areas_Red
            req_functional_areas_Maintenance = request.POST.get('req_functional_areas_Maintenance')
            #f.req_functional_areas_Maintenance = req_functional_areas_Maintenance
            req_functional_areas_Design = request.POST.get('req_functional_areas_Design')
            #f.req_functional_areas_Design = req_functional_areas_Design
            req_functional_areas_Production = request.POST.get('req_functional_areas_Production')
            #f.req_functional_areas_Production = req_functional_areas_Production
            req_functional_areas_RD = request.POST.get('req_functional_areas_RD')
            #f.req_functional_areas_RD = req_functional_areas_RD
            req_functional_areas_Others = request.POST.get('req_functional_areas_Others')
            #f.req_functional_areas_Others = req_functional_areas_Others
            req_functional_areas_Finance = request.POST.get('req_functional_areas_Finance')
            #f.req_functional_areas_Finance = req_functional_areas_Finance
            VsnandInterest = request.POST.get('VsnandInterest')
            #f.VsnandInterest = VsnandInterest
            PrsnName = request.POST.get('PrsnName')
            #f.PrsnName = PrsnName
            PrsnDesignation = request.POST.get('PrsnDesignation')
            #f.PrsnDesignation = PrsnDesignation
            PrsnPhone = request.POST.get('PrsnPhone')
            #f.PrsnPhone = PrsnPhone
            PrsnEmail = request.POST.get('PrsnEmail')
            #f.PrsnEmail = PrsnEmail
            CGPA = request.POST.get('CGPA')
            #f.CGPA = CGPA
            XII_perc = request.POST.get('XII_perc ')
            #f.XII_perc  = XII_perc
            X_perc = request.POST.get('X_perc')
            #f.X_perc = X_perc
            SpecialisationPG = request.POST.get('SpecialisationPG')
            #f.SpecialisationPG = SpecialisationPG
            Age_limits = request.POST.get('Age_limits')
            #f.Age_limits = Age_limits
            Test_Written = request.POST.get('Test_Written')
            #f.Test_Written = Test_Written
            Test_Aptitude = request.POST.get('Test_Aptitude')
            #f.Test_Aptitude = Test_Aptitude
            Test_Online = request.POST.get('Test_Online')
            #f.Test_Online = Test_Online
            Test_Technical = request.POST.get('Test_Technical')
            #f.Test_Technical = Test_Technical
            Test_Others = request.POST.get('Test_Others')
            #f.Test_Others = Test_Others
            GD = request.POST.get('GD')
            #f.GD =GD
            PITechnical = request.POST.get('PITechnical')
            #f.PITechnical = PITechnical
            PIHR = request.POST.get('PIHR')
            #f.PIHR = PIHR
            PIOthers = request.POST.get('PIOthers')
            #f.PIOthers = PIOthers
            ServiceAgreement = request.POST.get('ServiceAgreement')
            #f.ServiceAgreement = ServiceAgreement
            TrainingPeriod = request.POST.get('TrainingPeriod')
            #f.TrainingPeriod = TrainingPeriod
            AllStreamsBtech = request.POST.get('AllStreamsBtech')
            #f.AllStreamsBtech = AllStreamsBtech
            AllStreamsIDD = request.POST.get(' AllStreamsIDD')
            #f. AllStreamsIDD =  AllStreamsIDD
            AllStreamsMTech = request.POST.get('AllStreamsMTech')
            #f.AllStreamsMTech = AllStreamsMTech
            AllStreamsIMD = request.POST.get('AllStreamsIMD')
            #f.AllStreamsIMD = AllStreamsIMD
            CeraBtech = request.POST.get('CeraBtech')
            #f.CeraBtech = CeraBtech
            CeraMTech = request.POST.get('CeraMTech')
            #f.CeraMTech = CeraMTech
            CeraIDD = request.POST.get('CeraIDD')
            #f.CeraIDD = CeraIDD
            ChemBTech = request.POST.get('ChemBTech')
            #f.ChemBTech = ChemBTech
            ChemMTech = request.POST.get('ChemMTech')
            #f.ChemMTech = ChemMTech
            CivilBtech = request.POST.get('CivilBtech')
            #f.CivilBtech = CivilBtech
            CivilIDD = request.POST.get('CivilIDD')
            #f.CivilIDD = CivilIDD
            CivilMtech = request.POST.get('CivilMtech')
            #f.CivilMtech = CivilMtech
            ComputerBtech = request.POST.get('ComputerBtech')
            #f.ComputerBtech = ComputerBtech
            ComputerIDD = request.POST.get('ComputerIDD')
            #f.ComputerIDD = ComputerIDD
            TricalBtech = request.POST.get('TricalBtech')
            #f.TricalBtech = TricalBtech
            TricalMTech = request.POST.get('TricalMTech')
            #f.TricalMTech = TricalMTech
            TricalIDD = request.POST.get('TricalIDD')
            #f.TricalIDD = TricalIDD
            TronicsBtech = request.POST.get('TronicsBtech')
            #f.TronicsBtech = TronicsBtech
            TronicsMTech = request.POST.get('TronicsMTech')
            #f.TronicsMTech = TronicsMTech
            TronicsIDD = request.POST.get('TronicsIDD')
            #f.TronicsIDD = TronicsIDD
            MechBtech = request.POST.get('MechBtech')
            #f.MechBtech = MechBtech
            MechMTech = request.POST.get('MechMTech')
            #f.MechMTech = MechMTech
            MechIDD = request.POST.get('MechIDD')
            #f.MechIDD = MechIDD
            MetaBtech = request.POST.get('MetaBtech')
            #f.MetaBtech = MetaBtech
            MetaMTech = request.POST.get('MetaMTech')
            #f.MetaMTech = MetaMTech
            MetaIDD = request.POST.get('MetaIDD')
            #f.MetaIDD = MetaIDD
            MinBtech = request.POST.get('MinBtech')
            #f.MinBtech = MinBtech
            MinMTech = request.POST.get('MinMTech')
            #f.MinMTech = MinMTech
            MinIDD = request.POST.get('MinIDD')
            #f.MinIDD = MinIDD
            BioChemMTech = request.POST.get('BioChemMTech')
            #f.BioChemMTech = BioChemMTech
            BioChemIDD = request.POST.get('BioChemIDD')
            #f.BioChemIDD = BioChemIDD
            BioMedMTech = request.POST.get('BioMedMTech')
            #f.BioMedMTech = BioMedMTech
            BioMedIDD = request.POST.get('BioMedIDD')
            #f.BioMedIDD = BioMedIDD
            MSTMTech = request.POST.get('MSTMTech')
            #f.MSTMTech = MSTMTech
            MSTIDD = request.POST.get('MSTIDD')
            #f.MSTIDD = MSTIDD
            PharmaBtech = request.POST.get('PharmaBtech')
            #f.PharmaBtech = PharmaBtech
            PharmaMTech = request.POST.get('PharmaMTech')
            #f.PharmaMTech = PharmaMTech
            PharmaIDD = request.POST.get('PharmaIDD')
            #f.PharmaIDD =PharmaIDD
            EngPhy = request.POST.get('EngPhy')
            #f.EngPhy = EngPhy
            MNC = request.POST.get('MNC ')
            #f.MNC = MNC
            InC = request.POST.get('InC')
            #f.InC = InC
            CTC = request.POST.get('CTC')
            #.CTC = CTC
            In_Hand = request.POST.get('In_Hand')
            #f.In_Hand = In_Hand
            '''context = [Name_Of_the_Company= Name_Of_the_Company,'Address': Address,'Type': Type,
                       'Indstry_sctr_Core': Indstry_sctr_Core,'Indstry_sctr_consulting': Indstry_sctr_consulting,
                       'Indstry_sctr_IT': Indstry_sctr_IT,
                       'Indstry_sctr_Finanace':Indstry_sctr_Finanace,'Indstry_sctr_Govrnt': Indstry_sctr_Govrnt,
                       'Indstry_sctr_Other':Indstry_sctr_Other,
                       'req_functional_areas_Red': req_functional_areas_Red,
                       'req_functional_areas_Maintenance': req_functional_areas_Maintenance,
                       'req_functional_areas_Design': req_functional_areas_Design,
                       'req_functional_areas_Production': req_functional_areas_Production,
                       'req_functional_areas_RD': req_functional_areas_RD,
                       'req_functional_areas_Others': req_functional_areas_Others,
                       'req_functional_areas_Finance': req_functional_areas_Finance, 'VsnandInterest': VsnandInterest,
                       'PrsnName': PrsnName,
                       'PrsnDesignation': PrsnDesignation, 'PrsnPhone': PrsnPhone, 'PrsnEmail': PrsnEmail,
                       'CGPA': CGPA, 'XII_perc': XII_perc, 'X_perc': X_perc,
                       'SpecialisationPG': SpecialisationPG, 'Age_limits': Age_limits, 'Test_Written': Test_Written,
                       'Test_Aptitude': Test_Aptitude, 'Test_Online': Test_Online, 'Test_Technical': Test_Technical,
                       'Test_Others': Test_Others, 'GD': GD, 'PITechnical': PITechnical,
                       'PIHR':PIHR,'PIOthers': PIOthers, 'ServiceAgreement': ServiceAgreement,
                       'TrainingPeriod': TrainingPeriod,
                       'AllStreamsBtech': AllStreamsBtech, ' AllStreamsIDD': AllStreamsIDD,
                       'AllStreamsMTech': AllStreamsMTech, 'AllStreamsIMD': AllStreamsIMD,'CeraBtech': CeraBtech,
                       'CeraMTech': CeraMTech,'CeraIDD': CeraIDD, 'ChemBTech': ChemBTech,
                       'ChemMTech': ChemMTech, 'CivilBtech': CivilBtech,'CivilIDD': CivilIDD,'CivilMtech': CivilMtech,
                       'ComputerBtech': ComputerBtech,'ComputerIDD': ComputerIDD,'TricalBtech': TricalBtech,
                        'TricalMTech': TricalMTech, 'TricalIDD': TricalIDD, 'TronicsBtech':'TronicsBtech',
                       'TronicsMTech':TronicsMTech, 'TronicsIDD': TronicsIDD, 'MechBtech': MechBtech, 'MechMTech': MechMTech,
                       'MechIDD': MechIDD, 'MetaBtech':MetaBtech, 'MetaMTech':MetaMTech, 'MetaIDD':MetaIDD,
                       'MinBtech': MinBtech, 'MinMTech': MinMTech, 'MinIDD': MinIDD,
                       'BioChemMTech':BioChemMTech, 'BioChemIDD':BioChemIDD, 'BioMedMTech':BioMedMTech,
                       'BioMedIDD':BioMedIDD, 'MSTMTech':MSTMTech, 'MSTIDD': MSTIDD, 'PharmaBtech': PharmaBtech,
                       'PharmaMTech': PharmaMTech, 'PharmaIDD': PharmaIDD, 'EngPhy': EngPhy,
                       'MNC': MNC, 'InC': InC, 'CTC': CTC, 'In_Hand': In_Hand}'''
            objects = CompanyProfile(
                Name_Of_the_Company=Name_Of_the_Company,
                Address= Address,
                Type= Type,
                Indstry_sctr_Core= Indstry_sctr_Core,
                Indstry_sctr_consulting= Indstry_sctr_consulting,
                Indstry_sctr_IT= Indstry_sctr_IT,
                Indstry_sctr_Finanace=Indstry_sctr_Finanace,
                Indstry_sctr_Govrnt= Indstry_sctr_Govrnt,
                Indstry_sctr_Other=Indstry_sctr_Other,
                req_functional_areas_Red=req_functional_areas_Red,
                req_functional_areas_Maintenance= req_functional_areas_Maintenance,
                req_functional_areas_Design= req_functional_areas_Design,
                req_functional_areas_RD =req_functional_areas_RD,
                req_functional_areas_Others= req_functional_areas_Others,
                req_functional_areas_Finance= req_functional_areas_Finance,
                VsnandInterest= VsnandInterest,
                PrsnName=PrsnName,
                PrsnDesignation=PrsnDesignation,
                PrsnPhone= PrsnPhone,
                PrsnEmail=PrsnEmail,
                CGPA=CGPA,
                XII_perc= XII_perc,
                X_perc=X_perc,
                SpecialisationPG=SpecialisationPG,
                Age_limits=Age_limits,
                Test_Written=Test_Written,
                Test_Aptitude=Test_Aptitude,
                Test_Online=Test_Online,
                Test_Technical=Test_Technical,
                Test_Others=Test_Others,
                GD=GD,
                PITechnical= PITechnical,
                PIHR=PIHR,
                PIOthers=PIOthers,
                ServiceAgreement=ServiceAgreement,
                TrainingPeriod=TrainingPeriod,
                AllStreamsBtech= AllStreamsBtech,
                AllStreamsIDD=AllStreamsIDD,
                AllStreamsMTech=AllStreamsMTech,
                AllStreamsIMD= AllStreamsIMD,
                CeraBtech=CeraBtech,
                CeraMTech=CeraMTech,
                CeraIDD=CeraIDD,
                ChemBTech=ChemBTech,
                ChemMTech=ChemMTech,
                CivilBtech=CivilBtech,
                CivilIDD=CivilIDD,
                CivilMtech=CivilMtech,
                ComputerBtech=ComputerBtech,
                ComputerIDD=ComputerIDD,
                TricalBtech=TricalBtech,
                TricalMTech=TricalMTech,
                TricalIDD=TricalIDD,
                TronicsBtech=TronicsBtech,
                TronicsMTech=TronicsMTech,
                TronicsIDD=TronicsIDD,
                MechBtech=MechBtech,
                MechMTech=MechMTech,
                MechIDD=MechIDD,
                MetaBtech=MetaBtech,
                MetaMTech=MetaMTech,
                MetaIDD=MetaIDD,
                MinBtech=MinBtech,
                MinMTech=MinMTech,
                MinIDD=MinIDD,
                BioChemMTech=BioChemMTech,
                BioChemIDD=BioChemIDD,
                BioMedMTech=BioMedMTech,
                BioMedIDD=BioMedIDD,
                MSTMTech=MSTMTech,
                MSTIDD=MSTIDD,
                PharmaBtech=PharmaBtech,
                PharmaMTech=PharmaMTech,
                PharmaIDD=PharmaIDD,
                EngPhy=EngPhy,
                MNC=MNC,
                InC=InC,
                CTC=CTC,
                In_Hand=In_Hand
            )
            objects.save()
    return render(request, 'tpo/companyResponseSheet.html')


def chat(request):
    root=tk.Tk()
    p2p_chat=P2pChat(master=root)
    p2p_chat.mainloop()


def start_chat(request):
    form = StartChat()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StartChat(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in request.POST.get as required
            # ...
            # redirect to a new URL
            chat_form = form.save()
            Name = chat_form.Name
            Email = chat_form.Email
            Subject = "Details"
            body = "\nCompany Name - " + str(Name) + "\nEmail- " + str(Email)
            send_mail(subject=Subject, message=body, fail_silently=False, from_email="rotikapdaaurmakan15@gmail.com",
                      recipient_list=['miramiranomi07@gmail.com'])
            messages.add_message(request, messages.INFO, 'Feedback Submitted')
            print "done"


    # if a GET (or any other method) we'll create a blank form
    else:
        form = StartChat()

    return render(request, 'tpo/startchat.html', {'form': form})

