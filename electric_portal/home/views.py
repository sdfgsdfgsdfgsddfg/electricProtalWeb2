from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from datetime import *
from django.contrib.auth import logout as logout_auth
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    context = {'lang':"ar"}
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        ierr = ""
        errtitle = ""
        a = "work"
        jobNumFilter = UserTable.objects.filter(job_number=request.POST['jobNum'])
        if len(jobNumFilter) == 0:
            a = "no"
            ierr = "snack"
            errtitle = "الرقم الوظيفي غير صحيح"
        else:
            jobNumGet = UserTable.objects.get(job_number=request.POST['jobNum'])
        if a == "work":
            user = User.objects.get(pk = jobNumGet.main_user.pk)
            user = authenticate(username = user.username,password = request.POST["password"])
            if user is None:
                a = "no"
                ierr = "snack"
                errtitle = "كلمة المرور غير صحيحة"
        if a == "work":
            auth.login(request,user)
        return JsonResponse({'ierr':ierr,'errtitle':errtitle})
    return render(request, 'login.html', context)

def validateImageName(name):
    nums = "1234567890"
    for n in nums:
        name = name.replace(n,"")
    return name

def logout(request):
    logout_auth(request)
    return redirect("/")

def consultants(request):
    context = {'lang':"ar"}
    if not request.user.is_authenticated:
        return redirect("/login")
    else:
        user = User.objects.get(pk=request.user.pk)
        userTable = UserTable.objects.get(main_user=user)
        context['user'] = userTable
    if request.method == "POST":
        'consultantName', 'jobNum', 'phoneNumber', 'password'
        ierr = ""
        errtitle = ""
        a = "work"
        if a == "work":
            nameFilter = UserTable.objects.filter(consultant_name=request.POST["consultantName"])
            if len(nameFilter) != 0:
                a = "no"
                ierr = "snack"
                errtitle = "اسم الإستشاري مستخدَم في حساب آخر"
        if a == "work":
            jobFilter = UserTable.objects.filter(job_number=request.POST["jobNum"])
            if len(jobFilter) != 0:
                a = "no"
                ierr = "snack"
                errtitle = "الرقم الوظيفي مستخدَم في حساب آخر"
        if a == "work":
            phFilter = UserTable.objects.filter(phone=request.POST["phoneNumber"])
            if len(phFilter) != 0:
                a = "no"
                ierr = "snack"
                errtitle = "رقم الهاتف مُستخدم في حساب آخر"
        if a == "work":
            userCreate = User.objects.create_user(
                username = request.POST["consultantName"],
                password = request.POST["password"],
            )
            userCreate.save()
            userTableCreate = UserTable.objects.create(
                main_user = userCreate,
                consultant_name = request.POST["consultantName"],
                job_number = request.POST["jobNum"],
                phone = request.POST["phoneNumber"],
                user_role = "consultant",
            )
            userTableCreate.save()
        return JsonResponse({"ierr":ierr,"errtitle":errtitle})
    else:
        data = []
        usersFilter = UserTable.objects.all()
        for u in usersFilter:
            data.append([u.consultant_name,u.user_role])
        context['data'] = data
        if "getData" in request.GET:
            return JsonResponse({"data":data})
    return render(request, 'consultants.html', context)

def home(request):
    context = {'lang':"ar"}
    if not request.user.is_authenticated:
        return redirect("/login")
    else:
        user = User.objects.get(pk=request.user.pk)
        userTable = UserTable.objects.get(main_user=user)
        context['user'] = userTable
    if request.method == "POST":
        assayFilter = Assay.objects.filter(assay_num = request.POST["assayNum"])
        if len(assayFilter) != 0:
            return JsonResponse({"ierr":"y"})
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        year = now.year
        month = now.month
        day = now.day
        dateF = f'{hour}:{minute} {year}/{month}/{day}'
        if request.POST["checkType"] == "new":
            order_type = True
        else:
            order_type = False
        createAssay = Assay.objects.create(
            order_type = order_type,
            assay_num = request.POST["assayNum"],
            mission_num = request.POST["missionNum"],
            permit_type = request.POST["permitType"],
            contractor_name = request.POST["contractorName"],
            station = request.POST["station"],
            neighborhood = request.POST["neighborhood"],
            depth_of_excavation = request.POST["depthOfExcavation"],
            fossil_view = request.POST["fossilView"],
            cable_length = request.POST["cableLength"],
            date = dateF,
            user = userTable,
            month = month,
            year = year,
            day = day,
        )
        createAssay.save()
        for f in request.FILES:
            img_type = validateImageName(f)
            if img_type == "permit":
                createData = Permit.objects.create(
                    assay = createAssay,
                    permit_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "teamModel":
                createData = TeamModel.objects.create(
                    assay = createAssay,
                    team_model_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "preWorkMeeting":
                createData = PreworkMeeting.objects.create(
                    assay = createAssay,
                    prework_meeting = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "riskAssessment":
                createData = RiskAssessment.objects.create(
                    assay = createAssay,
                    risk_assessment_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "safeWorkProcedure":
                createData = SafeWorkProcedure.objects.create(
                    assay = createAssay,
                    safe_work_procedures_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "paramedic":
                createData = Paramedic.objects.create(
                    assay = createAssay,
                    paramedic_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "fighter":
                createData = Fighter.objects.create(
                    assay = createAssay,
                    fighter = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "assignedTask":
                createData = AssignedTask.objects.create(
                    assay = createAssay,
                    assigned_task_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "artificialSecurityCard":
                createData = ArtificialSecurityCard.objects.create(
                    assay = createAssay,
                    artificial_security_card_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "recipientCard":
                createData = RecipientCard.objects.create(
                    assay = createAssay,
                    recipient_card_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "sourceCard":
                createData = SourceCard.objects.create(
                    assay = createAssay,
                    source_card_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "tuvForEquipmentAndDriver":
                createData = TUVForEquipmentAndDriver.objects.create(
                    assay = createAssay,
                    TUV_for_equipment_and_driver_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "fireExtinguisher":
                createData = FireExtinguisher.objects.create(
                    assay = createAssay,
                    fire_extinguisher_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "firstAid":
                createData = FirstAid.objects.create(
                    assay = createAssay,
                    first_aid_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "workTeam":
                createData = WorkTeam.objects.create(
                    assay = createAssay,
                    work_team_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "picturesOfSite":
                createData = PicturesOfSite.objects.create(
                    assay = createAssay,
                    pictures_of_site_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "subscriptionNumber":
                createData = SubscriptionNumber.objects.create(
                    assay = createAssay,
                    subscription_number_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "cutterCapacity":
                createData = CutterCapacity.objects.create(
                    assay = createAssay,
                    cutter_capacity_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "counter":
                createData = Counter.objects.create(
                    assay = createAssay,
                    counter_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "missionLock":
                createData = MissionLock.objects.create(
                    assay = createAssay,
                    mission_lock_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "safetyBarrier":
                createData = SafetyBarrier.objects.create(
                    assay = createAssay,
                    safety_barriers_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "object":
                createData = Object.objects.create(
                    assay = createAssay,
                    object_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "obstacle":
                createData = Obstacle.objects.create(
                    assay = createAssay,
                    obstacles_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
            elif img_type == "violation":
                createData = Violation.objects.create(
                    assay = createAssay,
                    violations_img = request.FILES[f],
                )
                createData.save()
                createData.updateImage()
        return JsonResponse({"ierr":"y"})
    else:
        data = []
        dataFilter = Assay.objects.all()
        months = [1,2,3,4,5,6,7,8,9,10,11,12]
        for m in months:
            dataFilter = Assay.objects.filter(month=m)
            if m == 1:monthName = "يناير"
            if m == 2:monthName = "فبراير"
            if m == 3:monthName = "مارس"
            if m == 4:monthName = "إبريل"
            if m == 5:monthName = "مايو"
            if m == 6:monthName = "يونيو"
            if m == 7:monthName = "يوليو"
            if m == 8:monthName = "أغسطس"
            if m == 9:monthName = "سبتمبر"
            if m == 10:monthName = "أكتوبر"
            if m == 11:monthName = "نوفمبر"
            if m == 12:monthName = "ديسمبر"
            values = []
            for d in dataFilter:
                now = datetime(int(d.year),int(d.month),int(d.day))
                if now.strftime('%A') == 'Sunday':dayName = "الأحد"
                if now.strftime('%A') == 'Monday':dayName = "الإثنين"
                if now.strftime('%A') == 'Tuesday':dayName = "الثلاثاء"
                if now.strftime('%A') == 'Wednesday':dayName = "الأربعاء"
                if now.strftime('%A') == 'Thursday':dayName = "الخميس"
                if now.strftime('%A') == 'Friday':dayName = "الجمعة"
                if now.strftime('%A') == 'Saturday':dayName = "السبت"
                values.append([d.assay_num,d.user.consultant_name,f'{d.day} {dayName}'])
            if len(values) != 0:
                data.append([monthName,values])
        data = data[::-1]
        if "getData" in request.GET:
            return JsonResponse({"data":data})
        elif "search" in request.GET:
            data = []
            assayFilter = Assay.objects.filter(assay_num__icontains=request.GET["search"])
            for a in assayFilter:
                now = datetime(int(a.year),int(a.month),int(a.day))
                if now.strftime('%A') == 'Sunday':dayName = "الأحد"
                if now.strftime('%A') == 'Monday':dayName = "الإثنين"
                if now.strftime('%A') == 'Tuesday':dayName = "الثلاثاء"
                if now.strftime('%A') == 'Wednesday':dayName = "الأربعاء"
                if now.strftime('%A') == 'Thursday':dayName = "الخميس"
                if now.strftime('%A') == 'Friday':dayName = "الجمعة"
                if now.strftime('%A') == 'Saturday':dayName = "السبت"
                data.append([a.assay_num,a.user.consultant_name,f'{a.day} {dayName}'])
            return JsonResponse({"data":data})
        elif "getAssayData" in request.GET:
            data = []
            assayGet = Assay.objects.get(assay_num=request.GET["getAssayData"])
            if assayGet.order_type == True:
                order_type = "جديد"
            else:
                order_type = "مؤقت"
            data.append(order_type)
            data.append(assayGet.mission_num)
            data.append(assayGet.permit_type)
            data.append(assayGet.contractor_name)
            data.append(assayGet.station)
            data.append(assayGet.neighborhood)
            data.append(assayGet.depth_of_excavation)
            data.append(assayGet.fossil_view)
            data.append(assayGet.cable_length)

            images = []
            imageGet = Permit.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.permit_img.url)
            imageGet = TeamModel.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.team_model_img.url)
            imageGet = PreworkMeeting.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.prework_meeting.url)
            imageGet = RiskAssessment.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.risk_assessment_img.url)
            imageGet = SafeWorkProcedure.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.safe_work_procedures_img.url)
            imageGet = Paramedic.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.paramedic_img.url)
            imageGet = Fighter.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.fighter.url)
            imageGet = AssignedTask.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.assigned_task_img.url)
            imageGet = ArtificialSecurityCard.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.artificial_security_card_img.url)
            imageGet = RecipientCard.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.recipient_card_img.url)
            imageGet = SourceCard.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.source_card_img.url)
            imageGet = TUVForEquipmentAndDriver.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.TUV_for_equipment_and_driver_img.url)
            imageGet = FireExtinguisher.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.fire_extinguisher_img.url)
            imageGet = FirstAid.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.first_aid_img.url)
            imageGet = WorkTeam.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.work_team_img.url)
            imageGet = PicturesOfSite.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.pictures_of_site_img.url)
            imageGet = SubscriptionNumber.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.subscription_number_img.url)
            imageGet = CutterCapacity.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.cutter_capacity_img.url)
            imageGet = Counter.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.counter_img.url)
            imageGet = MissionLock.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.mission_lock_img.url)
            imageGet = SafetyBarrier.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.safety_barriers_img.url)
            imageGet = Object.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.object_img.url)
            imageGet = Obstacle.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.obstacles_img.url)
            imageGet = Violation.objects.filter(assay=assayGet)
            for img in imageGet:
                images.append(img.violations_img.url)
            data.append(images)
            data.append(assayGet.assay_num)
            return JsonResponse({"data":data})
        context['data']=data

    return render(request, 'home.html', context)