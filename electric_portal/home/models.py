from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
import bidi.algorithm

# Create your models here.

class UserTable(models.Model):
    main_user       = models.ForeignKey(User,on_delete=models.CASCADE)
    consultant_name = models.CharField(max_length=50)
    job_number      = models.CharField(max_length=50)
    phone           = models.CharField(max_length=13)
    user_role       = models.CharField(max_length=10)

    def __str__(self):
        return self.consultant_name

class Assay(models.Model):
    order_type          = models.BooleanField(default=True)
    assay_num           = models.CharField(max_length=50)
    mission_num         = models.CharField(max_length=50)
    permit_type         = models.CharField(max_length=50)
    contractor_name     = models.CharField(max_length=50)
    station             = models.CharField(max_length=50)
    neighborhood        = models.CharField(max_length=50)
    depth_of_excavation = models.CharField(max_length=50)
    fossil_view         = models.CharField(max_length=50)
    cable_length        = models.CharField(max_length=50)
    date                = models.CharField(max_length=20)
    user                = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    year                = models.CharField(max_length=5)
    month               = models.CharField(max_length=5)
    day                 = models.CharField(max_length=5)

    def __str__(self):
        return self.assay_num


def create_image(size, bgColor, message, font, fontColor):
    W, H = size
    image = Image.new('RGB', size, bgColor)
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)-20, 20), message, font=font, fill=fontColor)
    return image

def create_image2(size, bgColor, message, font, fontColor,parent):
    W, H = size
    draw = ImageDraw.Draw(parent)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)-20, (H-h)-20), message, font=font, fill=fontColor)

def create_image3(size, bgColor, message, font, fontColor,parent):
    W, H = size
    draw = ImageDraw.Draw(parent)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)-20, (H-h)-50), message, font=font, fill=fontColor)

def create_image4(size, bgColor, message, font, fontColor,parent):
    W, H = size
    draw = ImageDraw.Draw(parent)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)-20, (H-h)-80), message, font=font, fill=fontColor)

class Permit(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    permit_img = models.ImageField(default='img/unknown.png' , upload_to="permits")

    def updateImage(self, *args, **kwargs):
        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("التصاريح")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.permit_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class TeamModel(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    team_model_img = models.ImageField(default='img/unknown.png' , upload_to="team_model")
    
    def updateImage(self, *args, **kwargs):
        super(TeamModel, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("نموذج فريق العمل")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.team_model_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class PreworkMeeting(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    prework_meeting = models.ImageField(default='img/unknown.png' , upload_to="prework_meeting")
    
    def updateImage(self, *args, **kwargs):
        super(PreworkMeeting, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("إجتماع ما قبل العمل")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.prework_meeting.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class RiskAssessment(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    risk_assessment_img = models.ImageField(default='img/unknown.png' , upload_to="risk_assessment")
    
    def updateImage(self, *args, **kwargs):
        super(RiskAssessment, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("تقييم المخاطر")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.risk_assessment_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)


class SafeWorkProcedure(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    safe_work_procedures_img = models.ImageField(default='img/unknown.png' , upload_to="safe_work_procedures")
    
    def updateImage(self, *args, **kwargs):
        super(SafeWorkProcedure, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("إجراءات العمل الآمن")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.safe_work_procedures_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class Paramedic(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    paramedic_img = models.ImageField(default='img/unknown.png' , upload_to="paramedic")
    
    def updateImage(self, *args, **kwargs):
        super(Paramedic, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("المسعف")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.paramedic_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class Fighter(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    fighter = models.ImageField(default='img/unknown.png' , upload_to="fighter")
    
    def updateImage(self, *args, **kwargs):
        super(Fighter, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("المكافح")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.fighter.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class AssignedTask(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    assigned_task_img = models.ImageField(default='img/unknown.png' , upload_to="assigned_task")
    
    def updateImage(self, *args, **kwargs):
        super(AssignedTask, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("المهمة المسندة")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.assigned_task_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class ArtificialSecurityCard(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    artificial_security_card_img = models.ImageField(default='img/unknown.png' , upload_to="artificial_security_card")
    
    def updateImage(self, *args, **kwargs):
        super(ArtificialSecurityCard, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("بطاقة الأمن الإصطناعي")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.artificial_security_card_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class RecipientCard(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    recipient_card_img = models.ImageField(default='img/unknown.png' , upload_to="recipient_card")
    
    def updateImage(self, *args, **kwargs):
        super(RecipientCard, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("بطاقة المستلم")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.recipient_card_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class SourceCard(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    source_card_img = models.ImageField(default='img/unknown.png' , upload_to="source_card")
    
    def updateImage(self, *args, **kwargs):
        super(SourceCard, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("بطاقة المصدر")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.source_card_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class TUVForEquipmentAndDriver(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    TUV_for_equipment_and_driver_img  = models.ImageField(default='img/unknown.png' , upload_to="TUV_for_equipment_and_driver")
    
    def updateImage(self, *args, **kwargs):
        super(TUVForEquipmentAndDriver, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("للمعدات والسائق TUV")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.TUV_for_equipment_and_driver_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class FireExtinguisher(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    fire_extinguisher_img = models.ImageField(default='img/unknown.png' , upload_to="fire_extinguisher")
    
    def updateImage(self, *args, **kwargs):
        super(FireExtinguisher, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("طفاية الحريق")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.fire_extinguisher_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class FirstAid(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    first_aid_img = models.ImageField(default='img/unknown.png' , upload_to="first_aid")
    
    def updateImage(self, *args, **kwargs):
        super(FirstAid, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("الإسعافات الأولية")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.first_aid_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class WorkTeam(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    work_team_img = models.ImageField(default='img/unknown.png' , upload_to="work_team")
    
    def updateImage(self, *args, **kwargs):
        super(WorkTeam, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("فريق العمل")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.work_team_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class PicturesOfSite(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    pictures_of_site_img = models.ImageField(default='img/unknown.png' , upload_to="pictures_of_site")
    
    def updateImage(self, *args, **kwargs):
        super(PicturesOfSite, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("صور للموقع")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.pictures_of_site_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class SubscriptionNumber(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    subscription_number_img = models.ImageField(default='img/unknown.png' , upload_to="subscription_number")
    
    def updateImage(self, *args, **kwargs):
        super(SubscriptionNumber, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("رقم الإشتراك")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.subscription_number_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class CutterCapacity(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    cutter_capacity_img = models.ImageField(default='img/unknown.png' , upload_to="cutter_capacity")
    
    def updateImage(self, *args, **kwargs):
        super(CutterCapacity, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("سعة القاطع")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.cutter_capacity_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class Counter(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    counter_img = models.ImageField(default='img/unknown.png' , upload_to="counter")
    
    def updateImage(self, *args, **kwargs):
        super(Counter, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("العداد")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.counter_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class MissionLock(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    mission_lock_img = models.ImageField(default='img/unknown.png' , upload_to="mission_lock")
    
    def updateImage(self, *args, **kwargs):
        super(MissionLock, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("اقفال المهمة")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.mission_lock_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class SafetyBarrier(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    safety_barriers_img = models.ImageField(default='img/unknown.png' , upload_to="safety_barriers")
    
    def updateImage(self, *args, **kwargs):
        super(SafetyBarrier, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("الحواجز")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.safety_barriers_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class Object(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    object_img = models.ImageField(default='img/unknown.png' , upload_to="objects")
    
    def updateImage(self, *args, **kwargs):
        super(Object, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("النماذج")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.object_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class Obstacle(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    obstacles_img = models.ImageField(default='img/unknown.png' , upload_to="obstacles")
    
    def updateImage(self, *args, **kwargs):
        super(Obstacle, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("العوائق")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.obstacles_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)

class Violation(models.Model):
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE)
    violations_img = models.ImageField(default='img/unknown.png' , upload_to="violations")
    
    def updateImage(self, *args, **kwargs):
        super(Violation, self).save(*args, **kwargs)

        reshaped_text = arabic_reshaper.reshape(self.assay.user.consultant_name)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        reshaped_text2 = arabic_reshaper.reshape(self.assay.neighborhood)
        bidi_text2 = bidi.algorithm.get_display(reshaped_text2)
        reshaped_text3 = arabic_reshaper.reshape(self.assay.date)
        bidi_text3 = bidi.algorithm.get_display(reshaped_text3)
        reshaped_text4 = arabic_reshaper.reshape("المخالفات")
        bidi_text4 = bidi.algorithm.get_display(reshaped_text4)
        apath = self.violations_img.path
        limg = Image.open(apath)
        limg.thumbnail((400,1000))
        try:limg2 = Image.open('/home/assays/electricPortalWeb/electric_portal/static/img/logo.png')
        except:limg2 = Image.open('./static/img/logo.png')
        limg2.thumbnail((150,100))

        myFont = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 35)
        myFont2 = ImageFont.truetype('/home/assays/electricPortalWeb/electric_portal/static/fonts/arial.ttf', 17)
        myMessage = bidi_text
        myMessage2 = bidi_text2
        myMessage3 = bidi_text3
        myMessage4 = bidi_text4
        myImage = create_image((400, 800), 'white', myMessage, myFont, 'black')
        text = create_image2((400, 800), 'white', myMessage2, myFont2, 'black',myImage)
        text3 = create_image3((400, 800), 'white', myMessage3, myFont2, 'black',myImage)
        text4 = create_image4((400, 800), 'white', myMessage4, myFont2, 'black',myImage)
        myImage.paste(limg,(0,80))
        myImage.paste(limg2,(0,650))

        myImage.save(apath)