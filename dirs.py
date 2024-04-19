#### generator ####
import os
dirs=["static"]
worked=[]
def rdir(d:str):
    dirs=[d]
    worked.append(d)
    for i in os.listdir(d):
        nd=f"{d}/{i}"
        if os.path.isdir(nd):
            if not i in dirs:dirs.append(nd)
            if not nd in worked:rdir(nd)
        


#### //generator ####



dirs=['static', 'static/js', 'static/css', 'static/images', 'static/dependences', 'static/dependences/others', 'static/qfiles', 'static/pdfs', 'static/audios', 'static/pics', 'static/jsons', 'static/jsons/pdfs', 'static/jsons/selfCalendar', 'static/jsons/dbs', 'static/jsons/tasks', 'static/jsons/grades', 'static/pdf', 'static/fonts', 'static/files', 'static/archived', 'static/menu_images', 'static/qrcode', 'static/ods', 'static/ods/example', 'static/profile_pics', 'static/profile_pics/default']