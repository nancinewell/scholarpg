from django.shortcuts import render
from django.shortcuts import render
from student_hub.forms import StudentForm, BehaviorForm, SkillForm, RandomEventForm, MiracleForm
from student_hub.models import Student, Behaviors, Skills, RandomEvents, Miracles
import random
#CONTROL
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # STUDENTS # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# load the homepage to view all students
def homepage(req, msg=None):
    #get students

    #if there are students, send them to be rendered
    if Student.objects.exists():
        students = Student.objects.all()
        context={'students': students, 'msg': msg}
        return render(req, 'index.html', context)
    else: 
    #if no students, render without students
        return render(req, 'index.html')

#load the page to view one student
def view_student(req, pk):
    #get the one student by primary key
    student = Student.objects.get(pk=pk)
    #get the list of behaviors
    behaviors = Behaviors.objects.all()
    #get the list of skills that match the character class
    skills = Skills.objects.all().filter(charClass=student.charClass)
    #send data to page to be rendered
    context = {'student': student, 'behaviors': behaviors, 'skills': skills}
    return render(req, 'view_student.html', context)

#load the page to add a student 
def add_student_form(req):
    #render the add student form
    return render(req, 'add_student_form.html')

#submit the page to add a student
def add_student(req):
    #ensure sent via POST
    if req.method == 'POST':
        #get the form
        form = StudentForm(req.POST)
        #if it's valid...
        if form.is_valid():
            #try to save
            try:
                form.save()
                #send to confirmation page
                context = {'h2': 'Student Added'}
                return render(req, "confirmation.html", context)
            #if fail, reload with error msg
            except:
                form = StudentForm()
                context={'form': form, 'msg': "Please fill out the form entirely"}
                return render(req, "add_student_form.html", context)    
        #if not valid (which should never happen since there's validation in the form itself)
        #reload the form with a msg to fill it out properly
        else:
            form = StudentForm()
            context={'form': form, 'msg': "Please fill out the form entirely"}
            return render(req, "add_student_form.html", context)
    else:
        #if it's not sent via post, then reload the form.
        form = StudentForm()
        context={'form': form}
        return render(req, "add_student_form.html", context)

#load the page to update a single student
def update_student_form(req, pk):
    #get the student by primary key
    student = Student.objects.get(pk=pk)
    #send the student info to be rendered on the page
    context={'student': student}
    return render(req, 'update_student_form.html', context)

#submit the page to update a single student
def update_student(req, pk):
    #get the student
    student = Student.objects.get(pk=pk)
    #ensure it's sent via post
    if req.method == "POST":
        #get and set all student info to be updated
        name = req.POST['name']
        image = req.POST['image']
        charClass = req.POST['charClass']
        student.name = name
        student.image = image
        student.charClass = charClass
        #try save the student with the new info
        try:
            student.save()
            #send to the confirmation page
            context = {
                'h2': f"{student.name} Updated"
            }
            return render(req, "confirmation.html", context)
        # if fail, reload with error msg
        except:
            context = {"student": student, "msg": "There was an error. Student not updated."}
            return render(req, "update_student_form.html", context)
    #if not, send back to the update student page with an error msg
    else:
        context = {"student": student, "msg": "There was an error. Student not updated."}
        return render(req, "update_student_form.html", context)

#load page to delete student
def delete_student_form(req, pk):
    #get student
    student = Student.objects.get(pk=pk)
    #send student info to be loaded on the page
    context = {'student': student}
    return render(req, 'delete_student.html', context)

#submit student to be deleted
def delete_student(req, pk):
    #get the student
    student = Student.objects.get(pk=pk)
    #ensure request sent via post
    if req.method == "POST":
        #try to delete the student
        try:
            student.delete()
            #send to confirmation page
            context = {"h2": "Student Deleted"}
            return render(req, "confirmation.html", context)
        #if fail, reload with error msg
        except:
            context = {"student": student, "msg": "There was an error. Student not deleted."}
            return render(req, 'delete_student.html', context)
    #if not, reload the page with an error message
    else: 
        context = {"student": student, "msg": "There was an error. Student not deleted."}
        return render(req, 'delete_student.html', context)
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # BEHAVIORS # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#load page to view all behaviors
def view_behaviors(req):
    #if there are any behaviors, get them
    if Behaviors.objects.exists():
        behaviors = Behaviors.objects.all()
        #send them to be rendered
        context={'behaviors': behaviors}
        return render(req, 'student_behaviors.html', context)
    #if none render the page empty
    else: 
        return render(req, 'student_behaviors.html')
    
#load page to add new behavior
def add_behavior_form(req):
    #render page to add a new behavior
    return render(req, 'add_behavior_form.html')

#submit new behavior to be added
def add_behavior(req):
    #ensure request is sent via POST
    if req.method == 'POST':
        #get the form
        form = BehaviorForm(req.POST)
        #if the form is valid (which it should be since there's validation on the form)
        if form.is_valid():
            #try to save it
            try:
                form.save()
                #send to confirmation page
                context={'h2':'Behavior Added'}
                return render(req, 'confirmation.html', context)
            except:
                form = BehaviorForm()
                context={'form': form, 'msg': "Something went wrong. Behavior not added"}
                return render(req, "add_behavior_form.html", context)
    #if not, reload the form with an error msg
    else:
        form = BehaviorForm()
        context={'form': form, 'msg': "Something went wrong. Behavior not added"}
        return render(req, "add_behavior_form.html", context)

#load the update behavior page
def update_behavior_form(req, pk):
    #get the behavior by primary key
    behavior = Behaviors.objects.get(pk=pk)
    #send it to be rendered on the page
    context= {'behavior': behavior}
    return render(req, 'update_behavior_form.html', context)

#submit the updated behavior
def update_behavior(req, pk):
    #get the behavior by primary key
    behavior = Behaviors.objects.get(pk=pk)
    #ensure submitted via POST
    if req.method == "POST":
        #get and set the updated behavior info
        title = req.POST['title']
        desc = req.POST['desc']
        xp = req.POST['xp']
        gp = req.POST['gp']
        behavior.title = title
        behavior.desc = desc
        behavior.xp = xp
        behavior.gp = gp
        #try to save the new behavior info
        try:
            behavior.save()
            #send to confirmation page
            context = {'h2': "Behavior Updated"}
            return render(req, "confirmation.html", context)
        #if fail, reload the page with an error msg
        except:
            context = {"behavior": behavior, "msg": "There was an error. Behavior not updated."}
            return render(req, "update_behavior_form.html", context)
    #if not, reload the page with an error msg
    else:
        context = {"behavior": behavior, "msg": "There was an error. Behavior not updated."}
        return render(req, "update_behavior_form.html", context)

#load the delete behavior page
def delete_behavior_form(req, pk):
    #get behavior by primary key
    behavior = Behaviors.objects.get(pk=pk)
    #send it to be rendered on the page
    context = {'behavior': behavior}
    return render(req, 'delete_behavior.html', context)

#submit behavior to be deleted
def delete_behavior(req, pk):
    #get the behavior by primary key
    behavior = Behaviors.objects.get(pk=pk)
    #ensure request sent via POST
    if req.method == "POST":
        # delete the behavior
        try:
            behavior.delete()
            #send to confirmation page
            context = {"h2": "Behavior Deleted"}
            return render(req, "confirmation.html", context)
        #if fail, reload page with error msg
        except: 
            context = {"behavior": behavior, "msg": "There was an error. Behavior not deleted."}
            return render(req, 'delete_behavior.html', context)
    #if not, reload page with error msg
    else: 
        context = {"behavior": behavior, "msg": "There was an error. Behavior not deleted."}
        return render(req, 'delete_behavior.html', context)

#award behavior to student
def award_behavior(req):
    #get behavior primary key from the request
    bpk = req.POST.get('bpk')
    #get student primary key from the request
    spk = req.POST.get('spk')
    #get behavior by primary key
    behavior = Behaviors.objects.get(pk=bpk)
    #get student by primary key
    student = Student.objects.get(pk=spk)
    #ensure request sent via POST
    if req.method == "POST":
        #increment student xp by the amount stated in the behavior
        student.xp += behavior.xp
        #increment student gp by the amount stated in the behavior
        student.gp += behavior.gp
        try:
            #save the student
            student.save()
            #send to confirmation page
            context = {"h2": f"{behavior.title} Awarded! +{behavior.xp} XP & {behavior.gp} GP"}
            return render(req, "confirmation.html", context)
        #if fail, reload with error msg.
        except:
            context = {"student": student, "msg": "There was an error. Behavior not awarded."}
            return render(req, "view_student.html", context)
    #if not, reload page with error msg
    else: 
        context = {"student": student, "msg": "There was an error. Behavior not awarded."}
        return render(req, "view_student.html", context)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # SKILLS# # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#load page to view all skills
def view_skills(req):
    #if any exist...
    if Skills.objects.exists():
        #get all skills
        skills = Skills.objects.all()
        #send them to the page to be rendered
        context={'skills': skills}
        return render(req, 'student_skills.html', context)
    #if there aren't any... 
    else: 
        #render the page empty
        return render(req, 'student_skills.html')

#load page to add a skill
def add_skill_form(req):
    #render the page
    return render(req, 'add_skill_form.html')

#submit a new skill
def add_skill(req):
    #ensure request sent via POST
    if req.method == 'POST':
        #get the form
        form = SkillForm(req.POST)
        #if it's valid (which it should be. Validation on form)
        if form.is_valid():
            #try to save it
            try:
                form.save()
                #send to confirmation page
                context={'h2':'Skill Added'}
                return render(req, 'confirmation.html', context)
            #if fail, reload form with error message
            except:
                form = SkillForm()
                context={'form': form, 'msg': "Somethign went wrong. Skill not added"}
                return render(req, "add_skill_form.html", context)
    #if not, reload form with error message
    else:
        form = SkillForm()
        context={'form': form, 'msg': "Somethign went wrong. Skill not added"}
        return render(req, "add_skill_form.html", context)

#load the page to update a skill
def update_skill_form(req, pk):
    #get the skill by primary key
    skill = Skills.objects.get(pk=pk)
    #send skill to page to be rendered
    context={'skill': skill}
    return render(req, 'update_skill_form.html', context)

#submit updated skill
def update_skill(req, pk):
    #get the skill by primary key
    skill = Skills.objects.get(pk=pk)
    #ensure request sent via POST
    if req.method == "POST":
        #get and set fields for skill
        title = req.POST['title']
        desc = req.POST['desc']
        charClass = req.POST['charClass']
        sp = req.POST['sp']
        levelReq = req.POST['levelReq']
        skill.title = title
        skill.desc = desc
        skill.charClass = charClass
        skill.sp = sp
        skill.levelReq = levelReq
        #try to save skill with new info
        try:
            skill.save()
            #send to confirmation page
            context = {'h2': "Skill Updated"}
            return render(req, "confirmation.html", context)
        #if fail, reload form with error message
        except:
            context = {"skill": skill, "msg": "There was an error. Skill not updated."}
            return render(req, "update_skill_form.html", context)
    #if not, reload form with error message
    else:
        context = {"skill": skill, "msg": "There was an error. Skill not updated."}
        return render(req, "update_skill_form.html", context)
#load page to confirm deletion of skill
def delete_skill_form(req, pk):
    #get the skill by primary key
    skill = Skills.objects.get(pk=pk)
    #send to page to be rendered
    context = {'skill': skill}
    return render(req, 'delete_skill.html', context)

#submit skill to be deleted
def delete_skill(req, pk):
    #get the skill by primary key
    skill = Skills.objects.get(pk=pk)
    #ensure request sent via POST
    if req.method == "POST":
        #try to delete skill
        try:
            skill.delete()
            #send to confirmation page
            context = {"h2": "Skill Deleted"}
            return render(req, "confirmation.html", context)
        #if fail, reload form with error message
        except: 
            context = {"skill": skill, "msg": "There was an error. Skill not deleted."}
            return render(req, 'delete_skill.html', context)
    #if not, reload form with error message
    else: 
        context = {"skill": skill, "msg": "There was an error. Skill not deleted."}
        return render(req, 'delete_skill.html', context)

#use skill
def use_skill(req):
    #get skill primary key from request
    skillpk = req.POST['skillpk']
    #get student primary key from request
    studentpk = req.POST['spk']
    #get the skill by primary key
    skill = Skills.objects.get(pk=skillpk)
    #get the student by primary key
    student = Student.objects.get(pk=studentpk)
    #ensure request sent via POST
    if req.method == "POST":
        #make sure student has enough SP to use skill
        if student.sp >= skill.sp:
            #decrement student's SP based on skill's SP cost
            student.sp -= skill.sp
            #try to save student
            try:
                student.save()
                #send to confirmation page
                context = {'h2': f"Skill Used. {student.name}'s SP = {student.sp}"}
                return render(req, "confirmation.html", context)
            #if fail, reload the page with error message
            except: 
                context = {"student": student, "msg": "There was an error. Skill not used."}
                return render(req, 'view_student.html', context)
        #if not enough SP, render page with msg
        else: 
            context = {'student': student, 'msg': "Not enough SP to use that skill."}
            return render(req, "view_student.html", context)
    #if not, reload the page with error message
    else: 
        context = {"student": student, "msg": "There was an error. Skill not used."}
        return render(req, 'view_student.html', context)
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # RANDOM EVENTS # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#load page of classroom tools
def view_classroom_tools(req):
    return render(req, 'classroom_tools.html')

#load page to roll a random event
def view_random_event(req):
    msg=''
    #if there are random events...
    if RandomEvents.objects.exists():
        #get all students
        allStudents = Student.objects.all()
        
        #Count how many events
        noOfEvents = RandomEvents.objects.count()
        #get all events
        events = RandomEvents.objects.all()

        #if there's only 1, just display it. Random can't handle it.
        if RandomEvents.objects.count() == 1: 
            event = events[0]
        #if more than one, get a random event.
        else:
            #get a ruandom number between 0 and the number of events-1
            upperLimit = noOfEvents-1
            randomNumber = random.choices(range(0,upperLimit ), k=1)[0]
            #display the event at that random index
            event = events[randomNumber]
        
        #if students limited to charClass, filter them
        if event.charClass != "None": 
            students = allStudents.filter(charClass=event.charClass)
            

        #if student limited to one student
        if event.randomStudent:
            #count how many students there are after limits imposed
            noOfStudents = Student.objects.count()
            #get a random number between 1 and the number of students
            upperStudentLimit = noOfStudents-1
            randomStudentNumber = random.choices(range(0,upperStudentLimit ), k=1)[0]
            #if limited by charClass and there's at least one student, get a random student
            if event.charClass != "None" and students.count() > 0:
                randomStudent = students[randomStudentNumber]
            #if limited by charClass and there are no students, send no student
            if event.charClass != "None" and students.count() == 0:
                randomStudent = None
            #otherwise, just get a random student
            else:
                randomStudent = allStudents[randomStudentNumber]

        #if the event gives SP
        if event.sp > 0:
            #everyone gets some
            for student in allStudents:
                student.sp += event.sp
                #if it pushes them over the max, set to max.
                if student.sp > student.maxSP:
                    student.sp = student.maxSP
                #try to save the student
                try:
                    student.save()
                except:
                    msg += f"SP was not saved for {student}. Manually add it.\n"

            #limited students get more sp. 
            #If limited to charClass, but not a random student, give sp
            if event.charClass != "None" and not event.randomStudent:
                #if there are students of that charClass
                if students.count()>0:
                    for student in students:
                        student.sp += event.sp
                    #if it pushes them over the max, set to max.
                    if student.sp > student.maxSP:
                        student.sp = student.maxSP
                    try:
                        student.save()
                    except:
                        msg += f"SP was not saved for {student}. Manually add it.\n"
            #If limited to just one student, give sp
            if event.randomStudent:
                #if there is a random Student
                if randomStudent:
                    randomStudent.sp += event.sp
                    #if it pushes them over the max, set to max.
                    if randomStudent.sp > randomStudent.maxSP:
                        randomStudent.sp = randomStudent.maxSP
                    try:
                        randomStudent.save()
                    except: 
                        msg += f"SP was not saved for {student}. Manually add it.\n"
        #if event gives xp
        if event.xp > 0:
            #If limited to charClass, but not a random student, give xp
            if event.charClass != "None" and not event.randomStudent:
                #if there are students of that charClass
                if students.count()>0:
                    for student in students:
                        student.xp += event.xp
                        #try to save the student
                        try:
                            student.save()
                        except:
                            msg += f"{event.xp}XP was not saved for {student}. Manually add it.\n"
            #else if limited to just one student, give xp
            elif event.randomStudent:
                #if there is a random student
                if randomStudent:
                    randomStudent.xp += event.xp
                    #try to save student
                    try:
                        randomStudent.save()
                    except:
                        msg += f"{event.xp}XP was not saved for {randomStudent}. Manually add it.\n"
            #otherwise everyone gets some
            else:
                for student in allStudents:
                    student.xp += event.xp
                    try:
                        student.save()
                    except:
                        msg += f"{event.xp}XP was not saved for {student}. Manually add it.\n"
        #if event gives gold
        if event.gp > 0:
            #If limited to charClass, but not a random student, give gp
            if event.charClass != "None" and not event.randomStudent:
                #if there are students of that charClass
                if students.count()>0:
                    for student in students:
                        student.gp += event.gp
                        try:
                            student.save()
                        except:
                            msg += f"{event.gp}GP was not saved for {student}. Manually add it.\n"
            #else if limited to just one student, give gp
            elif event.randomStudent:
                #if there is a random student
                if randomStudent:
                    randomStudent.gp += event.gp
                    try:
                        randomStudent.save()
                    except:
                            msg += f"{event.gp}GP was not saved for {randomStudent}. Manually add it.\n"
            #otherwise everyone gets some
            else:
                for student in allStudents:
                    student.gp += event.gp
                    try:
                        student.save()
                    except:
                            msg += f"{event.gp}GP was not saved for {student}. Manually add it.\n"
        #set the context
        if event.randomStudent:
            context = {'event': event, 'student': randomStudent}
        else:
            context = {'event': event, 'msg': msg}
        #send event info to be rendered
        return render(req, 'roll_random_event.html', context)
    #if there are no random events, just display the events page. You can't pull one from nothing.
    else: 
        return render(req, 'view_random_events.html')

#load page to view all random events
def view_random_events(req):
    #if any exist...
    if RandomEvents.objects.exists():
        #get random events
        events = RandomEvents.objects.all()
        #send them to be rendered
        context={'events': events}
        return render(req, 'view_random_events.html', context)
    #if not, render an empty page
    else: 
        return render(req, 'view_random_events.html')

#load page to add a random event
def add_random_event_form(req):
    #render page
    return render(req, 'add_random_event_form.html')

#submit a new random event
def add_random_event(req):
    #ensure request sent via POST
    if req.method == 'POST':
        #get the form
        form = RandomEventForm(req.POST)
        #if it's valid (it should be. validation on form)
        if form.is_valid():
            #try to save form
            try:
                form.save()
                #send to confirmation page
                context={'h2':'Random Event Added'}
                return render(req, 'confirmation.html', context)
            #if fail, reload page with error msg
            except:
                form = RandomEventForm()
                context={'form': form, 'msg': 'Something went wrong. Random Event not added.'}
                return render(req, "add_random_event_form.html", context)
    #if not, reload page with error msg
    else:
        form = RandomEventForm()
        context={'form': form, 'msg': 'Something went wrong. Random Event not added.'}
        return render(req, "add_random_event_form.html", context)

#load page to update random event
def update_random_event_form(req, pk):
    #get event by primary key
    event = RandomEvents.objects.get(pk=pk)
    #send to be rendered on page
    context={'event': event}
    return render(req, 'update_random_event_form.html', context)

#submit random event to be updated
def update_random_event(req, pk):
    #get event by primary key
    event = RandomEvents.objects.get(pk=pk)
    #ensure request sent via POST
    if req.method == "POST":
        #get and set fields
        title = req.POST['title']
        desc = req.POST['desc']
        charClass = req.POST['charClass']
        sp = req.POST['sp']
        xp = req.POST['xp']
        gp = req.POST['gp']
        #try to get a random student from the event
        try:
            randomStudent = req.POST['randomStudent']
        #if there isn't one, set it to false
        except: 
            randomStudent = False
        event.title = title
        event.desc = desc
        event.charClass = charClass
        event.randomStudent = randomStudent
        event.sp = sp
        event.xp = xp
        event.gp = gp
        #try to save event
        try:
            event.save()
            #send to confirmation page
            context = {'h2': "Random Event Updated"}
            return render(req, "confirmation.html", context)
        #if fail reload page with error msg
        except: 
            context = {"event": event, "msg": "There was an error. Event was not updated."}
            return render(req, "update_random_event_form.html", context)
    #if not reload page with error msg
    else: 
        context = {"event": event, "msg": "There was an error. Event was not updated."}
        return render(req, "update_random_event_form.html", context)

#load page to confirm deletion of event
def delete_random_event_form(req, pk):
    #get event by primary key
    event = RandomEvents.objects.get(pk=pk)
    #send event to be rendered on the page
    context = {'event': event}
    return render(req, 'delete_random_event.html', context)

#submit event deletion
def delete_random_event(req, pk):
    #get event by primary key
    event = RandomEvents.objects.get(pk=pk)
    #ensure request sent via POST
    if req.method == "POST":
        #try to delete event
        try:
            event.delete()
            #send to confirmation page
            context = {"h2": "Event Deleted"}
            return render(req, "confirmation.html", context)
        #if fail, reload page with error msg
        except:
            context = {"event": event, "msg": "There was an error. Event was not deleted."}
            return render(req, 'delete_random_event.html', context)
    #if not, reload page with error msg
    else: 
        context = {"event": event, "msg": "There was an error. Event was not deleted."}
        return render(req, 'delete_random_event.html', context)
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # MIRACLES # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#load page to view miracle
def view_miracle(req):
    #if there are miracles, do all the stuff!
    if Miracles.objects.exists():
        #get all students
        allStudents = Student.objects.all()
        
        #number of miracles
        noOfMiracles = Miracles.objects.count()
        #get all miracles
        miracles = Miracles.objects.all()

        #if there's only 1, just display it. Random can't handle it.
        if Miracles.objects.count() == 1: 
            miracle = miracles[0]
        #if more than one, get a miracle.
        else:
            upperLimit = noOfMiracles-1
            randomNumber = random.choices(range(0,upperLimit ), k=1)[0]
            miracle = miracles[randomNumber]
        
        #if the miracle gives SP
        if miracle.sp > 0:
            #everyone gets some
            for student in allStudents:
                student.sp += miracle.sp
                #if it pushes them over the max, set to max.
                if student.sp > student.maxSP:
                    student.sp = student.maxSP
                student.save()
            
        #if miracle gives xp
        if miracle.xp > 0:
            #everyone gets some
            for student in allStudents:
                student.xp += miracle.xp
                student.save()
        #if miracle gives gold
        if miracle.gp > 0:
            for student in allStudents:
                student.gp += miracle.gp
                student.save()
        #set the context
        context = {'miracle': miracle}
        #return a page with variables
        return render(req, 'roll_miracle.html', context)
    #if there are no miracles, just display the miracles page. You can't pull one from nothing.
    else: 
        return render(req, 'view_miracles.html')

#load page to view all miracles
def view_miracles(req):
    #if there are any
    if Miracles.objects.exists():
        #get miracles
        miracles = Miracles.objects.all()
        #send to be rendered on the page
        context={'miracles': miracles}
        return render(req, 'view_miracles.html', context)
    #if none, render an empty page.
    else: 
        return render(req, 'view_miracles.html')

#load page to add amiracle
def add_miracle_form(req):
    #render page
    return render(req, 'add_miracle_form.html')

#submit new miracle
def add_miracle(req):
    #ensure request sent via post
    if req.method == 'POST':
        #get the form
        form = MiracleForm(req.POST)
        #if it's valid (should be- validation on form)
        if form.is_valid():
            #try to save form
            try:
                form.save()
                #send to confirmation page
                context={'h2':'Miracle Added'}
                return render(req, 'confirmation.html', context)
            #if fail, reload page with error msg
            except:
                form = MiracleForm()
                context={'form': form, 'msg': 'Something went wrong. Miracle was not added.'}
                return render(req, "add_miracle_form.html", context)
    #if not, reload page with error msg
    else:
        form = MiracleForm()
        context={'form': form, 'msg': 'Something went wrong. Miracle was not added.'}
        return render(req, "add_miracle_form.html", context)

#load page to update a miracle
def update_miracle_form(req, pk):
    #get miracle by primary key
    miracle = Miracles.objects.get(pk=pk)
    #send to be rendered on page
    context={'miracle': miracle}
    return render(req, 'update_miracle_form.html', context)

#submit miracle to be updated
def update_miracle(req, pk):
    #get miracle by primary key
    miracle = Miracles.objects.get(pk=pk)
    #ensure request sent via post
    if req.method == "POST":
        #get and set fields
        title = req.POST['title']
        desc = req.POST['desc']
        sp = req.POST['sp']
        xp = req.POST['xp']
        gp = req.POST['gp']
        miracle.title = title
        miracle.desc = desc
        miracle.sp = sp
        miracle.xp = xp
        miracle.gp = gp
        #try to save miracle
        try:
            miracle.save()
            #send to confirmation page
            context = {'h2': "Miracle Updated"}
            return render(req, "confirmation.html", context)
        #if fail, reload page with error msg
        except:
            context = {"miracle": miracle, "msg": "There was an error. Miracle was not updated."}
            return render(req, "update_miracle_form.html", context)
    #if not, reload page with error msg
    else:
        context = {"miracle": miracle, "msg": "There was an error. Miracle was not updated."}
        return render(req, "update_miracle_form.html", context)

#load page to confirmation miracle deletion
def delete_miracle_form(req, pk):
    #get miracle by primary key
    miracle = Miracles.objects.get(pk=pk)
    #send to be rendered on the page
    context = {'miracle': miracle}
    return render(req, 'delete_miracle.html', context)

#submit miracle deletion
def delete_miracle(req, pk):
    #get miracle by primary key
    miracle = Miracles.objects.get(pk=pk)
    #ensure request sent via post
    if req.method == "POST":
        #try to delete miracle
        try:
            miracle.delete()
            #send to confirmation page
            context = {"h2": "Miracle Deleted"}
            return render(req, "confirmation.html", context)
        #if fail, reload page with error msg
        except:
            context = {"miracle": miracle, "msg": "There was an error. Miracle was not deleted."}
            return render(req, 'delete_miracle.html', context)
    #if not, reload page with error msg
    else: 
        context = {"miracle": miracle, "msg": "There was an error. Miracle was not deleted."}
        return render(req, 'delete_miracle.html', context)